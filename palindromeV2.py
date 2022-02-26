#Looking for palindrome

def is_palindrome(string: str) -> bool:
    string = string.replace(' ','').lower()  #Deleting spaces in char string, and tranform in lower case
    return string == string[::-1]

def run():
    word = input('Write a word or phrase ')
    print(is_palindrome(word))

if __name__ == '__main__':
    run()


#mypy palindromeV2.py --check-untyped-defs <- in console, show if we have file error and it's line