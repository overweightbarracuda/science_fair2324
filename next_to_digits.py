import pickle as pkl
import glob
import tqdm
import gzip
import re


def find_chunks(file):
    with open(file, "rt", encoding="utf-8") as f:
        text = f.readlines()
    # regex = re.compile("(\d\D[0,5])[0,5]")
    # matches = re.findall(regex, text)
    matches = []
    for i in range(len(text)):
        line = text[i]
        c = 0
        for character in line:
            if character in "1234567890":
                c += 1
        matches.append((c, i))
    matches.sort(reverse=True)

    for i in range(5):
        print(matches[i][0], text[matches[i][1]])

def find_dates(file):
    with open(file, "rt", encoding="utf-8") as f:
        text = f.read()
    regex = re.compile("\d{4}(?:\D{0,3}\d){2,4}")
    matches = re.findall(regex, text)
    print(matches)
digits = "〇一二三四五六七八九"
with open("data/2grams.pkl", "rb") as f:
    grams_2 = pkl.load(f)
with open("data/1grams.pkl", "rb") as f:
    grams_1 = pkl.load(f)

next_frequency = {}
ratios = []

for gram in grams_2:
    if gram[0] in digits:
        if gram[1] in next_frequency:
            next_frequency[gram[1]] += grams_2[gram]
        else:
            next_frequency[gram[1]] = grams_2[gram]
    elif gram[1] in digits:
        if gram[0] in next_frequency:
            next_frequency[gram[0]] += grams_2[gram]
        else:
            next_frequency[gram[0]] = grams_2[gram]

for freq in next_frequency:
    freq1 = grams_1[freq]
    freq2 = next_frequency[freq]
    if freq1 < 50:
        continue
    ratios.append(((freq1/freq2), freq1, freq2, freq))
ratios.sort()
print(ratios[:10])

# find_dates("text/replaced_digits/chinese_text_AA.txt")