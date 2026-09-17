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

# let's convert tokens into token ids
    # we build a vocabulary by tokenizing the eentire text in a training dataset into individual tokens who are sorted alphabetically
    # duplicate tokens are removed, unique tokens are aggregated into a vocabulary that defines a mapping from  each unique token to a unique integer value

# we create a list of all unique tokens and sort them alphabetically
all_words = sorted(set(preprocessed))
vocab_size = len(all_words) #after sorted we can determine the vocabulary size
print(vocab_size)
# we create a vocabulary
vocab = {token: integer for integer, token in enumerate(all_words)}
for i, item in enumerate(vocab.items()):
    print(item)
    if i >= 50:
        break
# use this vocabulary to convert new text into tokens ids
    # we have the text, we have the tokenized text, we have the vocabulary, new tokenized text is mapped to tokens ids using existing vocabulary
# implementing a simple text tokenizer
class SimpleTokenizerV1:
    def __init__(self, vocab):
        self.str_to_int = vocab
        self.int_to_str = {i:s for s,i in vocab.items()}

    def encode(self, text):
        preprocessed = re.split(r'([,.?_!"()\']|--|\s)', text)
        preprocessed = [
            item.strip() for item in preprocessed if item.strip()
        ]
        ids = [self.str_to_int[s] for s in preprocessed]
        return ids

    def decode(self, ids):
        text = " ".join([self.int_to_str[i] for i in ids]) 

        text = re.sub(r'\s+([,.?!"()\'])', r'\1', text)
        return text

# let's instantiate a new tokenizer object from the class and tokenize a text passage from verdict.txt
tokenizer = SimpleTokenizerV1(vocab)
text =  """"It's the last he painted, you know,"
        Mrs. Gisburn said with pardonable pride."""
ids = tokenizer.encode(text)
print(ids)
# let's turn these tokens back into text
print(tokenizer.decode(ids))

# lets add a feature so that the tokenizer can handle unknown words
all_tokens = sorted(list(set(preprocessed)))
all_tokens.extend({"<|endoftext|>","<|unk|>"})
vocab = {token: integer for integer, token in enumerate(all_tokens)}
print(len(vocab.items()))

for i, item in enumerate(list(vocab.items())[-5:]):
    print(item)

class SimpleTokenizerV2:
    def __init__(self, vocab):
        self.str_to_int = vocab
        self.int_to_str = { i:s for s,i in vocab.items()}

    def encode(self, text):
        preprocessed = re.split(r'([,.:;?_!"()\']|--|\s)', text)
        preprocessed = [
            item.strip() for item in preprocessed if item.strip()
        ]
        preprocessed = [item if item in self.str_to_int
                        else "<|unk|>" for item in preprocessed]

        ids = [self.str_to_int[s] for s in preprocessed]
        return ids

    def decode(self, ids):
        text = " ".join([self.int_to_str[i] for i in ids])

        text = re.sub(r'\s+([,.:;?!"()\'])', r'\1', text)
        return text
# SimpleTokenizerV2 replaces unknown words with <|unk|> tokens
text1 = "Hello, do you like tea?"
text2 = "In the sunlit terraces of the palace."
text = " <|endoftext|> ".join((text1, text2))
print(text)

tokenizer = SimpleTokenizerV2(vocab)
print(tokenizer.encode(text))

print(tokenizer.decode(tokenizer.encode(text)))

# byte pair encoding bpe
# to make it easier for us, we will use an existing python source library called tiktoken
# tiktoken make it easier to encode, decode, get the token ids ...

from importlib.metadata import version
import tiktoken
print("tiktoken version", version("tiktoken"))

# lets instantiate BPE tokenizer from tiktoken
tokenizer = tiktoken.get_encoding("gpt2")
# similar to simpletokenizer2, lets encode text with tiktoken and print the token ids
text = (
    "Hello, do you like tea? <|endoftext|> In the sunlit terraces"
     "of someunknownPlace."
)
integers = tokenizer.encode(text, allowed_special={"<|endoftext|>"})
print(integers)
# let's also convert the token ids bback into text
strings = tokenizer.decode(integers)
print(strings)

# data sampling with a sliding window



