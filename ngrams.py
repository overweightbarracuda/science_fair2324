# %%
import re, glob
from tqdm import tqdm
import gzip
from itertools import permutations
import pickle as pkl

maxn = 6
filename = ""

def save_text_as_gzip(text, filename):
    with gzip.open(filename, 'wt', encoding='utf-8') as file:
        file.write(text)
def load_text_from_gzip(filename):
    with gzip.open(filename, 'rt', encoding='utf-8') as file:
        text = file.read()
    return text

def remove_latin(text):
    return re.sub(r"[（），。？！《》A-Za-z0-9\(\){}\[\]\?\!\._+|\\,`~\-=/<>%$#@*^:;]+", "_", text)
t = remove_latin("as dfn 128 _\n91():!!-=-%")

# %%
# for file_name in sorted(glob.glob("text/*/wiki*")):
#     result = []
#     with open(file_name, encoding="utf-8") as f:
#         for line in f.readlines():
#             if line.startswith("<doc") or line.startswith("</doc"):
#                 result.append("")
#             else:
#                 result.append(remove_latin(line))
#     with open(file_name.replace("text","text/cleaned"), "w", encoding="utf-8") as f:
#         f.write("\n".join(result))
#     print(file_name)
#%%
# text = ""
# for file_name in sorted(glob.glob("text/cleaned/*/wiki*")):
#     with open(file_name, encoding="utf-8") as f:
#         text += f.read()
# save_text_as_gzip(text, "chinese_text.txt.gz")
# print("read",len(text),"characters")
#%%
#text = load_text_from_gzip("chinese_text.txt.gz")
# %%
import glob
def dict_frequency(dictionary, top = 30):
    frequency_sorted = sorted(list(zip(list(dictionary.values()), zip(list(dictionary.keys())))), reverse=True)
    return(frequency_sorted[:top])
def ngrams(n, ignore = ["\n", " ", "_", "：", "、", "\u3000", "\xa0", "\u200b", "·"]):
    filenames = glob.glob("text/chinese_text_*.gz")
    frequency = dict()
    filenames.sort()
    for file in filenames:
        print(file)
        text = load_text_from_gzip(file)
        for i in tqdm(range(len(text)-1)):
            seq = text[i:i+n]
            if any([character in seq for character in ignore]) or len(set(seq)) != n:
                continue
            if seq not in frequency:
                frequency[seq] = 1
            else:
                frequency[seq] += 1
    return frequency
    # [frequency.pop(character) for character in ignore]
# %%
for n in range(1,maxn+1):
    print("n is: ",n)
    frequency = ngrams(n)
    with open("data/"+str(n) +"grams.pkl", "wb") as f:
        pkl.dump(frequency, f)
    frequency = []