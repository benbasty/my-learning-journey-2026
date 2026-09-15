import re
with open(
    "/Users/benbasty/Downloads/my-learning-journey-2026/LLM/build-llm-from-scratch/working-with-text-data/the-verdict.txt",
    "r",
    encoding="utf-8"
) as f:
    raw_text = f.read()
print("Total number of characters: ", len(raw_text))
print(raw_text[:99]) # Prints the first 99 characters of the file.

# let's tokenize the text
preprocessed = re.split(r'([,.:;?_!"()\']|--|\s)', raw_text)
preprocessed = [item.strip() for item in preprocessed if item.strip()]
print(len(preprocessed))
print(preprocessed[:30])

# from pathlib import Path
# file_path = Path(__file__).parent / "the-verdict.txt"
# with file_path.open("r", encoding="utf-8") as f:
    #raw_text = f.read()

#print("Total number of characters:", len(raw_text))
#print(raw_text[:99])

# page 24 2.3