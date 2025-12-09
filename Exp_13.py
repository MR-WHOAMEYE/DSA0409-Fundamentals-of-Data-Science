from collections import Counter
import string
with open("sample_text.txt", "r") as file:
    text = file.read()
text = text.lower()
text = text.translate(str.maketrans("", "", string.punctuation))
words = text.split()
word_freq = Counter(words)
print("Word Frequency Distribution:")
for word, freq in word_freq.items():
    print(f"{word}: {freq}")
