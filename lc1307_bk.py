class Solution:
    def isSolvable(self, words: list[str], result: str) -> bool:
        max_woerd_len = max(map(len, words))
        if max_woerd_len < len(result) - 1:
            return False
        if max_woerd_len > len(result):
            return False

        words = words + [result]
        first_letters = set(word[0] for word in words if len(word) > 1)
        cols, rows = len(result), len(words)
        letter_to_digits = {}

        def search(col: int, row: int, carry: int) -> bool:
            if col == cols:
                return carry == 0
            if row == rows:
                quotient, reminder = divmod(carry, 10)
                return reminder == 0 and search(col + 1, 0, quotient)

            word = words[row]
            if col >= len(word):
                return search(col, row + 1, carry)

            letter = word[~col]
            sign = 1 if row < (rows - 1) else -1

            if letter in letter_to_digits:
                return search(col, row + 1, carry + sign * letter_to_digits[letter])

            init_digit = 1 if letter in first_letters else 0
            for digit in range(init_digit, 10):
                if digit not in letter_to_digits.values():
                    letter_to_digits[letter] = digit
                    if search(col, row + 1, carry + sign * digit):
                        return True
                    del letter_to_digits[letter]
            return False

        return search(0, 0, 0)
