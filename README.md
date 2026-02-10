# Sleeping-Experiment-Dataset
The Sleeping Experiment Dataset, which contains 99 individual sample data

# (Dataset Name) Radar Sleep Posture Dataset (99 Subjects)

This dataset combines two subsets into a single release:
- **Cohort_1** (68 subjects)
- **Cohort_2** (31 subjects)

Each subject contains multiple recording parts/sessions. For each part/session, data are organized by **sleep posture**, and each posture contains **8 radar channels** saved as `.pkl` files.

---

## 1. Directory Structure

### 1.1 Dataset Root

```text
<DATASET_ROOT>/
├─ Cohort_1/
│  ├─ 1/
│  ├─ 2/
│  ├─ ...
│  └─ 68/
└─ Cohort_2/
   ├─ 1/
   ├─ 2/
   ├─ ...
   └─ 31/
```
### 1.2 Cohort_1 subset structure (example: subject `1`)

```text
Cohort_1/1/
├─ B1/ # Blanket id
│ ├─ L0/
│ │ ├─ radar1.pkl
│ │ ├─ radar_map1.png
│ │ ├─ radar_map1.npy
| | ├─ radar2.pkl
│ │ ├─ radar_map2.png
│ │ ├─ radar_map2.npy
│ │ ├─ ...
│ │ ├─ radar8.pkl
│ │ ├─ radar_map8.png
│ │ ├─ radar_map8.npy
│ │ ├─ radar_map_all.npy
│ │ ├─ radar_map_all.png
│ │ ├─ depth1.npz
│ │ └─ depth1.png
│ ├─ L1/
│ ├─ ...
│ └─ SU/
├─ B2/
└─ B3/
```
### 1.3 31-subject subset structure (example: subject `1`)

```text
30_SUBJECT_FULL_DATASET/1/
├─ B0/ # Blanket id
│ ├─ L0/
│ │ ├─ radar1.pkl
│ │ ├─ radar_map1.png
│ │ ├─ radar_map1.npy
| | ├─ radar2.pkl
│ │ ├─ radar_map2.png
│ │ ├─ radar_map2.npy
│ │ ├─ ...
│ │ ├─ radar8.pkl
│ │ ├─ radar_map8.png
│ │ ├─ radar_map8.npy
│ │ ├─ radar_map_all.npy
│ │ ├─ radar_map_all.png
│ │ ├─ depth1.npz
│ │ └─ depth1.png
│ ├─ L1/
│ ├─ ...
│ └─ SU/
├─ B1/
├─ B2/
└─ B3/
```


---

## 2. Posture Categories

Each part/session contains the following posture folders:

    1. "Mid Fowler": "MF"
    2. "Supine": "SU"
    3. "Left (straight)": "L0"
    4. "Left (bend 1 leg)": "L1"
    5. "Left (bend both legs)": "L2"
    6. "Right (straight)": "R0"
    7. "Right (bend 1 leg)": "R1"
    8. "Right (bend both legs)": "R2"
    9. "Prone (head to left)": "PL"
    10. "Prone (head to right)": "PR"

---


## 3. Loading Examples

### 3.1 Load `.pkl` in Python
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
```


## 5. Citation / Acknowledgement

## 6. License

## 7. Contact
