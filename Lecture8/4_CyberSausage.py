from fractions import Fraction
from math import floor


class Sausage:
    FULL_SIZE = 1  # Один батон - единичный объём
    SLICE_SIZE = 12  # Длина фарша в одном батоне (12 символов)

    def __init__(self, stuffing="pork!", volume="1"):
        self.stuffing = str(stuffing)
        self.volume = Fraction(volume)

    def __repr__(self):
        if self.volume * self.SLICE_SIZE < 1:
            return "/|\n||\n||\n||\n\\|"

        full_sausages = floor(self.volume)
        partial_sausage_length = int(self.volume % self.FULL_SIZE * self.SLICE_SIZE)

        sausage_parts = []
        for _ in range(full_sausages):
            sausage_parts.append(self._create_full_sausage())
        if partial_sausage_length > 0:
            sausage_parts.append(self._create_partial_sausage(partial_sausage_length))

        return self._combine_sausages(sausage_parts)

    def _create_full_sausage(self):
        stuff = (self.stuffing * (self.SLICE_SIZE // len(self.stuffing) + 1))[
            : self.SLICE_SIZE
        ]
        return (
            "/------------\\\n"
            f"|{stuff}|\n"
            f"|{stuff}|\n"
            f"|{stuff}|\n"
            "\\------------/"
        )

    def _create_partial_sausage(self, stuffing_length):
        stuff = (self.stuffing * (stuffing_length // len(self.stuffing) + 1))[
            :stuffing_length
        ]
        return (
            f"/{'-' * stuffing_length}|\n"
            f"|{stuff}|\n"
            f"|{stuff}|\n"
            f"|{stuff}|\n"
            f"\\{'-' * stuffing_length}|"
        )

    def _combine_sausages(self, sausages):
        rows = [sausage.split("\n") for sausage in sausages]
        combined = ["".join(row) for row in zip(*rows)]
        return "\n".join(combined)

    def __abs__(self):
        return abs(self.volume)

    def __add__(self, other):
        new_volume = self.volume + other.volume
        return Sausage(self.stuffing, max(new_volume, Fraction(0)))

    def __sub__(self, other):
        new_volume = self.volume - other.volume
        return Sausage(self.stuffing, max(new_volume, Fraction(0)))

    def __mul__(self, factor):
        if isinstance(factor, int) and factor >= 0:
            return Sausage(self.stuffing, self.volume * factor)
        raise ValueError("Multiplication factor must be a non-negative integer.")

    def __rmul__(self, factor):
        return self.__mul__(factor)

    def __truediv__(self, divisor):
        if isinstance(divisor, int) and divisor > 0:
            return Sausage(self.stuffing, self.volume / divisor)
        raise ValueError("Division divisor must be a positive integer.")

    def __bool__(self):
        return self.volume != 0


print(Sausage(":", "101.5") * 30)
