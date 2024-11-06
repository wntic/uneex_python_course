class Morse:
    def __init__(self, symbols="di dit dah"):
        # Default Morse representations
        self.dot = "di"
        self.end_dot = "dit"
        self.dash = "dah"
        self.letter_sep = " "
        self.word_sep = ", "

        # Parse symbols provided if any
        parts = symbols.split()
        if len(parts) >= 3:
            self.dot, self.end_dot, self.dash = parts[:3]

        # Internal structures to build Morse code
        self._morse_code = []
        self._current_letter = []
        self._first_in_letter = (
            True  # Track if we're adding the first symbol in a letter
        )

    def __pos__(self):  # Handle "+"
        # Append dot or end_dot based on position in letter
        if self._first_in_letter:
            self._current_letter.append(self.dot)
            self._first_in_letter = False
        else:
            self._current_letter.append(self.end_dot)
        return self

    def __neg__(self):  # Handle "-"
        # Append dash and update letter state
        if self._first_in_letter:
            self._current_letter.append(self.dash)
            self._first_in_letter = False  # Subsequent symbols are not the first
        else:
            self._current_letter.append(self.dash)  # Still allow appending dashes
        return self

    def __invert__(self):  # Handle "~"
        # End current letter, prepare for a new letter
        if self._current_letter:
            # Join current letter symbols with letter separator
            self._morse_code.append(self.letter_sep.join(self._current_letter))
            self._current_letter = []
            self._first_in_letter = True  # Reset for the next letter
        return self

    def __str__(self):
        # Add any remaining letter to Morse code
        if self._current_letter:
            self._morse_code.append(self.letter_sep.join(self._current_letter))

        # Join letters with word separators and return without end message
        return self.word_sep.join(self._morse_code)


# Test case
print(-+Morse())  # Should output: "dah dit"
