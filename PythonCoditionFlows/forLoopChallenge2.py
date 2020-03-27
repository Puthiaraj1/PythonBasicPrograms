# Challenge description - similar to for challenge 1 but finding '.' at the end of each ip address
ipAddress = input("Please enter any ip address")
# Character array , if you specify negative value it will read character from reverse
if ipAddress[-1] != '.':
    ipAddress += '.'
segment = 1
segment_length = 0

for character in ipAddress:
    if character == '.':
        print("segment {} contains {} characters".format(segment, segment_length))
        segment += 1
        segment_length = 0
    else:
        segment_length += 1
