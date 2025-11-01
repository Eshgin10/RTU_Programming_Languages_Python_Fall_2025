"""
Task 3 – Function with Combined Logic
------------------------------------
Write a function `analyze_sentence(text)` that returns:
1. total character count (len)
2. word count (split)
3. whether it contains the word "Python" (case-insensitive)
Return results as a tuple and print summary in main.
"""

def analyze_sentence(text):
    char_count = len(text)
    word_count = len(text.split())
    check_python = "python" in text.lower()

    return char_count, word_count, check_python

sentence = input("Enter a sentence: ")
result = analyze_sentence(sentence)

char_count, word_count, check_python = result

print(f"Character count is: {char_count}")
print(f"Word Count is: {word_count}")
print(f"Check Python: {check_python}")