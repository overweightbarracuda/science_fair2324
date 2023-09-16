# %%
import re, glob

def remove_latin(text):
    return re.sub(r"[（），。？！《》A-Za-z0-9\(\){}\[\]\?\!\._+|\\,`~\-=/<>%$#@*^:;]+", "_", text)
t = remove_latin("as dfn 128 _\n91():!!-=-%")
print(t)

# %%
for file_name in sorted(glob.glob("text/*/wiki*")):
    result = []
    with open(file_name, encoding="utf-8") as f:
        for line in f.readlines():
            if line.startswith("<doc") or line.startswith("</doc"):
                result.append("")
            else:
                result.append(remove_latin(line))
    with open(file_name.replace("text","text/cleaned"), "w", encoding="utf-8") as f:
        f.write("\n".join(result))
    print(file_name)
#%%
text = ""
for file_name in sorted(glob.glob("text/cleaned/*/wiki*")):
    with open(file_name, encoding="utf-8") as f:
        text += f.read()
print("read",len(text),"characters")
# %%
ignore = ["\n", " ", "_", "：", "、", "\u3000", "\xa0", "\u200b"]
frequency = dict()
for i in range(len(text)-1):
    seq = text[i:i+2]
    if any([character in seq for character in ignore]) or seq[0] == seq[1]:
        continue
    if seq not in frequency:
        frequency[seq] = 1
    else:
        frequency[seq] += 1
# [frequency.pop(character) for character in ignore]
frequency_sorted = sorted(list(zip(list(frequency.values()), zip(list(frequency.keys())))), reverse=True)
print(frequency_sorted[:30])
# %%
reverses = []
for key in frequency:
    if key[::-1] in frequency and key[::-1]:
        reverses.append((min(frequency[key], frequency[key[::-1]]), key))
reverses_sorted = sorted(reverses, reverse=True)
print(reverses_sorted[:30])
# %%
