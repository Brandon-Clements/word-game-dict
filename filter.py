# MIT License
#
# Copyright (c) 2022 Brandon Clements
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

MIN_LEN = 3
MAX_LEN = 10

with open('words.txt') as f:
    lines = f.readlines()

# Find line that splits head from dictonary
for (i, line) in enumerate(lines):
    if '---' in line:
        start_line = i
        break

# Split header from dictonary so we can copy it to start of new file
head = lines[0:i + 1]
lines = lines[i + 1:]
print(f"Number of starting words: {len(lines)}")

def count_caps(line):
    return sum(1 for x in line if x.isupper())

def count_nonalpha(line):
    return sum(1 for x in line if not x.isalpha() and not x.isspace())

# Remove acronyms (words with more than one capital)
lines = [line for line in lines if count_caps(line) <= 1]
print(f"Number of words after filtering acronyms: {len(lines)}")

# Remove words with numbers or symbols
lines = [line for line in lines if count_nonalpha(line) == 0]
print(f"Number of words after filtering symbols: {len(lines)}")

# Remove short and long words
lines = [line for line in lines if len(line) > MIN_LEN and len(line) < MAX_LEN]
print(f"Number of words after filtering short/long: {len(lines)}")

print(f"Number of filtered words: {len(lines)}")

with open('final.txt', 'w') as f:
    f.write("Filtered word list originaly generated from...\n")
    f.write("".join(head))
    f.write("".join(lines))
