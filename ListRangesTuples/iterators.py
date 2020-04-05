# Iterators is nothing but the stream of data
string_list = ["str1","str2","str3","str4"]
string_iter = iter(string_list)
for i in range(len(string_list)):
    print(next(string_iter))