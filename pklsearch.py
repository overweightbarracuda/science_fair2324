import pickle as pkl

with open("data/1grams.pkl", "rb") as f:
    freq = pkl.load(f)

print(freq["従"])
