# IBS Coding Fundamentals Exam

## Getting Started

- **Fork** this repository under your own account
- Clone your forked repository to your computer
- Create a `.gitignore` file so generated files won't be committed
- Commit your progress frequently and with descriptive commit messages
- All your answers and solutions should go in this repository
- Take care of style guide
- Take care of the naming of classes, fields, variables, files, etc.

## Keep in mind

- You can use any resource online, but **please work individually**

- **Don't just copy-paste** your answers and solutions,
  use your own words instead

- **Don't push your work** to GitHub until your mentor announces
  that the time is up

## Exercises


### Unique Characters

Create a function that takes a string as parameter
and returns a list with the unique letters of the given string.

Write 2 different unit test cases for the method.

#### Example

Input

```text
"anagram"
```

Output

```text
["n", "g", "r", "m"]
```

### Average temperature

Write a method which can read and parse a file containing information about
the average temperature of three European countries
to raise awareness of climate change.
Each line represents the average temperature of each country in the given year.
The actual year can be found at the end of each line.

The method should return the first coldest and hottest year in each country.

The application should write the data to the console as *key => value* pairs.

#### Example

[Example file can be found here.](temperatures_pckg/results.txt)

Output

```text
France => 1996, 2018
Sweden => 2004, 2017
Germany => 2000, 2017
```
