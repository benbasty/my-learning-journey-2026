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

class GPTDataset(Dataset):
    def __init__(self, text, tokenizer, max_length, stride):
        self.inputs = []
        self.targets = []

        token_ids = tokenizer.encode(text)

        for start in range(
            0,
            len(token_ids) - max_length,
            stride
        ):
            input_chunk = token_ids[
                start : start + max_length
            ]

            target_chunk = token_ids[
                start + 1 : start + max_length + 1
            ]

            self.inputs.append(
                torch.tensor(input_chunk, dtype=torch.long)
            )

            self.targets.append(
                torch.tensor(target_chunk, dtype=torch.long)
            )

    def __len__(self):
        return len(self.inputs)

    def __getitem__(self, index):
        return self.inputs[index], self.targets[index]

dataset = GPTDataset(
    raw_text,
    tokenizer,
    max_length=4,
    stride=4
)

# the class GPTDataset takes a long stream of tokens and turn it into a list of training examples,
# where each example is (input_chunk, target_chunk).
# Everything else about the class exists to make PyTorch's DataLoader able to work with those examples.

# Dataset is a PyTorch base class.
# PyTorch then expects us to implement __len__(how many items do we have), __getitem__(index) (get the item at this index)
# Once those two methods exist, a DataLoader can wrap your dataset and do all the heavy lifting (batching, shuffling, parallel loading) automatically

# __init__ is the setup that runs when you create the object
# The loop that builds every example: for start in range(0, len(token_ids) - max_length, stride):
# The two slices — this is the heart of the class
    # input_chunk = token_ids[start : start + max_length] | input_chunk starts at start
    # target_chunk = token_ids[start + 1 : start + max_length + 1] | target_chunk starts at start + 1
# Each input_chunk and target_chunk is currently a plain Python list of ints.
# They are converted into a PyTorch tensor.
# because PyTorch models operate on tensors, not Python lists.
# __len__ returns the total number of training examples the dataset holds — which equals the number of windows the loop produced.
# The DataLoader needs to know how many items exist so it can decide how many batches to create per epoch, sample indices for shuffling,
    # Know when an epoch is finished. The DataLoader needs to know how many items exist so it can:
    # Decide how many batches to create per epoch.
    # Sample indices for shuffling.
    # Know when an epoch is finished.
# __getitem__ gives the example at index i
# the Dataloader gathers a batch of examples by repeatedly calling __getitem__ with different indices.
    # This is why your class doesn't need to know anything about batching — that's the DataLoader's job.
# summary
    # class GPTDataset(Dataset) tells PyTorch this is a dataset it can use.
    # __init__ does all the work once: tokenize, slide the window, store tensors.
    # two slices : extract the input (starting at start) and the target (starting at start + 1), which is the one-token shift.
    # torch.tensor(..., dtype=torch.long) converts Python ints to the integer tensor type PyTorch embeddings and loss functions expect.
    # __len__ — tells Python (and the DataLoader) how many examples exist.
    # __getitem__ — returns one (input, target) pair when indexed with dataset[i].

# Dataset vs DataLoader
    # Dataset represent inndividual training samples
    # DataLoader handles things like batching, shuffling, iteration, data loading
    # we have 8 Dataset examples at once for example, Dataset gives inndividual samples, Dataloader gives batches of samples

# 8. Create the dataLoader
dataloader = DataLoader(
    dataset,
    batch_size=2,
    shuffle=False,
    drop_last=True
)
batch = next(iter(dataloader))
x, y = batch
print(x)
print(y)

# A batch is a small group of training examples processed together in one step.
# DataLoader is a PyTorch utility that wraps your GPTDataset (or any Dataset)
# and handles batching, shuffling, and iteration for you.
# DataLoader uses these functions wrote in dataset(__len__ and __getitem__) to fetch examples and stack them into batches.
# DataLoader
   # asks dataset for example #0 → (x0, y0)
   # asks dataset for example #1 → (x1, y1)
   # stacks them into a batch
   # hands the batch to you










