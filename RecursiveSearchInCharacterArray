# https://github.com/ilukgolf/STD-CS350-Data_Structures-Lab1_RecursiveSearchInCharacterArray
# Lab 1: Recursive Search In Character Array
# Student: Jirawat Bunmaraksasakul
# ID: 1630708046

# Data set to search from
# Note: Some strings intentionally contain lowercase characters (e.g., 'q', 'm', 'u', 'h') for testing recursive search functions.
data = [
    "QWERTYUIOPASDFGHJKLZXCVBNM",
    "ASDFGHJKLZXCVBNMqWERTYUIOP",
    "ZXCVBNMASDFGHJKLZWERTYUIOP",
    "POIUYTREWQLKJHGFDSAmNBVCXZ",
    "MNBVCXZLKJHGFDSAPOIUYTREWQ",
    "LKJHGFDSAZXCVBNMqPOIUYTREW",
    "ASDFGHJKLZXCVBNMWERTYuIOP",
    "QWERTYUIOPASDFGHJKLZXCVBNM",
    "ZXCVBNMASDFGHJKLZWERTYUIOP",
    "POIUYTREWQLKJHGFDSAZXCVBNM",
    "MNBVCXZLKJhGFDSAPOIUYTREWQ",
    "QWERTYUIOPASDFGHJKLZXCVBNM"
]

# Other data sets for additional testing
# Note: Some strings intentionally contain lowercase characters for testing recursive search functions.
#       This data set has 10 rows and 30 columns and contains lowercase 53 characters.
#       Created test data using PWGen - Password Tech (https://pwgen-win.sourceforge.io/)
data2 = [
    "cBHDZSnWYZnRIQLAJPVTmVTVEBoQCa",
    "CXrFxzUUCRdVATONPMpKGYXBVOXgVe",
    "VAQbSFZMOTzoDIXTQTTNJDYoLAAeZC",
    "OVMUNALTUOOBbAROZUTCChECFUmWVU",
    "QqZTQSAOEZWHIENGJSsKOYCEATNMhV",
    "ZYTjGiPKVKHClDTJnGNWpsVAZVRBHz",
    "IPRxDHNrIALUuPJAFAOATWJnMZkQDC",
    "NdIGvAZNCeFUKVCIgXMHXDCXOjqYYE",
    "JzXQMCIKFjYNZWIPCIEVCLMpQEWPBW",
    "dVKlBEPLwYIRmVzUgJJRBLGESHUcWi"
]

# 1 Count the lowercase characters in data using recursive function
"""
    Recursively counts lowercase characters in a 2D character array.

    Args:
        data (list of str): The character array to search.
        row (int, optional): The current row index. Defaults to 0.
        col (int, optional): The current column index. Defaults to 0.

    Returns:
        int: The total number of lowercase characters found.
"""
def count_lowercase_recursive(data, row=0, col=0):
    # Base case: If we have processed all rows
    if row >= len(data):
        return 0
    # If we have processed all columns in the current row, move to the next row
    if col >= len(data[row]):
        return count_lowercase_recursive(data, row + 1, 0)
    # Check if the current character is lowercase
    count = 1 if data[row][col].islower() else 0
    # Recur for the next character in the same row
    return count + count_lowercase_recursive(data, row, col + 1)

# 2  Find the lines with the lowercase characters using recursive function
"""
    Recursively finds the indices of rows containing at least one lowercase character.

    Args:
        data (list of str): The character array to search.
        row (int, optional): The current row index. Defaults to 0.
        lines (list, optional): The list of row indices with lowercase characters. Defaults to None.

    Returns:
        list: Indices of rows containing lowercase characters.
"""
def find_lines_with_lowercase_recursive(data, row=0, lines=None):
    if lines is None:
        lines = []
    # Base case: If we have processed all rows
    if row >= len(data):
        return lines
    # Check if the current row contains any lowercase character
    if any(c.islower() for c in data[row]):
        lines.append(row)
    # Recur for the next row
    return find_lines_with_lowercase_recursive(data, row + 1, lines)

# 3 Collect all lowercase characters using recursive function
"""
    Recursively collects all lowercase characters from a 2D character array.

    Args:
        data (list of str): The character array to search.
        row (int, optional): The current row index. Defaults to 0.
        col (int, optional): The current column index. Defaults to 0.
        collected (list, optional): The list of collected lowercase characters. Defaults to None.

    Returns:
        list: All lowercase characters found in the array.
"""
def collect_lowercase_recursive(data, row=0, col=0, collected=None):
    if collected is None:
        collected = []
    # Base case: If we have processed all rows
    if row >= len(data):
        return collected
    # If we have processed all columns in the current row, move to the next row
    if col >= len(data[row]):
        return collect_lowercase_recursive(data, row + 1, 0, collected)
    # Check if the current character is lowercase and collect it
    if data[row][col].islower():
        collected.append(data[row][col])
    # Recur for the next character in the same row
    return collect_lowercase_recursive(data, row, col + 1, collected)

# 4 Find all positions of lowercase characters using recursive function
"""
    Recursively finds all positions of lowercase characters in a 2D character array.

    Args:
        data (list of str): The character array to search.
        row (int, optional): The current row index. Defaults to 0.
        col (int, optional): The current column index. Defaults to 0.
        positions (list, optional): The list of positions and characters found. Defaults to None.

    Returns:
        list: A list of tuples (row, col, character) for each lowercase character found.
"""
def find_lowercase_positions_recursive(data, row=0, col=0, positions=None):
    if positions is None:
        positions = []
    # Base case: If we have processed all rows
    if row >= len(data):
        return positions
    # If we have processed all columns in the current row, move to the next row
    if col >= len(data[row]):
        return find_lowercase_positions_recursive(data, row + 1, 0, positions)
    # Check if the current character is lowercase and record its position and character
    if data[row][col].islower():
        positions.append((row, col, data[row][col]))
    # Recur for the next character in the same row
    return find_lowercase_positions_recursive(data, row, col + 1, positions)


# Test the functions
if __name__ == "__main__":
    data_test = data  # You can switch to data2 for additional testing

    # 1 Count lowercase characters
    lowercase_count = count_lowercase_recursive(data_test)
    print(f"Total lowercase characters: {lowercase_count}")

    # 2 Find lines with lowercase characters
    lines_with_lowercase = find_lines_with_lowercase_recursive(data_test)
    print(f"Lines with lowercase characters: {lines_with_lowercase}")

    # 3 Collect all lowercase characters
    collected_lowercase = collect_lowercase_recursive(data_test)
    print(f"Collected lowercase characters: {collected_lowercase}")

    # 4 Find all positions of lowercase characters
    lowercase_positions = find_lowercase_positions_recursive(data_test)
    print(f"Positions of lowercase characters: {lowercase_positions}")