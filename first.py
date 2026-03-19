def is_palindrome(s: str) -> bool:
    """Return True if s is palindrome, ignoring spaces and case."""
    normalized = ''.join(ch.lower() for ch in s if ch.isalnum())
    return normalized == normalized[::-1]


def main():
    text = input('Enter text to check for palindrome: ').strip()
    if text == '':
        print('No input provided.')
        return

    if is_palindrome(text):
        print(f'"{text}" is a palindrome.')
    else:
        print(f'"{text}" is not a palindrome.')


if __name__ == '__main__':
    main()
