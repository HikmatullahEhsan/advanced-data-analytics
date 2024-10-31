""" The objective of this assignment is to apply the DIKW (Data-Information-Knowledge-Wisdom) framework to understand, analyze, and derive insights from an employee performance dataset.

Dataset:
    Use the "DIKW_HW_Activity Dataset" which is Employee Performance Dataset and provided attached to this assignment. You can either download or manually create the CSV file using the data provided.

Instructions:
1. Data:
    Look at the raw data in the CSV file. Open it in any spreadsheet software (e.g., Excel, Google Sheets) or load it 
    using Python (e.g., Pandas DataFrame) as we did in the class. 
    Understand the data fields such as EmployeeID, EmployeeName, Department, Salary, PerformanceScore, etc.
    Answer the following questions:
    What are the different types of data present (e.g., categorical, numerical)?
    What are some examples of raw data from the dataset?
2. Information:
    Process the data to create meaningful summaries. You can use a spreadsheet formula or Python code.
    Tasks:
    Calculate the average salary for each department.
    Find the number of employees in each country.
    Determine the average performance score for all employees.
    Write your findings in a short summary. For example:
    "The average salary in the Engineering department is $73,500."
    "The number of employees in the USA is 2."
3. Knowledge: Answer the following questions:
    Which department has the highest average performance score? Why do you think that might be the case?
    Which countries have the most satisfied employees based on the job satisfaction score?
4. Applying Wisdom for Decision-Making: Imagine you are an HR manager who wants to improve employee satisfaction and performance.
    Answer the following questions:
    How can you improve job satisfaction for the department with the lowest scores?
    What kind of training or incentives would you suggest for improving employee performance?
    Are there any notable differences in salaries by gender that should be addressed?
    Submission and Grading:
    Submit a report including the responses to all tasks mentioned above under all four sections.
    You can submit this as a word document, pdf, or ipynb notebook.
    The following are the categories of the grading for this assignment:
    1. Complete understanding of the dataset. 
    2. Correct calculations and meaningful summaries. 
    3. Appropriate interpretation of information. 
    4. Thoughtful recommendations for improvement. 
    5. Clarity, completeness, and professionalism of the report.
    Bonus Task: Visualising your findings and submitting the assignment in ipynb notebook.

"""

import numpy as np
import pandas as pd

src_file = pd.read_csv("data/DIKW_HW_Activity.csv")


print(src_file.head())
# What are the different types of data present (e.g., categorical, numerical)?
# There are several types of data present:
#  1) Nominal Categorical  type: 'USA', 'UK', 'HR', 'FINANACE', 'MARKETING' (Nominal categorical)
#  2) Binary Categorical type: 'MALE', 'FEMALE'
#  3) Numerical continuous type: Salary, Performance score, and job statisfication
#  4) Date and Time: Joining date
