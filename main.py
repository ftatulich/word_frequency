from collections import Counter
from re import findall


def word_frequency(paragraph: list[str]) -> dict[str, int]:
    try:
        if not paragraph:
            return {}

        frequency = Counter()
        for sentence in paragraph:
            words = findall(r'\b\w+\b', sentence.lower())
            frequency.update(words)
        return dict(frequency)
    except Exception as e:
        print(f'error: {e}')
