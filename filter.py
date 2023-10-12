# %%
import re, glob
from tqdm import tqdm
import gzip
from itertools import permutations

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
print(t)

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
    filenames = glob.glob("text/*.gz")
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
frequency = ngrams(3)
# %%
def get_permutations(input_string):
    # Use permutations to generate all possible permutations of the input string
    perms = permutations(input_string)

    # Convert each permutation tuple to a string and store in a list
    perm_list = [''.join(p) for p in perms]

    return list(set(perm_list))
get_permutations("aa")
# %%
print("found", len(frequency), "ngrams")
def common_reverse(frequency, min_frequency = 30):
    reverses = []
    for key in frequency:
        if frequency[key] >= min_frequency:
            reverse_key = key[::-1]
            if reverse_key in frequency and reverse_key<key and frequency[reverse_key]>=min_frequency:
                reverses.append((min(frequency[key], frequency[reverse_key]), key))
    reverses_sorted = sorted(reverses, reverse=True)
    return(reverses_sorted)
#%%
def common_perms(frequency, min_frequency = 30):
    permutations = []
    for key in frequency:
        if frequency[key] >= min_frequency:
            key_permutations = get_permutations(key)
            min_count = 100000000
            for permutation in key_permutations:
                if permutation not in frequency or permutation>key or frequency[permutation]<min_frequency:
                    min_count = 0
                    break
                else:
                    min_count = min(min_count,frequency[permutation])
            if min_count>=min_frequency:
                permutations.append((min_count, key))
    sorted_perms = sorted(permutations, reverse = True)
    return sorted_perms

# %%
perms = common_perms(frequency, 1)
print("found", len(perms), "reverses")

chars = dict()

for count,perm in perms:
    for char in perm:
        if char not in chars:
            chars[char] = 1
        else:
            chars[char] += 1


# %%
