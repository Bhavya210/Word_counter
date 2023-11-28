def word_count(text):
    words = text.split()
    return len(words)

# Example usage:
input_text = "This is a sample text for word counting in Python."
result = word_count(input_text)
print(f"Word count: {result}")
