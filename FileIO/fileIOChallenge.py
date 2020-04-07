with open("sample.txt", 'a') as table_file:
    for i in range(1, 13):
        table_string = "{:>2} times {} is {:<2}".format(i, 2, i * 2)
        print(table_string,file=table_file)