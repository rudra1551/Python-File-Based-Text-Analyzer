import re
from collections import Counter

def Total_Char(text):
    Total_Character= len(text)
    print(f"\nTotal Characters ( With Spaces ) Are:    {Total_Character}")
    for i in text:
        if i==" ":
            Total_Character-=1
    print(f"Total Characters ( Without Spaces ) Are: {Total_Character}")

def Total_word(text):
    Total_Words= text.split()
    print(f"Total Number of Words Are:               {len(Total_Words)}")

def Total_Vowel(text):
    vowels="aeiou"
    count_vowels=0
    text_lower=text.lower()
    for i in text_lower:
        if i in vowels:
            count_vowels+=1
    print(f"Total Number Of vowels:                  {count_vowels}")

def Total_consonant(text):
    vowels="aeiou"
    count_consonants=0
    text_lower=text.lower()
    for i in text_lower:
        if i.isalpha() and i not in vowels:
            count_consonants+=1
    print(f"Total Number Of consonants:              {count_consonants}")

def Total_Uppercase(text):
    count_Upper=0
    for i in text:
        if i.isupper():
            count_Upper+=1
    print(f"Total Number Of Uppercase Letters:       {count_Upper}")

def Total_Lowercase(text):
    count_Lower=0
    for i in text:
        if i.islower():
            count_Lower+=1
    print(f"Total Number Of Lowercase Letters:       {count_Lower}")

def Frequency(text,number_words):
    words_list=re.findall(r"\b\w+\b",text.lower()) 
    frequency=Counter(words_list)
    if number_words==0:
        number_words=len(frequency)
    sort_frequency=frequency.most_common(number_words)
    longest_word=max(words_list,key=len)
    max_length=len(longest_word)+5
    print("\nWords"," "*len(longest_word)," "*2,"Frequency")
    print("--------------------------------")
    for i in sort_frequency:
        word=i[0]
        count=i[1]
        print(word," "*(max_length-len(word))," "*2,count)

def Sentences(text):
    count_sentence=1 
    for i in text:
        if i=="\n":
            count_sentence+=1
    print(f"Total Numbers of Sentences:              {count_sentence} ")

def main(text,number_words):
    Total_Char(text)
    Total_word(text)
    Total_Vowel(text)
    Total_consonant(text)
    Total_Uppercase(text)
    Total_Lowercase(text)
    Sentences(text)
    Frequency(text,number_words)
    
def File_Input():
    while True:   
        File=input("\nEnter File Path:").strip('"').strip("'")
        try:
            F=open(File,"r")
            text=F.read()
            F.close()
            break
        except FileNotFoundError:
            print("\nInvalid File Path, Enter a Valid File Path")
    
    while True:
        number_words=input("\nEnter how many number of common words you want OR press 0 for every word frequency: ").strip()
        if number_words.isdigit():
            number_words=int(number_words)
            main(text,number_words) 
            break
        else:
            print("\nInvalid Input, Enter Digits Only")


print("\nWelcome TO Text Analyzer:")

while True:
    File_Input()
    Choice=input("\nEnter Again to analyze another Text OR Enter Exit: ").strip().lower()
    if Choice!="again":
        break
    
print("\nThanks For Using Text Analyzer 🙏")
    
