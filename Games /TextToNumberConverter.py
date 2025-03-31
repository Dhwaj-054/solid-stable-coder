Text to Number converter game

def text_to_numbers(text):
    # Dictionary to map number words to their numeric values
    number_words = {
        "zero": 0, "one": 1, "two": 2, "three": 3, "four": 4,
        "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9,
        "ten": 10, "eleven": 11, "twelve": 12, "thirteen": 13, "fourteen": 14,
        "fifteen": 15, "sixteen": 16, "seventeen": 17, "eighteen": 18, "nineteen": 19,
        "twenty": 20, "thirty": 30, "forty": 40, "fifty": 50, "sixty": 60,
        "seventy": 70, "eighty": 80, "ninety": 90T
    }
    
    words = text.lower().split()  # Convert text to lowercase and split into words
    numbers = []
    
    for word in words:
        if word in number_words:
            numbers.append(str(number_words[word]))
        else:
            numbers.append(f"[Unknown: {word}]")  # Handle unknown words gracefully
    
    return " ".join(numbers)

if __name__ == "__main__":
    print("Welcome to the Text-to-Number Converter!")
    user_input = input("Enter a sentence with numbers as words (e.g., 'five apples and three oranges'): ")
    result = text_to_numbers(user_input)
    print(f"Converted: {result}")

#Output:

#Welcome to the Text-to-Number Converter!
#Enter a sentence with numbers as words (e.g., 'five apples and three oranges'): Twenty nine
#Converted: 20 9
