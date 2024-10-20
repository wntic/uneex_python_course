def get_input_text() -> list[str]:
    text = []

    while True:
        row = input()
        if not row:
            break
        text.append(row)

    return text


def extract_numbers(tokens: list[str]) -> list[int]:
    numbers = []

    for token in tokens:
        if token[0] == "-" and str.isnumeric(token[1:]):
            numbers.append(int(token))
        elif str.isnumeric(token):
            numbers.append(int(token))

    return numbers


def max_int(text: list[str]) -> int:
    tokens = []

    for row in text:
        tokens += row.split(" ")
        tokens = [str.lower(token) for token in tokens]

    numbers = extract_numbers(tokens)
    return max(numbers) if numbers else 0


if __name__ == "__main__":
    text = get_input_text()
    max = max_int(text)
    print(max)
