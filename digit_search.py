#%%
import re
import gzip
import pickle as pkl


def find_abc_sequences(s):
    # Define the regex pattern
    pattern = r'(?<![一二三四五六七八九])[一二三四五六七八九]+(?![一二三四五六七八九])'
    
    # Find all matches in the string
    matches = re.findall(pattern, s)
    
    return matches
def save_text_as_gzip(text, filename):
    with gzip.open(filename, 'wt', encoding='utf-8') as file:
        file.write(text)
def load_text_from_gzip(filename):
    with gzip.open(filename, 'rt', encoding='utf-8') as file:
        text = file.read()
    return text
# %%
digit_sequences = []
filenames = glob.glob("text/chinese_text_*.gz")
filenames.sort()
for file in filenames:
    print(file)
    text = load_text_from_gzip(file)
    print(len(text),text.count("一四一五九二"),text.count("一四一五二九") )
    digit_sequences.extend(find_abc_sequences(text))
    print(len(digit_sequences))


# %%
long_sequences = []
for seq in digit_sequences:
    if len(seq)>1:
        long_sequences.append(seq)
print(len(long_sequences))
# %%
chinese_digits = "一二三四五六七八九"

import math
def benfords_law_expected(digit):
    """
    Returns the expected frequency of a digit as the leading digit 
    according to Benford's Law.
    """
    if digit < 1 or digit > 9:
        raise ValueError("Digit should be between 1 and 9 inclusive")
    return math.log10(1 + 1/digit)

def check_benfords_law(numbers):
    """
    Checks if a list of numbers follows Benford's Law.
    Returns a dictionary with observed and expected frequencies for each leading digit.
    """
    # Extract leading digits
    leading_digits = [n[0] for n in numbers]  # Ignoring zeros

    # Compute observed frequencies
    observed_freqs = {digit: leading_digits.count(digit) / len(leading_digits) for digit in chinese_digits}

    # Compute expected frequencies according to Benford's Law
    expected_freqs = {i: benfords_law_expected(i) for i in range(1, 10)}

    return {
        'observed': observed_freqs,
        'expected': expected_freqs
    }

# Test
numbers = long_sequences
result = check_benfords_law(numbers)
print("Observed Frequencies:", result['observed'])
print("Expected Frequencies:", result['expected'])
# %%
