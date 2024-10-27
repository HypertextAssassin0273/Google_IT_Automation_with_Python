## Module 3 Graded Assessment
* **Total points: 10**
* **Score: 100%**

#### Note:
This graded quiz assesses your understanding of the concepts and procedures covered in the module and lab you just completed. Please answer the questions based on what you learned from the module and the activities you performed in the lab. Questions 1-5 are based on the module. Questions 6-10 are based on the lab.

- You can refer to your completed lab for help with the quiz.
- In order to complete this quiz, you must have completed the lab before it.

<br>

### Question 1

Which of the following functions are used to match a regular expression pattern in Python? Select all correct answers. 

- **re.findall()**
- **re.findall()**
- **re.match()**
- re.find()

### Question 2

Which function from Python’s re module can you use to replace old text with new text? 

- re.compile() function
- **re.sub() function** 
- str.replace() method
- re.findall() function 

### Question 3

You are reading an article that includes some government websites in the form https://www.website-domain.gov. You’d like to make a list of these websites by extracting them from the text automatically, instead of copying and pasting them by hand. 

Complete the function find_gov_urls to accomplish this task for all websites that end with **.gov**.

```py
def find_gov_urls(website):
 pattern = r"https://www.[a-z]+.gov" #enter the regex pattern here
 result = re.findall(pattern, website) #enter the re method here
 return result

print(find_gov_urls("https://www.data.gov is a great place to find open source datasets!")) # Should return ['https://www.data.gov']
print(find_gov_urls("Learn more about US National Parks at https://www.nps.gov, https://www.nationalparks.org, or https://www.recreation.gov.")) # Should return ['https://www.nps.gov', 'https://www.recreation.gov']
print(find_gov_urls("The Library of Congress (https://www.loc.gov) is an incredible resource!")) # Should return ['https://www.loc.gov']
print(find_gov_urls("The Library of Congress (www.loc.gov) is an incredible resource!")) # Should return []
```

Output:
```
['https://www.data.gov']
['https://www.nps.gov', 'https://www.recreation.gov']
['https://www.loc.gov']
[]
```

### Question 4

You’re working with a dataset on capital cities around the world. This dataset includes a field that contains information on both city and country. You’d like to separate this field into two fields, a city field and a country field. In the current field, city and country are separated by either a comma or a period. Complete the function `parse_city_country` to split city and country into two strings and return only the city.

```py
def parse_city_country(text):
  pattern = r"([a-zA-Z ]+)[,.] [a-zA-Z]+" #enter the regex pattern here
  result = re.search(pattern, text) #enter the re method  here
  return "" if result == None else result[1] #return the correct capturing group

print(parse_city_country("Paris, France")) # should return Paris
print(parse_city_country("Mumbai, India")) # should return Mumbai
print(parse_city_country("Rio de Janeiro. Brazil")) # should return Rio de Janeiro
print(parse_city_country("Tokyo! Japan"))  # result should be blank
```

Output:
```
Paris
Mumbai
Rio de Janeiro
```

### Question 5

A company uses Product ID numbers to identify each product line it makes. Each product ID starts with 4 digits, followed by a hyphen (-), followed by two capital letters, followed by a hyphen (-), followed by two more digits, in the format 1234-AB-12. The manufacturing team records information about the production of each product line daily. 

You want to extract the product ID numbers of one of these product lines, which begins with a 1. The other characters in the product ID can be any digit or variable, as long as they follow the product ID format described above. Complete the following code so the `find_productID` function returns all product ID numbers that match the product of interest. 

```py
def find_productID(report):
  pattern = r"1\d{3}-[A-Z]{2}-\d{2}" #enter the regex pattern here
  result = re.findall(pattern, report) #enter the re method  here
  return result
  
print(find_productID("Products 1234-AB-30 and 2234-AB-30, not items 12-AB-30 or 12345-AB-30")) # Should return ['1234-AB-30']
print(find_productID("Products of interest are 1234-AB-30, 1678-XZ-11, and 1561-CD-57. We're not interested in other products like 2345-AB-29.")) # Should return ['1234-AB-30', '1678-XZ-11', '1561-CD-57']
```

Output:
```
['1234-AB-30']
['1234-AB-30', '1678-XZ-11', '1561-CD-57']
```

### Question 6

In the lab, you defined the `replace_domain` as:

```py
def replace_domain(address, old_domain, new_domain):
  old_domain_pattern = r'' + old_domain + '$'
  address = re.sub(old_domain_pattern, new_domain, address)
  return address
```

What role does this function have in the process of updating outdated domain names with new domain names?

- To iterate over a list of email addresses
- To write the updated list to a CSV file
- **To replace the old domain with the new domain in an email address**
- To read data from a CSV file

### Question 7

What is the purpose of initializing the `old_domain_email_list` in the code from the lab?

- **To store email addresses with the old domain that match the regex pattern**
- To store email addresses with the new domain
- To store all email addresses from `user_email_list`
- To perform a substitution operation on email addresses

### Question 8

Why is it considered good practice to use the `close()` method to close a file after processing it in Python?

- To ensure the file remains open for other processes to access.
- **To free up system resources and prevent further reading or writing to the file**
- To permanently delete the file from the system
- To encrypt the file and enhance its security

### Question 9

What is a key benefit of using Python for creating reports and employing regular expressions?

- **To automate repetitive tasks and data analysis.**
- To optimize website performance.
-  To develop virtual reality applications.
- To enhance cybersecurity measures.

### Question 10

In the Python script for processing `user_emails.csv`, what is the purpose of the `contains_domain` function?

- To count the number of email addresses in the CSV file
- **To check if an email address belongs to a specific domain, using Regular Expressions (RegEx)**
- To add a new domain to each email address in the CSV file
- To encrypt email addresses in the CSV file for security
