from enum import Enum
import os


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
            formatted_lines.append(f"{new_line}# {line}")
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
                # duration = lines[i+1]  # ignored
                content_line = 1 if first else 2
                content = lines[i+content_line].strip()
                formatted_lines.append(f"{time} {content}")
                i += 1 + content_line
                first = False
        else:
            # For leftover lines at the end
            formatted_lines.append(line)
            i += 1

    return "\n".join(formatted_lines)


def process_folder(folder_path, output_folder):
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        output_file_path = os.path.join(output_folder, filename)

        # Only process text files
        if os.path.isfile(file_path) and filename.endswith(".md"):
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()

            formatted_content = reformat_transcript_with_chapters(content)

            # Replace the original file
            with open(output_file_path, "w", encoding="utf-8") as f:
                f.write(formatted_content)

            print(f"Formatted file: {filename}")


# Run the script
process_folder("./course-content/raw", "./course-content")
