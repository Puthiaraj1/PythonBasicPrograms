jabber = open("sample.txt", 'r')

for line in jabber:
    print(line)

jabber.close()

# with keyword doen't required separate close() call
with open("sample.txt", 'r') as jabber1:
    for line in jabber1:
        if "JAB" in line.upper():
            print(line,end = "")
# # Uisng readlines()
with open("sample.txt",'r') as jabber2:
    lines = jabber2.readlines()
print(lines)
