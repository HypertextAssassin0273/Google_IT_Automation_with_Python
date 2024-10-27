## Module 4 Graded Assessment
* **Total points: 10**
* **Score: 100%**

#### Note:
This graded quiz assesses your understanding of the concepts and procedures covered in the lab you just completed. Please answer the questions based on the activities you performed in the lab.

- You can refer to your completed lab for help with the quiz.
- In order to complete this quiz, you must have completed the lab before it.

<br>

### Question 1

What should Windows users do to connect to their VM in the provided lab environment?

- Open the Terminal application in Linux and enter the VM's IP address.
- Use the local Terminal application to connect using a PEM key.
- **Download the PPK key file from the Qwiklabs Start Lab page and use PuTTY for SSH connection.**
- Add Secure Shell to the Chrome browser and enter the VM's hostname.

### Question 2

What is the primary purpose of the **os** module?

- It allows you to perform mathematical operations and calculations efficiently.
- **It provides a portable way of using operating system dependent functionality with Python.**
- It enables you to create graphical user interfaces (GUIs) for Python applications.
- It is used for managing data serialization and deserialization tasks.

### Question 3

In the lab's Python script, what is the primary role of the `error_search` function when working with regular expressions (RegEx)?

- To compile a fixed RegEx pattern for matching specific error codes in the log file
- To encrypt and secure log file data using RegEx patterns
- To use RegEx for splitting the log file into individual logs
- **To create and search for RegEx patterns based on user input to identify errors in the log file**

### Question 4

What is the purpose of the `sys.exit(0)` statement in the script, and how does it affect the execution of the Python script?

- The `sys.exit(0)` statement is used to forcibly terminate the script, even if there are errors in the code.
- The `sys.exit(0)` statement is used to pause the script's execution and wait for user input before continuing.
- The `sys.exit(0)` statement is used to display an error message to the user and halt the script's execution if any errors are encountered.
- **The `sys.exit(0)` statement is used to indicate successful termination of the script, and it has no impact on the script's execution.**

### Question 5

In the lab’ script, what is the purpose of the `if __name__ == "__main__":` block, and why is it important for the execution of the script?

- The `if __name__ == "__main__":` block is used to display an error message to the user if any errors are encountered during script execution.
- The `if __name__ == "__main__":` block is used to define custom functions for the script, and it doesn't impact the script's execution.
- **The `if __name__ == "__main__":` block is the main entry point of the script, where the script's execution begins when it is run as the main program.**
- The `if __name__ == "__main__":` block is used to specify the author's name and copyright information for the script.

### Question 6

You are analyzing a log file. What would happen if you didn’t escape special characters in your regular expression? 

- The script would not run.
- There would be no effect.
- **The regular expression would match the literal character instead of the special meaning.**
- The regular expression would not match anything.

### Question 7

What is the purpose of defining the `main` function in the script, and why is it significant for the script's execution?

- **The `main` function serves as the entry point of the script and is executed when the script is run as the main program.**
- The `main` function is used to display error messages to the console and is executed only if errors are encountered during script execution.
- The `main` function is used to define custom functions within the script and is executed at the end of the script's execution.
- The `main` function defines the file paths for the log file and the output file and is executed at the beginning of the script's execution.

### Question 8

How does the `find_error.py` script process the `fishy.log` file according to the provided content?

- The script translates the contents of `fishy.log` into another programming language for cross-platform compatibility.
- It compresses `fishy.log` to reduce its size for storage efficiency.
- It automatically detects and fixes syntax errors within `fishy.log`.
- **The script first searches `fishy.log` for user-specified errors and then generates a new file, `errors_found.log`, containing these errors.**

### Question 9

What is the primary purpose of the re module in Python?

- **To provide support for working with Regular Expressions for pattern matching in strings**
- To enhance graphical capabilities and user interface design
- To enable network connectivity and communication over the internet
- For data encryption and cybersecurity purposes

### Question 10

Apply what you’ve learned from this lab to answer this question. You are working on the `find_error.py` script to search for specific errors in the `fishy.log` file. If you need to find all instances of a network connection failure, which of the following steps would you take to modify the script accordingly?

- Change the error_patterns list to include only "network" and "failure", and then run the script with `fishy.log`.
- **Modify the user input line to specifically ask for "network connection failure" errors, then process `fishy.log`.**
- Rewrite the Regular Expression in the script to only match logs with the word "network".
- Edit the file_output function to filter out all logs except those containing the word "network".
