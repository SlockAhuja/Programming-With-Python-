# Ahuja Slock

with open('file1.txt', 'r') as f1:
    data1 = f1.read()

with open('file2.txt', 'r') as f2:
    data2 = f2.read()

with open('merged.txt', 'w') as merged_file:
    merged_file.write(data1)
    merged_file.write('\n')  # Optional newline between files
    merged_file.write(data2)

print("Files merged into 'merged.txt'")
