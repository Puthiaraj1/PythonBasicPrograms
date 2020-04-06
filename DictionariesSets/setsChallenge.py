input_text = input("Please enter any text: ")
vowels_set = frozenset("aeiou")
input_text_set = set(input_text)
print(input_text_set)
print(vowels_set)

print(sorted(input_text_set.difference(vowels_set)))