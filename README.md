# Sleeping-Experiment-Dataset
The Sleeping Experiment Dataset, which contains 103 individual sample data

# (Dataset Name) Radar Sleep Posture Dataset (103 Subjects)

This dataset combines two subsets into a single release:
- **70_SUBJECT_FULL_DATASET** (72 subjects)
- **30_SUBJECT_FULL_DATASET** (31 subjects)

Each subject contains multiple recording parts/sessions. For each part/session, data are organized by **sleep posture**, and each posture contains **8 radar channels** saved as `.pkl` files. A corresponding raw recording `.bag` file is stored at the subject root.

---

## 1. Directory Structure

### 1.1 Dataset Root

```text
<DATASET_ROOT>/
├─ 72_SUBJECT_FULL_DATASET/
│  ├─ 1/
│  ├─ 2/
│  ├─ ...
│  └─ 72/
└─ 31_SUBJECT_FULL_DATASET/
   ├─ 1/
   ├─ 2/
   ├─ ...
   └─ 31/
```
### 1.2 72-subject subset structure (example: subject `1`)

```text
70_SUBJECT_FULL_DATASET/1/
├─ 1/ # session/part id
│ ├─ Left (bend 1 leg)/
│ │ ├─ <hh-mm-ss>-radar1.pkl
│ │ ├─ <hh-mm-ss>-radar2.pkl
│ │ ├─ ... 
| | └─ <hh-mm-ss>-radar8.pkl
│ ├─ Left (bend both legs)/
│ ├─ ...
│ └─ Supine/
├─ 2/
└─ 3/
```
### 1.3 31-subject subset structure (example: subject `1`)

```text
30_SUBJECT_FULL_DATASET/1/
├─ 0/ # part id
│ ├─ Left (bend 1 leg)/
│ │ ├─ radar1.pkl
│ │ ├─ radar2.pkl
│ │ └─ ... radar8.pkl
│ ├─ Left (bend both legs)/
│ ├─ ...
│ └─ Supine/
├─ 1/
├─ 2/
└─ 3/
```


---

## 2. Posture Categories

Each part/session contains the following posture folders:

1. `Left (bend 1 leg)`
2. `Left (bend both legs)`
3. `Left (straight)`
4. `Mid Fowler`
5. `Prone (head to left)`
6. `Prone (head to right)`
7. `Right (bend 1 leg)`
8. `Right (bend both legs)`
9. `Right (straight)`
10. `Supine`

---

## 3. Data Files

### 3.1 `.pkl` (processed radar channels)
- Each posture folder contains **8** `.pkl` files: radar1 ... radar8.
- **70-subject subset naming**: `<hh-mm-ss>-radar<1..8>.pkl`  
  Example: `11-54-10-radar3.pkl`
- **30-subject subset naming**: `radar<1..8>.pkl`  
  Example: `radar3.pkl`

> Note: The internal structure of each `.pkl` depends on the preprocessing pipeline. Use the loading example below to inspect keys/shapes.

### 3.2 `.bag` (raw recording)
- Each subject folder includes one `.bag` file at the subject root.
- This is the depth camera raw recording for that subject (e.g., ROS bag).

---


## 4. Loading Examples

### 4.1 Load `.pkl` in Python
```python
import pickle
from pathlib import Path

pkl_path = Path(".../Left (bend 1 leg)/radar1.pkl")  # or ".../11-54-10-radar1.pkl"

with open(pkl_path, "rb") as f:
    obj = pickle.load(f)

print(type(obj))
# If obj is a dict-like:
if hasattr(obj, "keys"):
    print(obj.keys())
