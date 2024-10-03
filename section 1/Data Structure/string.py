# Function to find the longest word in a string
# Time Complexity: O(n), Space Complexity: O(n) for storing the longest word
def findlongest(s):
    max_len = 0
    curr_word = ''
    largest_word = ''

    for char in s + '':  # Loop through each character in the string
        if char != ' ':
            curr_word += char  # Build the current word
        else:
            if len(curr_word) > max_len:  # Check if the current word is longer than the max found
                max_len = len(curr_word)
                largest_word = curr_word  # Update largest word
            curr_word = ''  # Reset for the next word

    return largest_word

# Example usage:
# s = "I love programming in Pythonsdfghjdfghj"
# longest = findlongest(s)
# print("Longest word:", longest)  # Output: "Pythonsdfghjdfghj"


# Function to find the first non-repeating character in a string
# Time Complexity: O(n), Space Complexity: O(n) for storing character counts
def first_non_repeat(s):
    chr_cnt = {}

    for char in s:
        if char in chr_cnt:
            chr_cnt[char] += 1
        else:
            chr_cnt[char] = 1

    for x in chr_cnt:  # Check the character counts
        if chr_cnt[x] == 1:
            return x  # Return the first non-repeating character
        
    return None  # Return None if no non-repeating character is found

# Example usage:
# print(first_non_repeat("sinans"))  # Output: "i"


# Function to check if a string is a palindrome
# Time Complexity: O(n), Space Complexity: O(n) for storing the filtered string
def is_palindrome(s):
    si = ''.join(x.lower() for x in s if x.isalpha())  # Filter and lower the string
    return si == si[::-1]  # Check if the string is equal to its reverse

# Example usage:
# print(is_palindrome("A man, a plan, a canal, Panama"))  # Output: True


# Function to compress a string using run-length encoding
# Time Complexity: O(n), Space Complexity: O(n) for the compressed string
def comp(s):
    if not s:
        return ''
    
    compress = []
    cnt = 1

    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            cnt += 1  # Count consecutive characters
        else:
            compress.append(s[i - 1] + str(cnt))  # Append the character and its count
            cnt = 1
    compress.append(s[-1] + str(cnt))  # Append the last character and its count
    return ''.join(compress)

# Example usage:
# print(comp('aaabbacc'))  # Output: "a3b2a1c2"


# Function to convert a string to title case (capitalize first letter of each word)
# Time Complexity: O(n), Space Complexity: O(n) for the new string
def to_titles(s):
    new_str = ''
    capitalize_next = True  # Flag to check if the next character should be capitalized

    for char in s:
        if char == ' ':
            new_str += char
            capitalize_next = True  # Set flag to capitalize next character
        else:
            if capitalize_next and 'a' <= char <= 'z':
                new_str += chr(ord(char) - 32)  # Capitalize the character
            elif not capitalize_next and 'A' <= char <= 'Z':
                new_str += chr(ord(char) + 32)  # Lowercase the character
            else:
                new_str += char
            capitalize_next = False  # Reset flag after processing a character

    return new_str

# Example usage:
# print(to_titles('sfdsf sffsf sfew we fr grg erggg rg gw'))


# Function to check if a string is a palindrome using two-pointer technique
# Time Complexity: O(n), Space Complexity: O(1)
def is_palindromes(s):
    i = 0
    j = len(s) - 1

    while i < j:
        if s[i] != s[j]:
            return False  # If characters don't match, it's not a palindrome
        i += 1
        j -= 1

    return True  # If all characters match, it is a palindrome

# Example usage:
# print(is_palindromes('asdfghjkkjhgfdsa'))  # Output: False


# Function to find the longest word in a string (alternative implementation)
# Time Complexity: O(n), Space Complexity: O(n) for storing the longest word
def logest_word(s):
    curr_word = ''
    max_word = ''

    for char in s + '':  # Loop through each character
        if char != ' ':
            curr_word += char  # Build the current word
        else:
            if len(curr_word) > len(max_word):  # Check if the current word is longer than the max found
                max_word = curr_word  # Update max word
            curr_word = ''  # Reset for the next word

    return max_word

# Example usage:
# print(logest_word('asdfg ghjk asdfghjkl asdjkladghjk'))  # Output: "asdfghjkl"


# Function to find the longest word in a string (alternative implementation with typo fixed)
# Time Complexity: O(n), Space Complexity: O(n) for storing the longest word
def titl(s):
    new_str = ''
    capitalize_next = True

    for char in s:
        if char == ' ':
            new_str += char
            capitalize_next = True  # Set flag to capitalize next character
        else:
            if capitalize_next and 'a' <= char <= 'z':
                new_str += chr(ord(char) - 32)  # Capitalize the character
            elif not capitalize_next and "A" <= char <= 'Z':
                new_str += chr(ord(char) + 32)  # Lowercase the character
            else:
                new_str += char
            capitalize_next = False  # Reset flag after processing a character

    return new_str

# Example usage:
print(titl('sdf fgh hgf bh njuy jg v'))  # Output: "Sdf Fgh Hgf Bh Njuy Jg V"
