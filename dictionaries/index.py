# A dictionary is an unordered collection of key-value pairs.
# A dictionary is defined using curly braces {} with key-value pairs separated by a colon :.

my_dict = {
    "name": "Bernard",
    "age": 25,
    "city": "Nairobi"
}


# You can access value using their keys.

print(my_dict["name"])

# You can add a new key-value pair or modify an existing one by assigning a value to a key

my_dict["email"] = "bernardbebeni@gmail.com"
my_dict["age"] = 28

print(my_dict.keys())
print(my_dict.items())

# You can loop through both key and values
for key, value in my_dict.items(): 
    print(f'{key}: {value}')



students = [
    {
        "name": "Bebeni",
        "school": "Computational",
        "year": "four"
    },
     {
        "name": "Omboga",
        "school": "Education",
        "year": "three"
    },
     {
        "name": "Paul",
        "school": "Science",
        "year": "second"
    },
     {
        "name": "Ryan",
        "school": "Mathematics",
        "year": "first"
    }
]


for student in students:
    print(student["name"], student["school"], student["year"], sep=", ")