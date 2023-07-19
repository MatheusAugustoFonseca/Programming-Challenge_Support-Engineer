def array_through(array):
    letters = []
    numbers = []

    for item in array:
        if isinstance(item, str):
            letters.append(item)
        elif isinstance(item, int):
            numbers.append(item)

    return letters, numbers


def largest_number(numbers):
    if len(numbers) == 0:
        raise IndexError("There are no numbers in your list")

    largest = max(numbers)

    return largest


exemple_array = ["a", 10, "b", "hello", 122, 15]
letters, numbers = array_through(exemple_array)
print("Only letters array:", letters)
print("Only numbers array:", numbers)

largest_number_value = largest_number(numbers)
print("Largest number:", largest_number_value)
