# %%
import re, tqdm, glob
all_matches = []
for file in tqdm.tqdm(glob.glob("text/replaced_digits/chinese_text_*.txt")):
    with open(file, encoding="utf-8") as f:
        # all_matches.extend(re.findall("\B\d\D{1,3}\d\D{1,3}\d\B", f.read()))
        all_matches.extend(re.findall("\d百\d十\d", f.read()))
print(all_matches[:10])


# %%
for match in all_matches:
    digits = [int(s) for s in re.findall("\d", match)]
    if digits[0] + digits[1] == digits[2]:
        print(match)
# %%
