def get_text(): # Function to get user input
    return input("Enter a paragraph of text:\n")

def clean_text(text):
    text = text.lower()
    punctuation = [",", ".", "!", "?"]
    for punct in punctuation:
        text = text.replace(punct, "")
    return text

def split_text(text):
    return text.split()

def count_words(words):
    word_counts = {}
    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    return word_counts

def most_common(word_counts):
    sorted_words = sorted(word_counts.items(), key=sort_count, reverse=False)
    return sorted_words[:5]

def sort_count(item):
    return (-item[1], item[0])

text = get_text()
cleaned = clean_text(text)
words = split_text(cleaned)
counts = count_words(words)
top_words = most_common(counts)

for word, number in top_words:
    print(word, number)





