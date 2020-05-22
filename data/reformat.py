with open("locations.txt", 'r') as f:
    items = f.readlines()

new_items = [x[:-1] for x in items if x != "\n"]
print(new_items)


str_items = "\n".join(new_items)

with open("locations.txt", 'w') as f:
    f.write(str_items)
