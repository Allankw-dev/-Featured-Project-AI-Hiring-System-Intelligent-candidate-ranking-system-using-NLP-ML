import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

COMMON_SKILLS = [
    # Programming Languages
    "python", "java", "javascript", "typescript", "c++", "c#", "ruby", "php",
    "swift", "kotlin", "go", "rust", "scala", "r", "matlab",

    # Web Frameworks
    "fastapi", "flask", "django", "react", "angular", "vue", "nodejs",
    "express", "spring", "laravel", "rails", "nextjs",

    # Databases
    "sql", "mysql", "postgresql", "mongodb", "redis", "sqlite", "oracle",
    "sql server", "dynamodb", "firebase", "supabase",

    # Cloud & DevOps
    "aws", "azure", "google cloud", "docker", "kubernetes", "terraform",
    "ci/cd", "jenkins", "github actions", "linux", "bash",

    # AI & Data Science
    "machine learning", "deep learning", "nlp", "computer vision",
    "tensorflow", "pytorch", "keras", "scikit-learn", "pandas", "numpy",
    "data analysis", "data science", "power bi", "tableau", "excel",

    # Tools & Others
    "git", "github", "gitlab", "rest api", "graphql", "microservices",
    "agile", "scrum", "jira", "figma", "html", "css", "bootstrap",
    "communication", "leadership", "teamwork", "problem solving"
]


def clean_text(text: str) -> str:
    if not text:
        return ""
    text = text.lower()
    text = re.sub(r"[^a-z0-9\s]", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text


def estimate_experience(text: str) -> float:
    """Extract years of experience from text more accurately."""
    if not text:
        return 0.0

    patterns = [
        r"(\d+)\+?\s*years?\s+(?:of\s+)?experience",
        r"(\d+)\+?\s*yrs?\s+(?:of\s+)?experience",
        r"experience\s+of\s+(\d+)\+?\s*years?",
        r"(\d+)\+?\s*years?\s+(?:in|of|with)",
    ]

    all_matches = []
    for pattern in patterns:
        matches = re.findall(pattern, text.lower())
        all_matches.extend([int(x) for x in matches])

    if all_matches:
        return float(max(all_matches))

    # Fallback: count date ranges
    date_ranges = re.findall(
        r"((?:19|20)\d{2})\s*[-–]\s*((?:19|20)\d{2}|present|current|now)",
        text.lower()
    )
    if date_ranges:
        total = 0
        for start, end in date_ranges:
            end_year = 2025 if end in ["present", "current", "now"] else int(end)
            total += max(0, end_year - int(start))
        return float(min(total, 30))

    return 0.0


def extract_skills(text: str) -> list:
    """Extract skills from text using comprehensive skill list."""
    if not text:
        return []
    lower = text.lower()
    found = [skill for skill in COMMON_SKILLS if skill in lower]
    return sorted(set(found))


def calculate_skill_gap(job_skills: list, resume_skills: list) -> dict:
    """Calculate matched and missing skills."""
    matched = [s for s in job_skills if s in resume_skills]
    missing = [s for s in job_skills if s not in resume_skills]
    extra = [s for s in resume_skills if s not in job_skills]
    return {
        "matched": matched,
        "missing": missing,
        "extra_skills": extra,
        "match_rate": round(len(matched) / len(job_skills) * 100, 2) if job_skills else 100.0
    }


def calculate_semantic_score(job_text: str, resume_text: str) -> float:
    """Calculate semantic similarity using TF-IDF."""
    job_clean = clean_text(job_text)
    resume_clean = clean_text(resume_text)

    if not job_clean or not resume_clean:
        return 0.0

    try:
        vectorizer = TfidfVectorizer(
            stop_words="english",
            ngram_range=(1, 2),
            min_df=1,
            sublinear_tf=True
        )
        tfidf_matrix = vectorizer.fit_transform([job_clean, resume_clean])
        score = float(cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])[0][0]) * 100
        return round(score, 2)
    except Exception:
        return 0.0


def get_experience_score(job_desc: str, resume_text: str) -> tuple:
    """Score experience match between job and resume."""
    job_exp = estimate_experience(job_desc)
    resume_exp = estimate_experience(resume_text)

    if job_exp > 0:
        score = min(resume_exp / job_exp, 1.0) * 100
    else:
        score = 100.0

    return round(score, 2), job_exp, resume_exp


def calculate_match(job_desc: str, resume_text: str, verification_score: float = 100.0):
    """
    Main AI scoring function.
    Returns comprehensive match analysis between job and resume.
    """
    # Semantic similarity
    semantic_score = calculate_semantic_score(job_desc, resume_text)

    # Skills analysis
    job_skills = extract_skills(job_desc)
    resume_skills = extract_skills(resume_text)
    skill_gap = calculate_skill_gap(job_skills, resume_skills)
    skills_score = skill_gap["match_rate"]

    # Experience analysis
    experience_score, job_exp, resume_exp = get_experience_score(job_desc, resume_text)

    # Weighted overall score
    overall_score = (
        0.45 * semantic_score +
        0.25 * skills_score +
        0.20 * experience_score +
        0.10 * verification_score
    )

    # Ranking label
    if overall_score >= 80:
        ranking_label = "Excellent Match"
    elif overall_score >= 60:
        ranking_label = "Good Match"
    elif overall_score >= 40:
        ranking_label = "Fair Match"
    else:
        ranking_label = "Weak Match"

    return {
        "overall_score": round(overall_score, 2),
        "semantic_score": round(semantic_score, 2),
        "skills_score": round(skills_score, 2),
        "experience_score": round(experience_score, 2),
        "verification_score": round(verification_score, 2),
        "matched_skills": skill_gap["matched"],
        "missing_skills": skill_gap["missing"],
        "extra_skills": skill_gap["extra_skills"],
        "resume_skills": resume_skills,
        "job_skills": job_skills,
        "resume_experience": resume_exp,
        "required_experience": job_exp,
        "ranking_label": ranking_label
    }


def recommend_jobs(resume_text: str, jobs: list) -> list:
    """
    Recommend best matching jobs for a candidate.
    jobs: list of dicts with 'id', 'title', 'description', 'required_skills'
    """
    recommendations = []

    for job in jobs:
        job_text = f"{job.get('title', '')} {job.get('description', '')} {job.get('required_skills', '')}"
        semantic = calculate_semantic_score(job_text, resume_text)
        resume_skills = extract_skills(resume_text)
        job_skills = extract_skills(job_text)
        skill_gap = calculate_skill_gap(job_skills, resume_skills)

        recommendations.append({
            "job_id": job.get("id"),
            "job_title": job.get("title"),
            "company": job.get("company"),
            "match_score": round((semantic + skill_gap["match_rate"]) / 2, 2),
            "matched_skills": skill_gap["matched"],
            "missing_skills": skill_gap["missing"],
        })

    return sorted(recommendations, key=lambda x: x["match_score"], reverse=True)