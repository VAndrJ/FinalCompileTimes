import re

def parse_and_average(filename):
    with open(filename, 'r') as file:
        content = file.read()

    arrays = re.findall(r'\[\s*([^\]]+)\]', content)

    for idx, array_text in enumerate(arrays, 1):
        numbers = [float(num.strip()) for num in array_text.split(',') if num.strip()]
        if len(numbers) <= 2:
            print(f"Array {idx}: Not enough numbers to drop min and max.")
            continue
        numbers.remove(min(numbers))
        numbers.remove(max(numbers))
        average = sum(numbers) / len(numbers)
        print(f"Array {idx} average (after dropping min/max): {average:.2f}")

if __name__ == "__main__":
    parse_and_average("README.md")
