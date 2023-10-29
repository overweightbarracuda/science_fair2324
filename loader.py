#%%
import pickle as pkl
from tqdm import tqdm

i = 6
with open(f"data/{i}seps.pkl", "rb") as f:
    freq = pkl.load(f)
    print("Loaded file")

with open(f"data/{i//2}seps.pkl", "rb") as f:
    half_freq = pkl.load(f)
    print("Loaded file")


#%%
results = []
for key in tqdm(freq):
    if freq[key] < 1000:
        continue
    else:
        odds = key[::2]
        evens = key[1::2]
        score = min(half_freq.get(odds, 0), half_freq.get(evens, 0))
        if score > 0:
            results.append((score, key))

results.sort(reverse=True)
print(results[:100])
# %%
freq
# %%
half_freq
# %%
