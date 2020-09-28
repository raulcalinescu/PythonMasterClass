menu = [
    ["egg", "bacon", "spam"],
    ["egg", "bacon", "sausage", "spam"],
    ["spam", "bacon", "sausage", "spam"],
    ["spam", "bacon", "spam", "sausage", "spam", "tomato", "spam"],
]

#does not work well with enumerate
# for list in menu:
#     for index, value in enumerate(reversed(list)):
#         if list[len(list) - 1 - index] == "spam":
#             del list[len(list) - 1 - index]
#     print(list)


for list in menu:
    for index in range (len(list) -1, -1, -1):
        if list[index] == "spam":
            del list[index]
    print(list)


