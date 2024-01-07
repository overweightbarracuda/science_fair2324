def grep_function(file, character):
    num_occurences = 0
    text_size = 0
    with open(file,encoding="utf8") as f:
        for line in f:
            if character in line:
                print(line)
                num_occurences +=1
                text_size += len(line)
    return(num_occurences,text_size)
print(grep_function("text/replaced_digits/chinese_text_AA.txt", "1942"))