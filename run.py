
def main():
    text = input("Enter a paragraph of text:\n")
    cleaned_text = text.lower()
    punctuation_to_remove = [',', '.', '!', '?']
    for punct in punctuation_to_remove:
        cleaned_text = cleaned_text.replace(punct, '')
    words = cleaned_text.split()
    word_count = {}
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    sorted_words = sorted(word_count.items(), key=lambda x: (-x[1], x[0]))
    top_words = sorted_words[:min(5, len(sorted_words))]
    for word, count in top_words:
        print(f"{word}: {count}")
if __name__ == "__main__":
    main()
