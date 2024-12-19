## Module 7 Graded Assessment
* **Total points: 10**
* **Score: 100%**

#### Note:
This graded quiz assesses your understanding of the concepts and procedures covered in the lab you just completed. Please answer the questions based on the activities you performed in the lab.

- You can refer to your completed lab for help with the quiz.
- In order to complete this quiz, you must have completed the lab before it.

<br>

### Question 1

What is the primary purpose of using regular expressions in log analysis? 

- To format log messages for easier readability
- To encrypt log data for enhanced security
- **To extract specific patterns and information from unstructured log data**
- To compress log files and save storage space

### Question 2

What will the following command return?

&emsp;&emsp;&emsp;&emsp; `grep "ERROR Tried to add information to closed ticket" syslog.log`

- **All the ERROR logs in which the system tried to add information to closed ticket**
- A duplicate file of _syslog_ with the “Tried to add information to closed ticket” errors removed
- All the ERROR logs in _syslog_
- All the closed tickets in _syslog_ 

### Question 3

Complete the sentence for the following Python regular expression: To match a string stored in a line variable, we use the search() method by defining a_____.

- span
- line
- **pattern**
- log

### Question 4

When sorting this dictionary:

&emsp;&emsp;&emsp;&emsp; `fruit = {"oranges": 3, "apples": 5, "bananas": 7, "pears": 2}`

What will the following line of code return?

&emsp;&emsp;&emsp;&emsp; `sorted(fruit.items(), key=operator.itemgetter(1))`

- `[('bananas', 7), ('apples', 5), ('oranges', 3), ('pears', 2)]`
- `[('apples', 5), ('bananas', 7), ('oranges', 3), ('pears', 2)]`
- **`[('pears', 2), ('oranges', 3), ('apples', 5), ('bananas', 7)]`**
- `sorted fruit = {"oranges": 3, "apples": 5, "bananas": 7, "pears": 2}`

### Question 5

What is the primary advantage of using regular expressions when writing automation scripts to process a system log and generate reports from log files? 

- Simplify the process of creating log files
- Enhance the visual presentation of log data in reports
- Automate the installation of log analysis software
- **Flexible pattern matching for extracting specific data from log entries**

### Question 6

While you were working with the log file named _syslog.log_, what command did you use to view the file? 

- `cat file syslog.log`
- **`cat syslog.log`**
- `search syslog.log`
- `grep syslog.log`

### Question 7

What would you expect the command `grep "ERROR" syslog.log` to return?

- The _ERROR_ messages in syslog.log 
- **All _ERROR_ logs in syslog.log**
- All _ERROR_ logs in syslog.log that have no corresponding error message
- All logs in syslog.log

### Question 8

What is the Python module used to perform similar tasks to the Unix command `grep` for filtering log data? 

- `logfilter` module
- `grep` module
- `logsearch` module
- **`re` (Regular Expression) module**

### Question 9

Which argument can be used with the `sorted()` function to sort a dictionary's items based on their values in descending order? 

- `sorted(dictionary, key=lambda x: x[1], reverse=True)`
- **`sorted(dictionary.items(), key=lambda x: x[1], reverse=True)`**
- `sorted(dictionary, reverse=True)`
- `sorted(dictionary.values(), reverse=True)`

### Question 10

If there is no csv file named user_emails.csv, what will the command nano user_emails.csv return? 

- A new csv file named _user_emails.csv populated withusers emails_
- An error message
- A new csv file named nano _user_emails.csv_ 
- **A new csv file named _user_emails.csv_**
