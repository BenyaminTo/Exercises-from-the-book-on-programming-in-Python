def word_m_iter(string , m):
    words = ()
    words = string.split()
    resaults = list()
    for w in words:
        if len(w) == m:
            resaults.append(w)
    return resaults
#------------------------------------------------------------------------------
string = input("Enter your string:")
m = int(input("Enter a number:"))

resault = word_m_iter(string , m)
print(f"Words whose count is equal to {m} size: ", resault)
