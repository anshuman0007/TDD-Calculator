import re

class Calc:

    def add(numbers: str) -> int:
        if not numbers:
            return 0
        
        delimiter = ",|\n"
        
        if numbers.startswith("//"):
            match = re.match(r"//(.+)\n(.*)", numbers)
            if match:
                delimiter, numbers = match.groups()
                delimiter = re.split(r"\[|\]", delimiter) if "[" in delimiter else [delimiter]
                delimiter = "|".join(map(re.escape, delimiter))

        num_list = re.split(delimiter, numbers)

        int_list = [int(n) for n in num_list if n]
        
        negatives = [n for n in int_list if n < 0]
        if negatives:
            raise ValueError(f"negative numbers not allowed: {','.join(map(str, negatives))}")
        
        return sum(int_list)

if __name__ == "__main__":
    user_input = input("Enter numbers (comma-separated or custom delimiter): ").encode().decode("unicode_escape").strip()
    #\n treated as new line "Error when using '//;\\n1;2"
    try:
        result = Calc.add(user_input)
        print("Sum:", result)
    except ValueError as e:
        print("Error:", e)