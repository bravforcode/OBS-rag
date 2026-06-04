import os
import re
import datetime
from collections import Counter

VAULT_PATH = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
STYLE_GUIDE_PATH = os.path.join(VAULT_PATH, "style-guide.md")

def analyze_style():
    all_text = ""
    file_count = 0
    
    print("Analyzing Vault style...")
    
    for root, dirs, files in os.walk(VAULT_PATH):
        for file in files:
            if file.endswith(".md") and file != "style-guide.md":
                try:
                    with open(os.path.join(root, file), 'r', encoding='utf-8') as f:
                        all_text += f.read() + "\n"
                        file_count += 1
                        if file_count > 100: # Limit sample
                            break
                except UnicodeDecodeError:
                    continue
        if file_count > 100:
            break

    # Very basic trait analysis
    traits = []
    
    # Check for bullet point preference
    bullet_count = len(re.findall(r'^\s*[\-\*]\s', all_text, re.MULTILINE))
    numbered_count = len(re.findall(r'^\s*\d+\.\s', all_text, re.MULTILINE))
    
    if bullet_count > numbered_count:
        traits.append("- Strong preference for bulleted lists over numbered lists.")
    
    # Check for header usage
    h1_count = len(re.findall(r'^#\s', all_text, re.MULTILINE))
    h2_count = len(re.findall(r'^##\s', all_text, re.MULTILINE))
    
    if h1_count > 0:
        traits.append("- Frequent use of H1 headers for structure.")
        
    # Check for sentence length (roughly)
    sentences = re.split(r'[\.\!\?]', all_text)
    avg_len = sum(len(s.split()) for s in sentences) / len(sentences) if sentences else 0
    
    if avg_len < 15:
        traits.append("- Concise writing style (average < 15 words per sentence).")
    else:
        traits.append("- Elaborate writing style (average > 15 words per sentence).")

    date_str = str(datetime.date.today())
    traits_str = "\n".join(traits)
    new_guide = f"\# Style Guide (Auto-generated)\n*Last Updated: {date_str}*\n\n## Observed Traits\n{traits_str}\n\n## Structural Rules\n1. Use YAML frontmatter for all notes.\n2. Maintain link integrity using [[WikiLinks]].\n3. Prefer flat hierarchies where possible.\n"
    
    with open(STYLE_GUIDE_PATH, 'w', encoding='utf-8') as f:
        f.write(new_guide)
        
    print(f"Updated Style Guide at {STYLE_GUIDE_PATH}")

if __name__ == "__main__":
    analyze_style()
