import tiktoken
import torch

from torch.utils.data import Dataset, DataLoader


# --------------------------------
# 1. Dataset
# --------------------------------

class GPTDataset(Dataset):

    def __init__(
        self,
        text,
        tokenizer,
        max_length,
        stride
    ):

        self.inputs = []
        self.targets = []

        token_ids = tokenizer.encode(text)

        for start in range(
            0,
            len(token_ids) - max_length,
            stride
        ):

            x = token_ids[
                start : start + max_length
            ]

            y = token_ids[
                start + 1 : start + max_length + 1
            ]

            self.inputs.append(
                torch.tensor(x, dtype=torch.long)
            )

            self.targets.append(
                torch.tensor(y, dtype=torch.long)
            )


    def __len__(self):
        return len(self.inputs)


    def __getitem__(self, index):
        return (
            self.inputs[index],
            self.targets[index]
        )


# --------------------------------
# 2. Raw text
# --------------------------------

raw_text = """
Movement makes us feel alive.
We learn by moving, experimenting, failing, and trying again.
Language models learn differently, but they also learn from patterns.
A language model converts text into tokens and attempts to predict
which token should appear next.

The process begins with text. Text becomes token IDs.
Token IDs become vectors. Those vectors eventually flow through
a transformer neural network.
""" * 5


# --------------------------------
# 3. Tokenizer
# --------------------------------

tokenizer = tiktoken.get_encoding("gpt2")


# --------------------------------
# 4. Dataset
# --------------------------------

max_length = 8

dataset = GPTDataset(
    text=raw_text,
    tokenizer=tokenizer,
    max_length=max_length,
    stride=max_length
)


# --------------------------------
# 5. DataLoader
# --------------------------------

dataloader = DataLoader(
    dataset,
    batch_size=4,
    shuffle=False,
    drop_last=True
)


# --------------------------------
# 6. Get one batch
# --------------------------------

x, y = next(iter(dataloader))

print("Input IDs:")
print(x)

print("\nInput shape:")
print(x.shape)

print("\nTarget IDs:")
print(y)

print("\nTarget shape:")
print(y.shape)


# --------------------------------
# 7. Token embedding layer
# --------------------------------

vocab_size = 50257
embedding_dim = 256

token_embedding = torch.nn.Embedding(
    vocab_size,
    embedding_dim
)


# --------------------------------
# 8. Token embeddings
# --------------------------------

token_embeddings = token_embedding(x)

print("\nToken embedding shape:")
print(token_embeddings.shape)


# --------------------------------
# 9. Positional embedding layer
# --------------------------------

context_length = 1024

position_embedding = torch.nn.Embedding(
    context_length,
    embedding_dim
)


# --------------------------------
# 10. Position IDs
# --------------------------------

positions = torch.arange(max_length)

print("\nPositions:")
print(positions)


# --------------------------------
# 11. Position embeddings
# --------------------------------

position_embeddings = position_embedding(
    positions
)

print("\nPosition embedding shape:")
print(position_embeddings.shape)


# --------------------------------
# 12. FINAL INPUT EMBEDDINGS
# --------------------------------

input_embeddings = (
    token_embeddings +
    position_embeddings
)

print("\nFinal input embedding shape:")
print(input_embeddings.shape)