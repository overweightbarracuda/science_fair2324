from grep_function import grep_all
import glob
import pickle as pkl


with open(f"data/1grams.pkl", "rb") as f:
    freq = pkl.load(f)
    print("Loaded file")

total_length = 0
for c in freq:
    total_length += freq[c]


def relative_amount(character, block):
    try:
        total_freq = freq[character]/total_length
    except:
        total_freq = 1
    total_block_lines = len(block)
    num_block_occurences = block.count(character)
    block_freq = num_block_occurences/total_block_lines
    return(block_freq/total_freq, total_freq, block_freq)

print(relative_amount("风", "自_年_陈国富的工作重心逐渐转入两岸3地华语电影的整合与开创_年之后_他与中国第1民营电影公司华谊兄弟合作_在_年中监制了_集结号_、_风声_、_唐山大地震_、_狄仁杰_系列、_太极_系列、_画皮_、_1942_等_部影片_其中_部票房过亿_至_年底_陈国富监制电影的累计票房已达到了_亿人民币_"))

a = grep_all("1942")
grepped_text = "".join(a[2])





relative_freq = {}

for c in grepped_text:
    if c not in relative_freq:
        relative_freq[c] = relative_amount(c, grepped_text)

rels =  sorted(list(zip(list(relative_freq.values()), zip(list(relative_freq.keys())))), reverse=True)

print(rels)

