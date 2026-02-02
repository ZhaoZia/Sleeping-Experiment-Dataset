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
