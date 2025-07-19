import os
import re

# ------------------ CONFIG ----------------------
# For keyword highlighting in terminal (bold yellow)
def highlight(text, word):
    return re.sub(f"(?i)({re.escape(word)})", '\033[93m\\1\033[0m', text)

# -------------------------------------------------
folder = input("Enter the directory to index (e.g., D:\\TextFiles): ").strip()
if not os.path.isdir(folder):
    print(f"Folder '{folder}' does not exist.")
    exit(1)

query = input("Enter the keyword to search: ").strip()
if not query:
    print("No keyword entered.")
    exit(1)

found = False
print(f"\nSearching for '{query}' in all .txt files under {folder}\n")

for filename in os.listdir(folder):
    if filename.lower().endswith('.txt'):
        filepath = os.path.join(folder, filename)
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            lines = f.readlines()
        matches = []
        for i, line in enumerate(lines, 1):
            if re.search(query, line, re.IGNORECASE):
                # Highlight keyword in output
                matches.append(f"Line {i}: {highlight(line.rstrip(), query)}")
        if matches:
            found = True
            print(f"\n\033[1m[File: {filename}]\033[0m")
            for m in matches:
                print(m)
print("\nSearch complete.")
if not found:
    print(f"No matches found for '{query}'.")
