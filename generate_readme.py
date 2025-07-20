import os
import re

def extract_problem_info(filename):
    # Assuming filename format: 339A_Helpful_Maths.cpp
    match = re.match(r"(\d+[A-Z]*)_(.+)\.cpp", filename)
    if match:
        code = match.group(1)
        title = match.group(2).replace('_', ' ')
        # Separate contest_id (numeric part) and problem_letter (alphabet part)
        contest_id = re.sub(r'[A-Z]$', '', code)
        problem_letter_match = re.findall(r'[A-Z]$', code)
        problem_letter = problem_letter_match[0] if problem_letter_match else ''
        link = f"https://codeforces.com/problemset/problem/{contest_id}/{problem_letter}"
        return {
            "code": code,
            "title": title,
            "link": link,
            "filename": filename
        }
    return None

def extract_metadata(filepath):
    metadata = {
        "language": "Unknown",
        "difficulty": "Unknown",
        "tags": "None"
    }
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            for _ in range(5):  # Check first 5 lines for metadata
                line = file.readline()
                if "// Language:" in line:
                    metadata["language"] = line.split(":", 1)[1].strip()
                elif "// Difficulty:" in line:
                    metadata["difficulty"] = line.split(":", 1)[1].strip()
                elif "// Tags:" in line:
                    metadata["tags"] = line.split(":", 1)[1].strip()
    except:
        pass
    return metadata

def generate_readme():
    cpp_files = [f for f in os.listdir() if f.endswith(".cpp")]
    problems = []

    for file in sorted(cpp_files):
        info = extract_problem_info(file)
        if info:
            meta = extract_metadata(file)
            info.update(meta)
            problems.append(info)

    with open("README.md", "w", encoding='utf-8') as f:
        f.write("# 🧠 Codeforces Problem Solutions\n\n")
        f.write("This repository contains my solutions to Codeforces problems. Each solution includes a direct link to the original problem.\n\n")
        f.write("| Code | Title | Language | Difficulty | Tags | Link | File |\n")
        f.write("|------|-------|----------|------------|------|------|------|\n")
        for p in problems:
            f.write(f"| {p['code']} | {p['title']} | {p['language']} | {p['difficulty']} | {p['tags']} | [Link]({p['link']}) | [{p['filename']}]({p['filename']}) |\n")

    print("✅ README.md generated successfully!")

if __name__ == "__main__":
    generate_readme()
