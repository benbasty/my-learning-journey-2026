#understanding tokenization
# raw text -> tiktoken -> token ids -> pytorch dataset -> sliding window input/target samples
# -> dataloader -> batch of tokens ids -> token embeddings + positional embeddings -> final input embeddings

import tiktoken
import torch

from torch.utils.data import DataLoader, Dataset

torch.tensor
torch.arange
torch.nn.Embedding

# 1. so lets start with the python strinng, the raw text
raw_text = """
Movement makes us feel alive.
We learn by moving, experimenting, failing, and trying again.
Language models learn differently, but they also learn from patterns.
A model receives text, converts it into numbers, and tries to predict what comes next.
"""

# a neural network cannot direcltly process raw text. It needs numbers
# and we can't directly turn words into floating vector points
# so we will process it this way: text -> tokens -> tokens ids -> embeddings

# 2. lets tokenize the text
import tiktoken
tokenizer = tiktoken.get_encoding("gpt2")
tokens_id = tokenizer.encode(raw_text)
print(tokens_id[:20])

# 3. tokens ids can be decoded back into text
decoded = tokenizer.decode(tokens_id)
print(decoded)

# 4. Next-Token Prediction: How Inputs and Targets Are Created
    # at every position in the sequence, the model is asked to predict the token that comes next.
    # The target is the exact same sequence, just starting one token later.
    # Given this sequence seq = [10, 20, 30, 40, 50]
    # input_ids  = seq[:-1]   # [10, 20, 30, 40] All elements returned except from the last one
    # target_ids = seq[1:]    # [20, 30, 40, 50] All elements returned starting from index 1 to the end
    # position 0 : inputs_ids = 10, target-ids = 20
    # position 1 : inputs_ids = 20, target-ids = 30
    # position 2 : inputs_ids = 30, target-ids = 40
    # position 3 : inputs_ids = 40, target-ids = 50

# 5. Context length
    # The LLM are not training with big data such as book directly
    # instead they broken into chunks
    # we can limit each training example to contain four input tokens. max_length = 4
    # lets suppose this is the token stream [10, 20, 30, 40, 50, 60, 70, 80]
    # input: [10, 20, 30, 40]
    # target: [20, 30, 40, 50]

# 6. Sliding window
    # This time, lets use the token stream A B C D E F G H I J
    # this token stream is 10 strings long
    # Index:  0  1  2  3  4  5  6  7  8  9
    # Token:  A  B  C  D  E  F  G  H  I  J
    # Next, we choose a context length: the number of tokens the model is allowed to look at when predicting the next one.
    # context_lenght = 4 -> each training example will be an input of 4 tokens and a target of 4 tokens
    # The window is the 4-token input plus the next token, so the window has 5 positions total.
    # The window slides one token to the right each time, producing a new example.
    # Window 1 starts at index 0: input:   A  B  C  D | target:  B  C  D  E
    # Window 2 starts at index 1: input:   B  C  D  E | target:  C  D  E  F
    # Window 3 starts at index 2: input:   C  D  E  F | target:  D  E  F  G
    # Window 4 starts at index 3: input:   D  E  F  G | target:  E  F  G  H
    # Window 5 starts at index 4: input:   E  F  G  H | target:  F  G  H  I
    # Window 6 starts at index 5: input:   F  G  H  I | target:  G  H  I  J
    # the number of windows can be found out this way: len(seq) - context_lenght = 10 - 4 = 6

max_length = 4
stride = 1 # stride helps the window to move one token at a time

# 7. Create our PyTorch Dataset






