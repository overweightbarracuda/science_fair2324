#%%
import pickle as pkl
from tqdm import tqdm

i = 8
with open(f"data/{i}seps.pkl", "rb") as f:
    freq = pkl.load(f)
    print("Loaded file")

with open(f"data/{i//2}seps.pkl", "rb") as f:
    half_freq = pkl.load(f)
    print("Loaded file")


#%%
results = []
for key in tqdm(freq):
    if freq[key] < 1:
        continue
    else:
        odds = key[::2]
        evens = key[1::2]
        print(odds,evens)
        score = min(half_freq.get(odds, 0), half_freq.get(evens, 0))
        if score > 0:
            results.append((freq[key], half_freq.get(odds,0), half_freq.get(evens, 0), key))

results.sort(reverse=True)
print(results)
# %%
freq
# %%
half_freq
# %%
