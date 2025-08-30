# ⏱️ Flexible Counter Function

A non-interactive script that demonstrates a powerful and flexible `counter()` function in Python. This function can count in ascending or descending order between any two numbers with a specified step.

## Features of the `counter()` function

* **Counts Up & Down**: Automatically detects whether to count up (e.g., 1 to 10) or down (e.g., 10 to 0) based on the start and end values.
* **Customizable Step**: Allows the user to define the interval between numbers in the sequence.
* **Handles Edge Cases**: Correctly manages a step of `0` (defaults to 1) and negative steps (converts them to positive).
* **Animated Output**: Prints each number with a short delay to create a visual counting effect in the terminal.

## How to Use

1.  Ensure you have Python installed.
2.  Save the code as a `.py` file (e.g., `counter_function.py`).
3.  Run the script from your terminal:
    ```sh
    python counter_function.py
    ```
4.  The script will automatically run three predefined examples to demonstrate the function's capabilities. You can modify the script to call the `counter()` function with your own parameters.

### Script Output

```
------Counter function------
Counting from 1 to 10 by 1s
1 2 3 4 5 6 7 8 9 10 END!
Counting from 10 to 0 by 2s
10 8 6 4 2 0 END!
Counting from 10 to -10 by 2s
10 8 6 4 2 0 -2 -4 -6 -8 -10 END!
```
