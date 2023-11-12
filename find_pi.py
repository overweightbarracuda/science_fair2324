import pickle as pkl

PI = "一四"
def look_for(t, n):
    instances = []
    for c in len(t)-len(n):
        if t[c:c+len(n)] == n:
            instances.append((c, n))



for i in range(1,7):
    with open(f"data/{i}grams.pkl", "rb") as f:
        text = pkl.load(f)
        print("loaded "+f.name)
    