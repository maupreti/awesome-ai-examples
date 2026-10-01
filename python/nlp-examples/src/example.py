"""NLP Example - Text Processing Basics"""


def process_text(text):
    """Basic text processing example."""
    return {
        "original": text,
        "length": len(text),
        "words": len(text.split()),
        "uppercase": text.upper(),
        "lowercase": text.lower(),
    }


if __name__ == "__main__":
    sample_text = "Welcome to Natural Language Processing Examples"
    result = process_text(sample_text)
    print("NLP Example Results:")
    for key, value in result.items():
        print(f"  {key}: {value}")
