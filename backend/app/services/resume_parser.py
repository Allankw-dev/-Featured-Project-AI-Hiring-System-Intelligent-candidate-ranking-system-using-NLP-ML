import re
import pdfplumber


def extract_text(file_path: str) -> str:
    """Extract raw text from PDF or DOCX."""
    text = ""
    try:
        if file_path.endswith(".pdf"):
            with pdfplumber.open(file_path) as pdf:
                for page in pdf.pages:
                    page_text = page.extract_text()
                    if page_text:
                        text += page_text + "\n"

        elif file_path.endswith(".docx"):
            try:
                import docx
                doc = docx.Document(file_path)
                text = "\n".join([para.text for para in doc.paragraphs])
            except ImportError:
                pass

    except Exception as e:
        print(f"Error extracting text: {str(e)}")

    return text.strip()


def extract_email(text: str) -> str:
    """Extract email address from text."""
    pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
    matches = re.findall(pattern, text)
    return matches[0] if matches else ""


def extract_phone(text: str) -> str:
    """Extract phone number from text."""
    patterns = [
        r"\+?254[\s\-]?\d{3}[\s\-]?\d{6}",  # Kenya format
        r"\+?\d{1,3}[\s\-]?\(?\d{3}\)?[\s\-]?\d{3}[\s\-]?\d{4}",
        r"\d{10,12}",
    ]
    for pattern in patterns:
        matches = re.findall(pattern, text)
        if matches:
            return matches[0].strip()
    return ""


def extract_name(text: str) -> str:
    """Extract candidate name from first lines of resume."""
    lines = [line.strip() for line in text.split("\n") if line.strip()]
    for line in lines[:5]:
        # Name likely has 2-4 words, no special characters
        if re.match(r"^[A-Za-z]+(?: [A-Za-z]+){1,3}$", line):
            if len(line) > 4 and "@" not in line:
                return line
    return ""


def extract_education(text: str) -> list:
    """Extract education details from resume."""
    education = []
    degrees = [
        "bachelor", "master", "phd", "doctorate", "diploma",
        "certificate", "bsc", "msc", "mba", "bcom", "ba ", "ma ",
        "b.sc", "m.sc", "b.tech", "m.tech", "degree"
    ]
    lines = text.lower().split("\n")
    for i, line in enumerate(lines):
        if any(deg in line for deg in degrees):
            education.append(text.split("\n")[i].strip())
    return education[:5]


def extract_sections(text: str) -> dict:
    """Extract structured sections from resume."""
    sections = {
        "experience": [],
        "education": [],
        "skills": [],
        "summary": ""
    }

    section_keywords = {
        "experience": ["experience", "work history", "employment", "career"],
        "education": ["education", "academic", "qualification", "degree"],
        "skills": ["skills", "technical skills", "competencies", "expertise"],
        "summary": ["summary", "objective", "profile", "about me"]
    }

    lines = text.split("\n")
    current_section = None

    for line in lines:
        line_lower = line.lower().strip()

        for section, keywords in section_keywords.items():
            if any(kw in line_lower for kw in keywords):
                current_section = section
                break

        if current_section and line.strip():
            if current_section == "summary":
                sections["summary"] += line + " "
            else:
                sections[current_section].append(line.strip())

    return sections


def parse_resume(file_path: str) -> dict:
    """
    Full resume parsing — returns structured data.
    """
    text = extract_text(file_path)

    if not text:
        return {
            "raw_text": "",
            "name": "",
            "email": "",
            "phone": "",
            "education": [],
            "sections": {},
            "word_count": 0
        }

    return {
        "raw_text": text,
        "name": extract_name(text),
        "email": extract_email(text),
        "phone": extract_phone(text),
        "education": extract_education(text),
        "sections": extract_sections(text),
        "word_count": len(text.split())
    }