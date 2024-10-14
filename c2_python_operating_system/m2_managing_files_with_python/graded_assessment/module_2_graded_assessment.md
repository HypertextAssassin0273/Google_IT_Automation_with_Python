## Module 2 Graded Assessment
* **Total points: 10**
* **Score: 100%**


### Question 1

Which Python function would you use to open a CSV file? 

- file.open()
- **open()**
- csv.reader()
- csv.open()

### Question 2

What are headers in the context of a CSV file?

- **Headers are the first row in a CSV file, typically containing the names of each column.**
- Headers are special characters or symbols used to separate data items in a CSV file.
- Headers are additional rows added at the end of a CSV file to summarize the data.
- Headers refer to the metadata that describes the source and author of the CSV file.

### Question 3

What is the advantage of using absolute paths compared to relative paths?

- **Absolute paths work consistently regardless of the current working directory.**
- Absolute paths are always secure and prevent unauthorized access.
- Absolute paths are shorter and easier to type.
- Absolute paths are required for all file system operations.

### Question 4

Considering the current directory is /user/share/doc/python3, what command will display the contents of the subdirectory "examples" within the current directory?

- dir examples
- ls /user/share/doc/python3/examples
- cd examples
- **ls examples**

### Question 5

When using the open function in Python, what does the first parameter typically represent?

- **The name of the file you want to open**
- A description of what you intend to do with the file
- An optional encoding type for the file contents
- The mode you want to open the file in (e.g., read, write)

### Question 6

You're writing Python code to read a text file line by line. After printing each line, you notice an extra blank line appearing in the output. How can you modify the code to eliminate these extra blank lines while still preserving the content of each line?

- Open the file in binary mode instead of read mode.
- **Use the strip method on each line before printing it.**
- Modify the loop to skip printing lines containing only whitespace characters.
- Change the print function call to print(line, end="").

### Question 7

In Python, how can you determine the current working directory from which your script is being executed?

- The script's filename provides information about the working directory.
- There's a built-in current_directory variable.
- **Use the os.getcwd() method from the os module.**
- You need to specify the working directory when running the script.

### Question 8

You have a CSV file with information about employees, including columns for name, department, and salary. What's the advantage of using csv.DictReader compared to the standard csv.reader function when working with this data in Python?

- There's no significant difference, both functions achieve the same result.
- csv.DictReader automatically converts all data types in the CSV file.
- csv.DictReader is faster for reading large CSV files.
- **csv.DictReader allows you to access data by column names (like keys in a dictionary) which is more intuitive and easier to manage.**

### Question 9

Imagine you're working in a terminal on a Linux or Unix-based system. You've been instructed to navigate to the "data" directory and then list the files within that directory. Which of the following commands would achieve the desired outcome?

- **cd data and ls**
- view data
- show data
- open data

### Question 10

In Python's csv module, what's the primary benefit of registering a dialect like empDialect with csv.register_dialect as shown in the code snippet: csv.register_dialect('empDialect', skipinitialspace=True, strict=True)?

- It ensures that all CSV files processed by your program will use this specific dialect.
- It simplifies error handling when dealing with CSV files that might have inconsistencies.
- **It allows you to define custom parsing behavior (like removing leading spaces) for CSV files without explicitly specifying the parameters every time you use the csv module.**
- It creates a new dialect object that can be reused for multiple CSV files.
