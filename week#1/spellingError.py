from spellchecker import SpellChecker

def find_spelling_errors(text):
    # Create a SpellChecker object
    spell = SpellChecker()

    # Split the text into words
    words = text.split()

    # Find misspelled words
    misspelled = spell.unknown(words)

    # Print misspelled words
    if misspelled:
        print("Spelling errors found:")
        for word in misspelled:
            print(f"- {word}")
    else:
        print("No spelling errors found.")

if __name__ == "__main__":
    # Example text
    input_text = """This is a sample text with some speling erors. The quik brown fox jumps ovr the lazy dog."""

    find_spelling_errors(input_text)
