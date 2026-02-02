import pickle
from pathlib import Path

pkl_path = Path(".../Left (bend 1 leg)/radar1.pkl")  # or ".../11-54-10-radar1.pkl"

with open(pkl_path, "rb") as f:
    obj = pickle.load(f)

print(type(obj))
# If obj is a dict-like:
if hasattr(obj, "keys"):
    print(obj.keys())