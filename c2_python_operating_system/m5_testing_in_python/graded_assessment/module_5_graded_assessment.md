## Module 5 Graded Assessment
* **Total points: 10**
* **Score: 100%**

#### Note:
This graded quiz assesses your understanding of the concepts and procedures covered in the lab you just completed. Please answer the questions based on the activities you performed in the lab.

- You can refer to your completed lab for help with the quiz.
- In order to complete this quiz, you must have completed the lab before it.

<br>

### Question 1

What is the cause of an IndexError?

- **Attempting to access an index that's outside the bounds of a list.**
- Attempting to index a list with invalid parameters.
- Not specifying classes.
- Searching a list that contains errors.

### Question 2

When you looked for the script emails.py in the scripts directory, what command did you use to navigate to the scripts directory?

- `nano ~/scripts/emails_test.py` 
- `ls user_emails.csv`
- **`cd ~/scripts`**
- `cat emails.py`

### Question 3

When you began working with the existing emails.py script, what mode did you need to open it in? 

- Test mode
- Automation mode
- **Edit mode**
- Script mode

### Question 4

Which of the following statements accurately describe how try/except blocks work? Select all that apply.

- If an exception occurs during the execution of the try clause, the try clause is executed and ignored.
- If no exceptions occur, the try clause is ignored.
- **The try clause is executed.**
- **If an exception occurs during the execution of the try clause, the rest of the try clause is then skipped.**

### Question 5

When testing a working script with a known bug, what is the first step in the testing process? 

- Find all bugs in the software.
- Create a list of features that are unnecessary. 
- Use the software so that it works correctly
- **Reproduce the bug.**

### Question 6

When searching for an employee, the method email_dict.get(username) should return a valid email address unless the searched employee doesn’t exist. To return a message like, "No email address found" for a non-existent employee, what type of loop will do the job? 

- An edge case loop
- **An if-else loop**
- A try/except loop
- A unittesting loop

### Question 7

The following code will either return an email address for an employee or an error message if there is no employee matching the name entered. What would the error message be?

```py
if email_dict.get(fullname.lower()):
    return email_dict.get(fullname.lower())
else:
    return "No email"
```

- “No employee found”
- **“No email”**
- “No email address found”
- “Missing parameters”

### Question 8

Which of the following is the correct order of blocks in a try/except construct? 


- **try, except, finally, raise**
- raise, try, except, finally
- try, raise, except, finally
- try, except, raise, finally

### Question 9

The following portion of code will return an error message if a user fails to enter the full name of the employee for a search. What will the error message be?

```py
def find_email(argv):
 """ Return an email address based on the username given."""
 # Create the username based on the command line input.
 try:
   fullname = str(argv[1] + " " + argv[2])
   # Preprocess the data
   email_dict = populate_dictionary('/home/<username>/data/user_emails.csv')
   # Find and print the email
   return email_dict.get(fullname.lower())
 except IndexError:
   return "Missing name"
```

- IndexError”
- “No email address found”
- “Missing username”
- **“Missing name”**

### Question 10

When writing a try/except clause, how many except clauses can be included? 

- One more except clauses than there are specific handlers for different exceptions.
- **As many except clauses are needed to specify handlers for different exceptions.** 
- Only one.
- As many as needed as long as there is one try clause per except clause.
