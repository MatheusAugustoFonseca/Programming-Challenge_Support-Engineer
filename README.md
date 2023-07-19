# Programming Challenge - Support Engineer
The purpose of this repository is to upload my Programming  Challenge for a Support Engineer position at Lexart labs.

## Intro
The objective of this challenge was to create an algorithm that traverses an array that contains string of letters and numbers.
#### The results must have:
+ An array containing only letters;
+ An array containing only numbers;
+ Obtain the largest number from the numbers array.

## Methodology
To perform this challenge I chose Python as the main programming language.

Developing the solution I choose to create two functions to resolve this problem;
```python
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
```
 1. The first function, named ```array_through(array)```, receive an array as argument and goes through it. To analyze all array position there is a ```for... in loop``` and there are two conditions checking the type of each position item, with the ```isinstance()``` function. The first ```if``` check if the item is an string type, by recingving ```True``` or ```False```, receiving ```True``` the item is appended for another array, called ```letters```. The second ```if``` check if the item is an integer type, by rreceiving ```True``` or ```False```, receiving ```True``` the item is appended for another array, called ```numbers```. And then, the function return the two new arrays, ```letters``` and ```numbers```, now filled with the itens from the array placed on ```array_through()``` as argument, divided by type.
 2. The second function, named ```largest_number(numbers)```, receives an array of numbers as argument and goes through it. It checks if the list is empty using an if condition. If the list is empty, it raises an error informing ```There are no numbers in your list```. Otherwise, it finds the largest number using the ```max()``` function and stores it in the ```largest``` variable. Finally, it returns the largest number."

## Results Analysis
```python
exemple_array = ["a", 10, "b", "hello", 122, 15]
letters, numbers = array_through(exemple_array)
print("Only letters array:", letters)
print("Only numbers array:", numbers)

largest_number_value = largest_number(numbers)
print("Largest number:", largest_number_value)
```

To analize the algorithm results I used ```exemple_array = ["a", 10, "b", "hello", 122, 15]```, as an argument for ```array_through(exemple_array)``` function, unpacking the return in two variables, ```letters``` and ```numbers```. Then with two prints, we can see the results obtained:
+ ```Only letters array: ['a', 'b', 'hello']```
+ ```Only numbers array: [10, 122, 15]```
  
To analize the ```largest_number()```, I called it with the ```numbers``` variable unpacked as an argument, and stored at a new variable, ```largest_number_value```. The final result is showed at the last print:
+ ```Largest number: 122```

## Conclusion
The algorithm created was able to iterate through all array inputted, obtaining:
+ An array containing only letters;
+ An array containing only numbers;
+ A variable with the largest number.
