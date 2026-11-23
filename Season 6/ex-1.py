def string_iteration(string1 , string2):
    return string1.count(string2)
#------------------------------------------------------------------------------
str1 = input("Enter first string:")
str2 = input("Enter second string:")

print("This is the number of times the subsequence one appears in the subsequence two:",string_iteration(str1 , str2))