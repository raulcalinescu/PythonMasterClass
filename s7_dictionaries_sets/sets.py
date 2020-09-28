# Create a program that takes some text and returns a list of all the
# characters in the text that are not vowels, sorted in alphabetical order.

# you can either enter the text from the string or initialize a string variable
# with the string

my_input = input("My text is:")
vowels = frozenset("aeiou")
# vowels = {'a', 'e', 'i', 'o', 'u'}
final_set = set(my_input).difference(vowels)
my_list = sorted(final_set)
# for char in my_input:
  #  if char not in vowels and char != ' ':
   #     my_list.append(char)
print(my_list)

