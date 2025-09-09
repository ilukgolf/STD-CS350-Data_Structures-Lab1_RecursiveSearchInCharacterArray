# https://github.com/ilukgolf/STD-CS350-Data_Structures-Lab1_RecursiveSearchInCharacterArray
# Lab 1: Recursive Search In Character Array
# Student: Jirawat Bunmaraksasakul
# ID: 1630708046

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

def count_lowercase_recursive(data, row=0, col=0):
    if row >= len(data):
        return 0
    if col >= len(data[row]):
        return count_lowercase_recursive(data, row + 1, 0)
    count = 1 if data[row][col].islower() else 0
    return count + count_lowercase_recursive(data, row, col + 1)

def find_lines_with_lowercase_recursive(data, row=0, lines=None):
    if lines is None:
        lines = []
    if row >= len(data):
        return lines
    if any(c.islower() for c in data[row]):
        lines.append(row)
    return find_lines_with_lowercase_recursive(data, row + 1, lines)

def collect_lowercase_recursive(data, row=0, col=0, collected=None):
    if collected is None:
        collected = []
    if row >= len(data):
        return collected
    if col >= len(data[row]):
        return collect_lowercase_recursive(data, row + 1, 0, collected)
    if data[row][col].islower():
        collected.append(data[row][col])
    return collect_lowercase_recursive(data, row, col + 1, collected)

def find_lowercase_positions_recursive(data, row=0, col=0, positions=None):
    if positions is None:
        positions = []
    if row >= len(data):
        return positions
    if col >= len(data[row]):
        return find_lowercase_positions_recursive(data, row + 1, 0, positions)
    if data[row][col].islower():
        positions.append((row, col, data[row][col]))
    return find_lowercase_positions_recursive(data, row, col + 1, positions)


if __name__ == "__main__":
    data_test = data  # You can switch to data2 for additional testing

    lowercase_count = count_lowercase_recursive(data_test)
    print(f"Total lowercase characters: {lowercase_count}")

    lines_with_lowercase = find_lines_with_lowercase_recursive(data_test)
    print(f"Lines with lowercase characters: {lines_with_lowercase}")

    collected_lowercase = collect_lowercase_recursive(data_test)
    print(f"Collected lowercase characters: {collected_lowercase}")

    lowercase_positions = find_lowercase_positions_recursive(data_test)
    print(f"Positions of lowercase characters: {lowercase_positions}")