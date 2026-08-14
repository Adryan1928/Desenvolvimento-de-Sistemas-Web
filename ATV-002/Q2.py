vowels = ["A", "E", "I", "O", "U"]

def analyze_string(string):
    count_of_vowels = 0
    for char in string:
        if char.upper() in vowels:
            count_of_vowels += 1

    reverse_string = string[::-1]

    palindrome_check = string.lower() == reverse_string.lower()
    
    return {
        'count_of_vowels': count_of_vowels,
        'reverse_string': reverse_string,
        'is_palindrome': palindrome_check
    }

string = input("Enter a string: ")
print(analyze_string(string))