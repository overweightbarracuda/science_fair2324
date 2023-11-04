import re
def match(text, sep, p):
    k=p-1
    #t = [[0,1],[2,1],[0,3],[4,1],[0,5]]
    t= []
    for i in range(0,2*k+1):
        if i%2 == 1:
            t.append([i+1,1])
        else:
            t.append([0,i+1])
    print(t)
    state = 0
    for i in range(0,len(text)):
        if text[i]==sep:
            j = 0
        else:
            j = 1
        state = t[state][j]
        if state ==(2*k+1):
            print(text[i-2*k:i+1])
            state = 2*k-1
#match("asdask_d_jaklfjklasklfjaklsjflkasjfklaa_b_c_d_a", "_")

def find_strings_with_separator(text, n, ignore=["\n", "\u3000", "\xa0", "\u200b", "·"]):
    found_strings = []
    for i in range(0,len(text)-2*n+1):
        force = False
        for j in range(0,n-1):
            if text[i+1] != text[i+2*j+3]:
                force = True
                break
        if force == True:
            continue
        else:
            found_strings.append(text[i:i+2*n])
    return found_strings

print(find_strings_with_separator("asdask/d/j/aklfjklasklfjaklsjflkasjfklaa_b_c_d_a_",6))



# for match in matches:
#     if any([character in match for character in ignore]):
#         continue
#     found_strings.append(match)

# return found_strings
# pattern = re.compile(r".(.).\1.\1")
# matches = []
# for match in re.finditer(pattern, "asdask/d/j/aklfjklasklfjaklsjflkasjfklaa_b_c_d_a_"):
#         matches.append(match.group(0))
# print(matches)
#print(find_strings_with_separator("_", 3, "asdask_d_jaklfjklasklfjaklsjflkasjfklaa_b_c_d_a"))
