test_list = [-4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

def even_app(parameters):
    edited_list = []
    for i in parameters:
        if i % 2 == 0:
            edited_list.append(i)
    return edited_list

print(f"Alkuperäinen lista on {test_list}")

result = even_app(test_list)
print(result)

print(test_list)
