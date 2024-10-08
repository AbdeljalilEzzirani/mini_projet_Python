files = ["log_2023.txt", "log_2024.csv", "report_2023.pdf", "data_2024.csv", "log_2025.csv"]

i = 0
length = len(files)
files_log = []
files_csv = []
while i < length:
    if files[i].startswith('log_'):
            files_log.append(files[i])
    if files[i].endswith('.csv'):
        files_csv.append(files[i])
    i += 1




print(" \n ---> Files commençant par 'log_':")
print(files_log)

print(" \n ---> Files avec l'extension '.csv':")
print(files_csv)
