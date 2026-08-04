# Data Science Environment Setup & Notebook Preflight

## Learning Goals
- Choose **NumPy** for fast homogeneous numerical computation and **Pandas** for labeled, heterogeneous tables.
- Express array operations with **vectorization**, **broadcasting**, **masks**, and deliberate axis choices.
- Build defensible joins and **split-apply-combine** analyses with explicit validation.
- Design plots whose scales, encodings, annotations, and layout answer a real question.
- Produce a **restartable notebook** whose results survive a clean kernel run.

---

## Prerequisites & Tools
No background beyond the covered chapters is assumed.

**Required setup:**
- **Python** 3.10 or higher
- **JupyterLab** or **Jupyter Notebook**
- Core libraries: `NumPy`, `Pandas`, `Matplotlib`, and `Seaborn`

---

## Launching Jupyter
Open your terminal and run the following commands in order:

1. **Initialize Conda**  
   ```bash
   conda init
2. **Activate the base environment**  
   ```bash
   conda activate
3. **Start Jupyter Lab**  
   ```bash
   jupyter lab
4. **Once the server starts, a new page should open automatically in your browser. If not, navigate to:**  
   http://localhost:8888/lab

## Preflight Cell
A **preflight cell** is the very first code cell in a Jupyter Notebook. It acts like an airplane pilot’s pre‑flight checklist—it prepares your coding environment, imports required tools, sets configuration options, and ensures your data science work is **reproducible** before you run any actual analysis.

**Copy and execute the following code block as your first cell:**

```python
import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set a specific random seed for reproducible results
rng = np.random.default_rng(20250720)
# Prevent Pandas from truncating columns – display up to 20 columns at once
pd.set_option("display.max_columns", 20)
# Apply a clean, professional style to all future plots
sns.set_theme(style="whitegrid", context="notebook")
# Verify core environment versions
print(sys.version.split()[0], np.__version__, pd.__version__)
```