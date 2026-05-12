# STEP 1A
# Import SQL Library and Pandas
import sqlite3
import pandas as pd

# STEP 1B
# Connect to the database
conn = sqlite3.connect("data.sqlite")


# STEP 2
# Select employeeNumber and lastName from employees
df_first_five = pd.read_sql("""SELECT employeeNumber, lastName FROM employees""", conn)

# STEP 3
# Same as step 2 but lastName comes first
df_five_reverse = pd.read_sql("""SELECT lastName, employeeNumber FROM employees""", conn)

# STEP 4
# Same as step 3 but alias employeeNumber as ID
df_alias = pd.read_sql("""SELECT lastName, employeeNumber AS ID FROM employees""", conn)

# STEP 5
# Use CASE to label Executives vs Not Executives
df_executive = pd.read_sql("""
SELECT *,
    CASE
        WHEN jobTitle = 'President' OR jobTitle = 'VP Sales' OR jobTitle = 'VP Marketing'
        THEN 'Executive'
        ELSE 'Not Executive'
    END AS role
FROM employees
""", conn)

# STEP 6
# Find the length of each employee's last name
df_name_length = pd.read_sql("""SELECT LENGTH(lastName) AS name_length FROM employees""", conn)

# STEP 7
# Return the first two letters of each job title
df_short_title = pd.read_sql("""SELECT SUBSTR(jobTitle, 1, 2) AS short_title FROM employees""", conn)

# STEP 8
# Calculate the rounded total price per order, then sum them all
sum_total_price = pd.read_sql("""
SELECT ROUND(priceEach * quantityOrdered) AS total_price
FROM orderDetails
""", conn).sum().reset_index(drop=True)

# STEP 9
# Return orderDate plus day, month, year columns
df_day_month_year = pd.read_sql("""
SELECT orderDate,
    strftime('%d', orderDate) AS day,
    strftime('%m', orderDate) AS month,
    strftime('%Y', orderDate) AS year
FROM orders
""", conn)

conn.close()
