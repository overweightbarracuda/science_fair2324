import glob

def grep_function(file, character):
    lines = []
    num_occurences = 0
    text_size = 0
    with open(file,encoding="utf8") as f:
        for line in f:
            if character in line:
                lines.append(line)
                num_occurences +=1
                text_size += len(line)
    return(num_occurences, text_size, lines)
# print(grep_function("text/replaced_digits/chinese_text_AA.txt", "1942"))



def grep_all(t):
    all_grep = (0, 0, [])
    for file in glob.glob("text/replaced_digits/chinese_text_*.txt"):
        grep = grep_function(file, t)
        all_grep = (all_grep[0] + grep[0], all_grep[1] + grep[1], all_grep[2].__add__(grep[2]))
        # print(all_grep[0], all_grep[1])
        # print(file)
    return all_grep

