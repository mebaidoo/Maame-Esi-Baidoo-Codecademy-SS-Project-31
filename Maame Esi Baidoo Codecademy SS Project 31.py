import codecademylib3
from sklearn import preprocessing
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np

# load in financial data
financial_data = pd.read_csv('financial_data.csv')

# code goes here
#Inspecting the data
print(financial_data.head())
#Saving each column in a separate variable
month = financial_data.Month
revenue = financial_data.Revenue
expenses = financial_data.Expenses
#Creating a plot of revenue over the last six months
#print(financial_data.tail())
plt.plot(month, revenue)
plt.xlabel("Month")
plt.ylabel("Amount ($)")
plt.title("Revenue")
plt.show()
plt.clf()
#Creating a plot of expenses over the last six months
plt.plot(month, expenses)
plt.xlabel("Month")
plt.ylabel("Amount ($)")
plt.title("Expenses")
plt.show()
#Plots show expenses are increasing while revenues are decreasing
#Loading expenses csv file into a pandas dataframe and look at expenses to see how to cut expenses
expense_overview = pd.read_csv("expenses.csv")
print(expense_overview.head(7))
#Storing the Expense column containing different categories of expenses in a variable and the Proportion column in another variable
expense_categories = expense_overview["Expense"]
proportions = expense_overview["Proportion"]
#Creating a pie chart of the expenses proportions and combining all categories with smaller proportions in "Other"
expense_categories = ['Salaries', 'Advertising', 'Office Rent', 'Other']
proportions = [0.62, 0.15, 0.15, 0.08]
plt.clf()
plt.pie(proportions, labels = expense_categories)
plt.title("Expense Categories")
plt.axis("equal")
plt.tight_layout()
plt.show()
#expense_cut tells which category the company should cut down costs on in a big way
expense_cut = "Salaries"
#Loading employees data in a pandas dataframe to see which employee to let go off depending on productivity score to cut down salaries expenses
employees = pd.read_csv("employees.csv")
print(employees.head())
#Sorting the column containing the productivity percentages in ascending order
sorted_productivity = employees.sort_values(by = ["Productivity"])
print(sorted_productivity)
#Storing the first 100 employees from sorted data in a variable, that is, the less 100 productive employees to cut
employees_cut = sorted_productivity.head(100)
print(employees_cut)
#Saving what transformation should be used on the income and productivity columns, which contain outliers to explore the relationship between them, to a variable
transformation = "standardization"
#Selecting the Commute Time Column
commute_times = employees["Commute Time"]
#Getting the descriptive statistics for commute times
print(commute_times.describe())
#Exploring the shape of the commute time data using a histogram
#plt.clf()
#plt.hist(commute_times)
#plt.title("Employee Commute Times")
#plt.xlabel("Commute Time")
#plt.ylabel("Frequency")
#plt.show()
#The histogram appears to be right-skewed
#Making the histogram from the data appear more symmetrical using log transformation
commute_times_log = np.log(commute_times)
#print(commute_times)
#print(commute_times_log)
plt.clf()
plt.hist(commute_times_log)
plt.title("Employee Commute Times")
plt.xlabel("Commute Time")
plt.ylabel("Frequency")
plt.show()
print(commute_times.skew())
print(commute_times_log.skew())
#Looks like the log transformation significantly reduced the right-skewness of the data
#Applying standardization to the income and productivity columns of the employees data to see the relationship between these two on the same scale
income_and_prod_data = employees[["Salary", "Productivity"]]
scaler = preprocessing.StandardScaler()
standardized_data = scaler.fit_transform(income_and_prod_data)
print(standardized_data)
standardized_dataframe = pd.DataFrame(standardized_data)
print(standardized_dataframe)
plt.clf()
#Plotting income against productivity using the standardized data
plt.plot(standardized_dataframe[0], standardized_dataframe[1])
plt.show()