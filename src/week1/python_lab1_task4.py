"""
Task 4 – Text-based Arithmetic Analyzer
--------------------------------------
Create a text-based analyzer that:
1. Counts non-space characters.
2. Counts words.
3. Extracts numbers and computes their sum and average.
Use helper functions:
- count_characters(text)
- count_words(text)
- extract_numbers(text)
- analyze_text(text)
Print formatted summary in main.
"""

def count_characters(text):
    """Count non-space characters in a string."""
    return len(text.replace(" ", ""))

def count_words(text):
    """Count number of words in a string."""
    return len(text.split())

def extract_numbers(text):
    """Return list of integers found in text."""
    numbers = []
    for word in text.split():
        if word.isdigit():  # Check if the word is an integer
            numbers.append(int(word))
    return numbers

def analyze_text(text):
    """Perform text-based arithmetic analysis."""
    char_count = count_characters(text)
    word_count = count_words(text)
    nums = extract_numbers(text)

    total = sum(nums) if nums else 0
    average = total / len(nums) if nums else 0

    return char_count, word_count, nums, total, average

if __name__ == "__main__":
    sentence = input("Enter a sentence with some numbers: ")
    char_count, word_count, nums, total, average = analyze_text(sentence)

    print(f"\nAnalysis Results:")
    print(f"Non-Space Characters: {char_count}")
    print(f"Word Count: {word_count}")
    print(f"Numbers Found: {nums}")
    print(f"Sum of Numbers: {total}")
    print(f"Average of Numbers: {average:.2f}")