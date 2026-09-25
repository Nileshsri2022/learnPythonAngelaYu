#!/usr/bin/env python3
"""
Generate structured lecture note .md files from transcripts.

Reads angelaYu/transcripts/Day N/*.txt and writes angelaYu/Day N/*.md
with structured study notes in the same style as the learnAndroidDev repo.
"""

import html
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent.parent  # repo root
TRANSCRIPTS = REPO / "angelaYu" / "transcripts"

DASHES_RE = re.compile(r"^-{5,}\s*$")

LEVEL_EMOJI = {
    "Beginner": "🐍",
    "Intermediate": "🔧",
    "Intermediate+": "🚀",
    "Advanced": "🎓",
    "Professional": "💼",
}

# Topics for each day (condensed titles for the Key Concepts table)
DAY_TOPICS = {
    1: "Working with Variables in Python to Manage Data",
    2: "Understanding Data Types and How to Manipulate Strings",
    3: "Control Flow and Logical Operators",
    4: "Randomisation and Python Lists",
    5: "Python Loops",
    6: "Python Functions & Karel",
    7: "Hangman",
    8: "Function Parameters & Caesar Cipher",
    9: "Dictionaries, Nesting and the Secret Auction",
    10: "Functions with Outputs",
    11: "The Blackjack Capstone Project",
    12: "Scope & Number Guessing Game",
    13: "Debugging: How to Find and Fix Errors in your Code",
    14: "Higher Lower Game Project",
    15: "Local Development Environment Setup & the Coffee Machine",
    16: "Object Oriented Programming (OOP)",
    17: "The Quiz Project & the Benefits of OOP",
    18: "Turtle & the Graphical User Interface (GUI)",
    19: "Instances, State and Higher Order Functions",
    20: "Build the Snake Game Part 1: Animation & Coordinates",
    21: "Build the Snake Game Part 2: Inheritance & List Slicing",
    22: "Build Pong: The Famous Arcade Game",
    23: "The Turtle Crossing Capstone Project",
    24: "Files, Directories and Paths",
    25: "Working with CSV Data and the Pandas Library",
    26: "List Comprehension and the NATO Alphabet",
    27: "Tkinter, *args, **kwargs and Creating GUI Programs",
    28: "Tkinter, Dynamic Typing and the Pomodoro GUI Application",
    29: "Building a Password Manager GUI App with Tkinter",
    30: "Errors, Exceptions and JSON Data: Improving the Password",
    31: "Flash Card App Capstone Project",
    32: "Send Email (smtplib) & Manage Dates (datetime)",
    33: "API Endpoints & API Parameters: ISS Overhead Notifier",
    34: "API Practice: Creating a GUI Quiz App",
    35: "Keys, Authentication & Environment Variables: Send SMS",
    36: "Stock Trading News Alert Project",
    37: "Habit Tracking Project: API Post Requests & Headers",
    38: "Workout Tracking Using Google Sheets",
    39: "Capstone Part 1: Flight Deal Finder",
    40: "Capstone Part 2: Flight Club",
    41: "Introduction to HTML",
    42: "Intermediate HTML",
    43: "Introduction to CSS",
    44: "Intermediate CSS",
    45: "Web Scraping with Beautiful Soup",
    46: "Create a Spotify Playlist using the Musical Time Machine",
    47: "Create an Automated Amazon Price Tracker",
    48: "Selenium Webdriver Browser and Game Playing Bot",
    49: "Automating your Exercise Routine at the Gym",
    50: "Auto Tinder Swiping Bot",
    51: "Internet Speed X Complaint Bot",
    52: "Instagram Follower Bot",
    53: "Web Scraping Capstone: Data Entry Job Automation",
    54: "Introduction to Web Development with Flask",
    55: "HTML & URL Parsing in Flask and the Higher Lower Game",
    56: "Rendering HTML: Static files and Using Website Templates",
    57: "Templating with Jinja in Flask Applications",
    58: "Web Foundation Bootstrap",
    59: "Blog Capstone Project Part 2: Adding Styling",
    60: "Make POST Requests with Flask and HTML Forms",
    61: "Building Advanced Forms with Flask-WTForms",
    62: "Flask, WTForms, Bootstrap and CSV: Coffee & Wifi Project",
    63: "Databases with SQLite and SQLAlchemy",
    64: "My Top 10 Movies Website",
    65: "Web Design School: How to Create a Website that People will Love",
    66: "Building Your Own API with RESTful Routing",
    67: "Blog Capstone Project Part 3: RESTful Routing",
    68: "Authentication with Flask",
    69: "Blog Capstone Project Part 4: Adding Users",
    70: "Git, Github and Version Control",
    71: "Deploying Your Web Application",
    72: "Data Exploration with Pandas: College Major v.s. Your Salary",
    73: "Data Visualisation with Matplotlib: Programming Languages",
    74: "Aggregate & Merge Data with Pandas: Analyse the LEGO Dataset",
    75: "Google Trends Data: Resampling and Visualising Time Series",
    76: "Beautiful Plotly Charts & Analysing the Android App Store",
    77: "Computation with NumPy and N-Dimensional Arrays",
    78: "Linear Regression and Data Visualisation with Seaborn",
    79: "Analysing the Nobel Prize with Plotly, Matplotlib & Seaborn",
    80: "The Tragic Discovery of Handwashing: t-Tests & Distributions",
    81: "Capstone Project: Predict House Prices",
    82: "Professional Portfolio Project: Python Scripting",
    83: "Professional Portfolio Project: Python Web Development",
    84: "Final Stretch",
    85: "Bonus Lecture: Succeed in the Age of AI",
}


def get_day_info(dirname: str) -> tuple[int, str, str]:
    """Parse day number, level, and topic from directory name."""
    m = re.match(r"^(\d+)-Day\s*\d+\s*-\s*(.+?)\s*-\s*(.+)$", dirname)
    if m:
        return int(m.group(1)), m.group(2).strip(), m.group(3).strip()
    m2 = re.match(r"^(\d+)-(.+)$", dirname)
    if m2:
        return int(m2.group(1)), "", m2.group(2).strip()
    return 0, "", dirname


def parse_transcript(path: Path) -> tuple[str, str, str, str]:
    """Parse a transcript file -> (course, chapter, lecture, body)."""
    text = path.read_text(encoding="utf-8", errors="replace")
    lines = text.splitlines()
    course, chapter, lecture = "", "", path.stem
    body_start = 0

    for i, line in enumerate(lines[:12]):
        if DASHES_RE.match(line.strip()):
            body_start = i + 1
            break
        if line.startswith("Course:"):
            course = line.split(":", 1)[1].strip()
        elif line.startswith("Chapter:"):
            chapter = line.split(":", 1)[1].strip()
        elif line.startswith("Lecture:"):
            lecture = line.split(":", 1)[1].strip()

    body = "\n".join(lines[body_start:]).strip()
    return course, chapter, lecture, body


def split_into_paragraphs(body: str) -> list[str]:
    """Split transcript body into logical paragraphs."""
    raw = body.split("\n\n")
    paragraphs = []
    for p in raw:
        cleaned = " ".join(p.split()).strip()
        if cleaned and len(cleaned) > 20:
            paragraphs.append(cleaned)
    if not paragraphs:
        # Single block — split on sentence boundaries
        sentences = re.split(r'(?<=[.!?])\s+', body.strip())
        chunk = []
        for s in sentences:
            chunk.append(s)
            if len(" ".join(chunk)) > 200:
                paragraphs.append(" ".join(chunk))
                chunk = []
        if chunk:
            paragraphs.append(" ".join(chunk))
    return paragraphs


def extract_python_concepts(body: str) -> list[str]:
    """Extract Python-specific concepts mentioned in the transcript."""
    concepts = []
    pattern_map = {
        r'\bprint\s*\(': "print() function",
        r'\bdef\s+\w+': "Function definitions (def)",
        r'\bclass\s+\w+': "Class definitions (class)",
        r'\bfor\s+\w+\s+in\b': "for loops",
        r'\bwhile\s+': "while loops",
        r'\bif\s+': "if/elif/else conditionals",
        r'\btry\s*:': "try/except error handling",
        r'\bimport\s+': "Module imports",
        r'\binput\s*\(': "input() function",
        r'\brange\s*\(': "range() function",
        r'\blen\s*\(': "len() function",
        r'\bstr\s*\(': "String conversion (str())",
        r'\bint\s*\(': "Integer conversion (int())",
        r'\bfloat\s*\(': "Float conversion (float())",
        r'\blist\s*\(': "list() / List operations",
        r'\bdict\s*\(': "dict() / Dictionary operations",
        r'\bappend\s*\(': "List .append() method",
        r'\.split\s*\(': "String .split() method",
        r'\.join\s*\(': "String .join() method",
        r'\.strip\s*\(': "String .strip() method",
        r'\.lower\s*\(': "String .lower() method",
        r'\.upper\s*\(': "String .upper() method",
        r'\.replace\s*\(': "String .replace() method",
        r'\bopen\s*\(': "File I/O with open()",
        r'\bwith\s+open': "Context managers (with open)",
        r'\bf\s*["\']': "f-strings for string formatting",
        r'\.format\s*\(': "String .format() method",
        r'lambda\s': "Lambda functions",
        r'\bmap\s*\(': "map() function",
        r'\bfilter\s*\(': "filter() function",
        r'\bzip\s*\(': "zip() function",
        r'\benumerate\s*\(': "enumerate() function",
        r'\bsorted\s*\(': "sorted() function",
        r'list comprehension': "List comprehensions",
        r'\btkinter\b': "Tkinter GUI framework",
        r'\bflask\b': "Flask web framework",
        r'\brequests\.\b': "requests library (HTTP)",
        r'\bBeautifulSoup\b': "BeautifulSoup (web scraping)",
        r'\bpandas\b': "Pandas library",
        r'\bmatplotlib\b': "Matplotlib (data visualization)",
        r'\bnumpy\b': "NumPy library",
        r'\bSQLite\b': "SQLite database",
        r'\bSQLAlchemy\b': "SQLAlchemy ORM",
        r'\bjson\b': "JSON data handling",
        r'\bsmtplib\b': "smtplib (sending emails)",
        r'\bdatetime\b': "datetime module",
        r'\brandom\b': "random module",
        r'\bos\.\b': "os module (file/system operations)",
        r'\bselenium\b': "Selenium web automation",
    }

    for pattern, concept in pattern_map.items():
        if re.search(pattern, body, re.I):
            concepts.append(concept)
            if len(concepts) >= 12:
                break
    return concepts


def identify_teaching_segments(body: str) -> list[tuple[str, str]]:
    """Identify distinct teaching segments in the transcript."""
    segments = []
    paragraphs = split_into_paragraphs(body)

    current_topic = ""
    current_text = []

    topic_patterns = [
        (r'(?:let me show you|let\'s (?:look at|see|create|build|start|write|try|go))', "Demonstration"),
        (r'(?:the (?:key|important|main|first|next) (?:thing|concept|point|step|part))', "Key Point"),
        (r'(?:this is (?:called|known as|basically|actually))', "Concept Explanation"),
        (r'(?:remember (?:that|to|this)|don\'t forget)', "Remember"),
        (r'(?:the (?:syntax|structure|format|way) (?:is|for|to))', "Syntax/Structure"),
        (r'(?:for example|for instance|e\.g\.)', "Example"),
        (r'(?:the (?:difference|problem|issue|reason) (?:is|with|why))', "Explanation"),
        (r'(?:we can (?:also|use|create|do|make|add))', "Additional Concept"),
        (r'(?:challenge|exercise|try it|pause the video|give (?:this|that) a go)', "Practice Challenge"),
    ]

    for para in paragraphs:
        found_topic = None
        for pattern, topic_name in topic_patterns:
            if re.search(pattern, para[:200], re.I):
                found_topic = topic_name
                break

        if found_topic and found_topic != current_topic:
            if current_text:
                segments.append((current_topic, " ".join(current_text)))
            current_topic = found_topic
            current_text = [para]
        else:
            current_text.append(para)

    if current_text:
        segments.append((current_topic, " ".join(current_text)))

    return segments


def clean_sentence(text: str) -> str:
    """Clean up a transcript sentence for note use."""
    text = re.sub(r'^(?:And |So |Now |Well,? |But |Also,? |Then |Right[.,]?\s+)', '', text)
    text = text.strip()
    if text and text[0].islower():
        text = text[0].upper() + text[1:]
    return text


def escape_html(text: str) -> str:
    """Escape raw HTML tags in transcript text so they render as literal text."""
    return html.escape(text)


def generate_note(day_num: int, level: str, topic: str,
                  lecture_num: int, transcript_path: Path) -> str:
    """Generate a structured lecture note from a transcript."""
    course, chapter, lecture, body = parse_transcript(transcript_path)

    if not body or len(body) < 50:
        return ""

    # Escape HTML tags in the body to prevent them being rendered as live HTML
    body = escape_html(body)

    emoji = LEVEL_EMOJI.get(level, "📖")
    concepts = extract_python_concepts(body)
    paragraphs = split_into_paragraphs(body)

    lines = []

    # Title
    lines.append(f"# {emoji} {lecture}")
    lines.append("")

    # Metadata block (like Android repo)
    lines.append("---")
    lines.append("")
    lines.append("### Overview")
    lines.append("")
    lines.append(f"**Course:** {course or '100 Days of Code: The Complete Python Pro Bootcamp'}")
    lines.append(f"**Chapter:** {chapter or f'Day {day_num} - {level} - {topic}'}")
    lines.append(f"**Lecture:** {lecture}")
    lines.append(f"**Level:** {level or 'N/A'}")
    lines.append("")
    lines.append("---")
    lines.append("")

    # Summary (first paragraph or two)
    lines.append("### Summary")
    lines.append("")
    summary_paras = paragraphs[:2] if len(paragraphs) >= 2 else paragraphs[:1]
    for p in summary_paras:
        lines.append(p)
        lines.append("")
    lines.append("---")
    lines.append("")

    # Key Concepts table
    if concepts:
        lines.append("### Key Concepts")
        lines.append("")
        lines.append("| # | Concept | Description |")
        lines.append("|---|---------|-------------|")
        for i, concept in enumerate(concepts, 1):
            lines.append(f"| {i} | **{concept}** | Introduced/used in this lecture |")
        lines.append("")
        lines.append("---")
        lines.append("")

    # Detailed Notes (body paragraphs with some structure)
    if len(paragraphs) > 2:
        lines.append("### Detailed Notes")
        lines.append("")

        for para in paragraphs[2:]:
            # Make some paragraphs into sub-headings
            first_words = para[:80].lower()
            if any(kw in first_words for kw in
                   ["first,", "firstly,", "step 1", "let's start",
                    "let me show", "let's create", "let's build"]):
                lines.append(f"#### Step-by-Step")
                lines.append("")
            elif any(kw in first_words for kw in
                     ["the key", "important", "remember", "note that",
                      "don't forget", "keep in mind"]):
                lines.append(f"#### 💡 Key Point")
                lines.append("")
            elif any(kw in first_words for kw in
                     ["for example", "for instance", "here's an example",
                      "let me demonstrate"]):
                lines.append(f"#### Example")
                lines.append("")

            lines.append(para)
            lines.append("")
        lines.append("---")
        lines.append("")

    # Practice Exercise (only if explicitly mentioned)
    exercise_paras = []
    for p in paragraphs:
        pl = p.lower()
        if any(kw in pl for kw in ["pause the video", "give this challenge a go",
                                     "your challenge", "try it yourself",
                                     "your turn to", "give that a go"]):
            exercise_paras.append(p)
    if exercise_paras:
        lines.append("### 🏋️ Practice Exercise")
        lines.append("")
        for p in exercise_paras[:2]:  # Max 2 paragraphs
            lines.append(p)
            lines.append("")
        lines.append("---")
        lines.append("")

    # Next Steps (last paragraph if it mentions next lesson)
    if paragraphs:
        last = paragraphs[-1].lower()
        if any(kw in last for kw in ["next lesson", "see you", "head over",
                                      "next video", "i'll see you"]):
            lines.append("### Next Steps")
            lines.append("")
            lines.append(paragraphs[-1])
            lines.append("")

    return "\n".join(lines)


def main():
    if not TRANSCRIPTS.is_dir():
        print(f"Error: {TRANSCRIPTS} not found", file=sys.stderr)
        return 1

    total_notes = 0
    total_days = 0

    for day_dir in sorted(TRANSCRIPTS.iterdir()):
        if not day_dir.is_dir():
            continue
        day_num, level, topic = get_day_info(day_dir.name)
        if day_num == 0:
            continue

        # Create the Day N output directory
        nn = f"{day_num:02d}"
        day_name = f"{nn}-Day {day_num} - {level} - {topic}" if level else f"{nn}-{topic}"
        out_dir = REPO / "angelaYu" / day_name
        out_dir.mkdir(parents=True, exist_ok=True)

        transcripts = sorted(day_dir.glob("*.txt"))
        if not transcripts:
            continue

        total_days += 1

        for idx, t_path in enumerate(transcripts, 1):
            note_content = generate_note(day_num, level, topic, idx, t_path)
            if not note_content:
                continue

            note_name = t_path.stem + ".md"
            note_path = out_dir / note_name
            note_path.write_text(note_content, encoding="utf-8")
            total_notes += 1

        print(f"Day {day_num:2d}: {len(transcripts):3d} notes → {day_name}/")

    print(f"\n✅ Generated {total_notes} lecture notes across {total_days} days")
    return 0


if __name__ == "__main__":
    sys.exit(main())