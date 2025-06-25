# Example list to append
my_list = ["Apple", "Banana", "Cherry"]

# Append the list to the file
with open("example.txt", "a") as file:
    for index, item in enumerate(my_list, start=1):
        file.write(f"{index}. {item}\n")

# Display the file contents with numbers
with open("example.txt", "r") as file:
    for line_number, line in enumerate(file, start=1):
        print(f"{line_number}: {line.strip()}")