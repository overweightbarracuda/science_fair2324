def relative_amount(file, character, block):
    num_file_occurences = 0
    total_file_lines = 0
    with open(file,encoding="utf8") as f:
        for line in f:
            total_file_lines += len(line)
            if character in line:
                num_file_occurences +=1
    total_block_lines = len(block)
    num_block_occurences = block.count(character)
    return(num_file_occurences/total_file_lines, num_block_occurences/total_block_lines)

print(relative_amount("text/replaced_digits/chinese_text_AA.txt", "风88888800000000000000000000000000000000000000000000000000000000000", "自_年_陈国富的工作重心逐渐转入两岸3地华语电影的整合与开创_年之后_他与中国第1民营电影公司华谊兄弟合作_在_年中监制了_集结号_、_风声_、_唐山大地震_、_狄仁杰_系列、_太极_系列、_画皮_、_1942_等_部影片_其中_部票房过亿_至_年底_陈国富监制电影的累计票房已达到了_亿人民币_"))
    
