import re

def remove_consecutive_duplicates(input_str):
    pattern = r'(\w)\1{2}'
    match = re.search(pattern, input_str)
    while match:
        input_str = re.sub(pattern, '', input_str)
        match = re.search(pattern, input_str)
    return input_str
input_str = "aabbbaccddddc"
print(remove_consecutive_duplicates(input_str))