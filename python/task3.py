sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
}

sample=["name","salary"]

for i in sample:
 sample_dict.pop(i, None)

print (sample_dict)