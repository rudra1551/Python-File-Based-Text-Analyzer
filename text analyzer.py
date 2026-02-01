# File-Based Text Analyzer
# Built while learning Python through hands-on projects
# Analyzes text files and provides statistics such as
# character count, word count, and word frequency

import re
from collections import Counter

# Calculates total characters with and without spaces
def Total_Char(text):
    Total_Character= len(text)
    print(f"\nTotal Characters ( With Spaces ) Are:    {Total_Character}")
    for i in text:
        if i==" ":
            Total_Character-=1
    print(f"Total Characters ( Without Spaces ) Are: {Total_Character}")

# Counts total number of words in the text
def Total_word(text):
    Total_Words= text.split()
    print(f"Total Number of Words Are:               {len(Total_Words)}")

# Counts total vowels (case-insensitive)
def Total_Vowel(text):
    vowels="aeiou"
    count_vowels=0
    text_lower=text.lower()
    for i in text_lower:
        if i in vowels:
            count_vowels+=1
    print(f"Total Number Of vowels:                  {count_vowels}")

# Counts total consonants (alphabetic characters only)
def Total_consonant(text):
    vowels="aeiou"
    count_consonants=0
    text_lower=text.lower()
    for i in text_lower:
        if i.isalpha() and i not in vowels:
            count_consonants+=1
    print(f"Total Number Of consonants:              {count_consonants}")

# Counts uppercase letters in the text
def Total_Uppercase(text):
    count_Upper=0
    for i in text:
        if i.isupper():
            count_Upper+=1
    print(f"Total Number Of Uppercase Letters:       {count_Upper}")

# Counts lowercase letters in the text
def Total_Lowercase(text):
    count_Lower=0
    for i in text:
        if i.islower():
            count_Lower+=1
    print(f"Total Number Of Lowercase Letters:       {count_Lower}")

# Analyzes word frequency and displays the most common words
# User can choose how many top frequent words to display
def Frequency(text,number_words):
    words_list=re.findall(r"\b\w+\b",text.lower()) 
    frequency=Counter(words_list)
    if number_words==0:
        number_words=len(frequency)

# Sort words by frequency in descending order
    sort_frequency=frequency.most_common(number_words)
    longest_word=max(words_list,key=len)
    max_length=len(longest_word)+5
    print("\nWords"," "*len(longest_word)," "*2,"Frequency")
    print("--------------------------------")
    for i in sort_frequency:
        word=i[0]
        count=i[1]
        print(word," "*(max_length-len(word))," "*2,count)

# Estimates number of sentences based on line breaks
def Sentences(text):
    count_sentence=1 
    for i in text:
        if i=="\n":
            count_sentence+=1
    print(f"Total Numbers of Sentences:              {count_sentence} ")

# Executes all analysis functions in sequence
def main(text,number_words):
    Total_Char(text)
    Total_word(text)
    Total_Vowel(text)
    Total_consonant(text)
    Total_Uppercase(text)
    Total_Lowercase(text)
    Sentences(text)
    Frequency(text,number_words)
    
# Handles file input and validates user input for analysis options
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

# Program entry point
while True:
    File_Input()
    Choice=input("\nEnter Again to analyze another Text OR Enter Exit: ").strip().lower()
    if Choice!="again":
        break
    
print("\nThanks For Using Text Analyzer 🙏")
    

