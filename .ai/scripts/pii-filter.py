import re
import sys

PII_PATTERNS = {
    "Email": r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+',
    "Phone": r'\b(?:\+?\d{1,3}[-.\s]?)?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}\b',
    "IP Address": r'\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b',
    # Add more as needed
}

def scan_text(text):
    found_pii = []
    for label, pattern in PII_PATTERNS.items():
        matches = re.findall(pattern, text)
        if matches:
            found_pii.append((label, matches))
    return found_pii

def main():
    if len(sys.argv) > 1:
        # Scan files
        for arg in sys.argv[1:]:
            if os.path.exists(arg):
                with open(arg, 'r', encoding='utf-8') as f:
                    content = f.read()
                    results = scan_text(content)
                    if results:
                        print(f"PII found in {arg}:")
                        for label, matches in results:
                            print(f"  {label}: {', '.join(matches)}")
    else:
        # Interactive or piped input
        print("PII Filter: Piped mode. Paste text and Ctrl+D (or Ctrl+Z on Windows) to scan.")
        text = sys.stdin.read()
        results = scan_text(text)
        if results:
            print("\n--- PII Detection Results ---")
            for label, matches in results:
                print(f"{label}: {', '.join(matches)}")
        else:
            print("No PII detected.")

if __name__ == "__main__":
    import os
    main()
