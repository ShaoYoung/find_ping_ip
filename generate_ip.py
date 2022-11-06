import pandas
import openpyxl
import re

# pattern = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
file = 'ip_adresses.xlsx'


ip_addresses = ['192.168.186.' + str(i) for i in range (100, 200)]      # List comprehension
# print(ip_adresses_last)
df = pandas.DataFrame({'IP_adresses': ip_addresses})
df.to_excel(file)
