from enum import Enum
import os
from openai import OpenAI

client = OpenAI()

# ---------- Transcript Formatter ----------


class Mode(Enum):
    SECTIONS = 1
    TRANSCRIPT = 2


def reformat_transcript_with_chapters(text):
    lines = text.splitlines()
    formatted_lines = []

    i = 0
    first = True
    mode = Mode.TRANSCRIPT.value
    while i < len(lines):
        line = lines[i].strip()

        # If empty line, preserve it
        if line == "":
            formatted_lines.append("")
            i += 1
            continue

        # Keep chapter lines as-is
        if line.startswith("Chapter"):
            mode = Mode.SECTIONS.value
            new_line = "" if first else "\n"
            formatted_lines.append(f"{new_line}# {line}\n")
            i += 1
            continue

        # Process transcript block (time + duration + text)
        if i + 2 < len(lines):
            if mode == Mode.TRANSCRIPT.value:
                time = lines[i].strip()
                content = lines[i+1].strip()
                formatted_lines.append(f"{time} {content}")
                i += 2
            else:
                time = lines[i].strip()
                content_line = 1 if first else 2
                content = lines[i+content_line].strip()
                formatted_lines.append(f"{time} {content}\n")
                i += 1 + content_line
                first = False
        else:
            # For leftover lines at the end
            formatted_lines.append(line)
            i += 1

    return "\n".join(formatted_lines)


def process_and_format_folder(input_folder, output_folder):
    os.makedirs(output_folder, exist_ok=True)

    for filename in os.listdir(input_folder):
        file_path = os.path.join(input_folder, filename)
        output_file_path = os.path.join(output_folder, filename)

        # Only process Markdown files
        if os.path.isfile(file_path) and filename.endswith(".md"):
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()

            formatted_content = reformat_transcript_with_chapters(content)

            # Save formatted file
            with open(output_file_path, "w", encoding="utf-8") as f:
                f.write(formatted_content)

            print(f"Formatted file: {filename}")


# ---------- AI Summarizer ----------

def summarize_text(text, model="gpt-4"):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful assistant that summarizes course content."},
            {"role": "user", "content": f"Please provide a concise summary for the following text:\n\n{text}"}
        ]
    )
    # Access the content of the first choice
    summary = response.choices[0].message.content.strip()
    return summary


def summarize_folder(folder_path):
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        # Only process Markdown files
        if os.path.isfile(file_path) and filename.endswith(".md"):
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()

            print(f"Generating summary for: {filename} ...")
            summary = summarize_text(content)

            summary_filename = f"{os.path.splitext(filename)[0]} Summary.md"
            output_file_path = os.path.join(folder_path, summary_filename)

            with open(output_file_path, "w", encoding="utf-8") as f:
                f.write(f"# Summary of {filename}\n\n{summary}")

            print(f"Summary saved to: {summary_filename}")


# ---------- Main ----------

RAW_FOLDER = "./course-content/raw"
OUTPUT_FOLDER = "./course-content"

# Step 1: Format transcripts
process_and_format_folder(RAW_FOLDER, OUTPUT_FOLDER)

# Step 2: Generate summaries in the same folder
summarize_folder(OUTPUT_FOLDER)
