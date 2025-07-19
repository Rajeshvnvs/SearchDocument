import os
import re
import PyPDF2

def highlight(text, word):
    return re.sub(f"(?i)({re.escape(word)})", '\033[93m\\1\033[0m', text)

folder = input("Enter the directory to search for PDFs: ").strip()
if not os.path.isdir(folder):
    print(f"Folder '{folder}' does not exist.")
    exit(1)

query = input("Enter the keyword to search: ").strip()
if not query:
    print("No keyword entered.")
    exit(1)

found = False
print(f"\nSearching for '{query}' in all .pdf files under {folder}\n")

for filename in os.listdir(folder):
    if filename.lower().endswith('.pdf'):
        filepath = os.path.join(folder, filename)
        try:
            with open(filepath, 'rb') as file:
                reader = PyPDF2.PdfReader(file)
                for page_num, page in enumerate(reader.pages):
                    try:
                        text = page.extract_text()
                        if text is None:
                            continue
                        lines = text.split('\n')
                        for i, line in enumerate(lines, 1):
                            if re.search(query, line, re.IGNORECASE):
                                if not found:
                                    found = True
                                print(f"\n\033[1m[File: {filename}] (Page {page_num+1})\033[0m")
                                print(f"Line {i}: {highlight(line.rstrip(), query)}")
                    except Exception:
                        continue
        except Exception as e:
            print(f"Could not read {filename}: {e}")
print("\nSearch complete.")
if not found:
    print(f"No matches found for '{query}'.")
