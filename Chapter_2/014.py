fname = "hightemp.txt"
n = int(input("input>"))

with open(fname) as data_file:
    for i, line in enumerate(data_file):
        if i >= n:
            break
        print(line.rstrip())