import pandas
import openpyxl
import re

# считывает ip-адреса из xlsx-файла
def read_ip(file = 'ip_adresses.xlsx'):
    pattern = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
    workbook = openpyxl.load_workbook(file)
    sh_names = workbook.sheetnames
    ip_addresses = []
    for worksheet in sh_names:
        for row in workbook[worksheet].rows:
            for cell in row:
                match = re.findall(pattern, str(cell.value))
                if len(match)>0:
                    for ip in match:
                        ip_addresses.append(ip)
                        # print(f'Лист {worksheet} ячейка {cell.coordinate}')
    return ip_addresses
    # print(ip_addresses)
