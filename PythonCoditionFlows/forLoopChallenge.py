# Challenge description - get the ip address from keyboard and find the segments by the '.' character and
# print the segment length . in this challenge ip address can be anything (not necessary to have valid address)
# example 123.456.7890.11
ipAddress = input("Please enter any ip address")
segment = 1
segment_length = 0
character = ''
for character in ipAddress:
    if character == '.':
        print("segment {} contains {} characters".format(segment,segment_length))
        segment += 1
        segment_length = 0
    else:
        segment_length +=1
# Below check to find the last segment character length.
# Unlike Java & C language,in Python you can access the for loop variable outside the loop.
# But for loop has to be executed at least once . If you enter any empty character it will fail
# To fix the issue , initialize the variable
if character != '.':
    print("segment {} contains {} characters".format(segment,segment_length))
