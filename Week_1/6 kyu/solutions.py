'''These are Blackbox AI's solutions to 4 katas of 6 kyu difficulty'''
def difference(a, b):
    """
    Kata link: https://www.codewars.com/kata/523f5d21c841566fde000009/train/python
    """
    return [val for val in a if val not in b]
def duplicate_count(text):
    """
    Kata link: https://www.codewars.com/kata/54bf1c2cd5b56cc47f0007a1/train/python
    """
    # Convert the string to lowercase and create a set of characters
    unique_chars = set(text.lower())
    
    # Initialize a count variable to 0
    count = 0
    
    # Iterate over each character in the set of unique characters
    for char in unique_chars:
        # If the character occurs more than once in the input string
        if text.lower().count(char) > 1:
            # Increment the count variable
            count += 1
            
    # Return the count variable
    return count
def convert_string(input_string):
  """
  Kata link: https://www.codewars.com/kata/54b42f9314d9229fd6000d9c/train/python
  """
    # Create an empty dictionary to store the count of each character
    char_count = {}

    # Iterate through each character in the input string
    for char in input_string:
        # Convert the character to lowercase and add it to the dictionary
        # If the character is not already in the dictionary, add it with a count of 1
        # If the character is already in the dictionary, increment its count
        char_count[char.lower()] = char_count.get(char.lower(), 0) + 1

    # Create an empty string to store the output
    output_string = ""

    # Iterate through each character in the input string again
    for char in input_string:
        # Convert the character to lowercase and add it to the output string
        # If the character appears only once, add "(" to the output string
        # If the character appears more than once, add ")" to the output string
        if char_count[char.lower()] == 1:
            output_string += "("
        else:
            output_string += ")"

    # Return the output string
    return output_string
def find_uniq(arr):
  """
  Kata link: https://www.codewars.com/kata/585d7d5adb20cf33cb000235/train/python
  """
    # Sort the array
    sorted_arr = sorted(arr)
    # Check if the first two elements are equal
    if sorted_arr[0] != sorted_arr[1]:
        return sorted_arr[0]
    else:
        # If the first two elements are equal, check if the last element is different
        if sorted_arr[-1] != sorted_arr[0]:
            return sorted_arr[-1]
        else:
            # If all elements are equal, return any element
            return sorted_arr[0]
