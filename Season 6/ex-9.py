def NumChar(string):
    char = []
    for ch in string:
        if ch not in char:
            char.append(ch)
    
    char_dic = dict()
    for ch in char:
        char_dic[ch] = 0
        
    for ch in string:
        if ch in char_dic.keys():
            char_dic[ch] += 1
        else:
            continue
        
    return char_dic

#------------------------------------------------------------------------------
string = ""
while True:
    line = input("Enter text (enter a line ending with a dot to finish): ")
    if line.endswith('.'):
        string += line
        break
    string += line + " "
    
print("Number of characters:", NumChar(string))