# List Analysis Tool

A beginner-friendly Python project that allows users to build a list of numbers and then performs a simple analysis on the collected data.

## Features

- Stores numbers in a list
- Counts the total numbers entered
- Sorts the list in descending order
- Checks whether the number 5 is present
- Displays the complete list

## Technologies Used

- Python 3

## How to Run

1. Clone this repository:

```bash
git clone https://github.com/your-username/list-analysis-tool.git
```

2. Navigate to the project folder:

```bash
cd list-analysis-tool
```

3. Run the script:

```bash
python main.py
```

## Example

### Input

```text
Enter a number: 8
Would you like to continue? Y

Enter a number: 5
Would you like to continue? Y

Enter a number: 2
Would you like to continue? N
```

### Output

```text
Your list contains 3 numbers.
[8, 5, 2]
The value 5 is part of the list!
```

## Learning Objectives

This project demonstrates:

- Lists
- List methods (`append()` and `sort()`)
- User input handling
- Loops (`while`)
- Membership testing with `in`
- Conditional statements
- Basic data analysis

## Key Concepts

### Adding Values to a List

```python
numbers.append(number)
```

Adds a new element to the end of the list.

### Sorting in Descending Order

```python
numbers.sort(reverse=True)
```

Sorts the list from largest to smallest.

### Checking Membership

```python
if 5 in numbers:
```

Determines whether a value exists in the list.
