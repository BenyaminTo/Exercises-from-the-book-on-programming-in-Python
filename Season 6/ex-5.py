def sort(english_words_dict):
    sorted_dict = dict(sorted(english_words_dict.items()))
    print("The sorted dictionary is:", sorted_dict)
#------------------------------------------------------------------------------
def insert(english_words_dict):
    word = input("Enter your word:")
    english_words_dict[word] = input("Enter meaning:")
#------------------------------------------------------------------------------
def update(english_words_dict):
    dic = {input("Enter your word:"):input("Enter meaning:")}
    english_words_dict.update(dic)
#------------------------------------------------------------------------------
def remove(english_words_dict, key):
    if key in english_words_dict:
        english_words_dict.pop(key)
    else:
        print("This key isn't exist!")
#------------------------------------------------------------------------------
def display():
    print(english_words_dict)
#------------------------------------------------------------------------------
def menu(item):
    if item == 1:
        sort(english_words_dict)
    elif item == 2:
        insert(english_words_dict)
    elif item == 3:
        update(english_words_dict)
    elif item == 4:
        key = input("Enter a key for remove:")
        remove(english_words_dict, key)
    elif item == 5:
        display()
    else:
        print("This item isn't exist!")
#------------------------------------------------------------------------------
english_words_dict = {
    "apple": "پیاز",
    "banana": "نارنگ",
    "cherry": "مکعه",
    "date": "سنگ",
    "elderberry": "بله بلوط",
    "fig": "گندم",
    "grape": "باز",
    "honeydew": "دونه مالک",
    "kiwi": "کویی",
    "lemon": "نارنج",
    "mango": "مانو",
    "nectarine": "نکاتری",
    "orange": "نارنج",
    "papaya": "پیپیا",
    "peach": "موز",
    "pineapple": "نارنجی",
    "plum": "بلوط",
    "quince": "گیاهان قرنی",
    "raspberry": "توت فرنگی",
    "strawberry": "کیش",
    "tangerine": "نارنجیه",
    "ugli": "نارنجیه تازه",
    "watermelon": "بادمجان",
    "xigua": "سیاه کوبه",
    "yellow passion fruit": "نارنج پرتقالی زرد",
    "zucchini": "بازیکن"
}
print("Select an item:")
print("0.end")
print("1.sort")
print("2.insert")
print("3.update")
print("4.remove")
print("5.display")
while(True):
    item = int(input("Enter a item:"))
    if item == 0:
        break
    menu(item)
