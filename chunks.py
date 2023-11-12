import pickle as pkl
import glob
import tqdm
import gzip

digits = "一二三四五六七八九"

def save_text_as_gzip(text, filename):
    with gzip.open(filename, 'wt', encoding='utf-8') as file:
        file.write(text)
def load_text_from_gzip(filename):
    with gzip.open(filename, 'rt', encoding='utf-8') as file:
        text = file.read()
    return text

def replace_digits(text:str):
    replaced = text
    for i in range(9):
        replaced = replaced.replace(digits[i], str(i+1))
    return replaced

print(replace_digits("三一四一"))

for file in tqdm.tqdm(sorted(glob.glob("text/chinese_text_AA*.gz"))):
    text = load_text_from_gzip(file)
    print(file)
    new_text = replace_digits(text)
    with open("text/replaced_digits/AA.txt", "wt", encoding='utf-8') as f:
        f.write(new_text)
    
