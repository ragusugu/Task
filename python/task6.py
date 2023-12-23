# file = r'python/task6.txt'
# find = "love"

# def read_check(file, find):
#     with open(file, 'r') as file:
#         content = file.read()
#         print(content)
#         position = content.find(find)
#         if position != -1:
#             return True
#         else:
#             return False
# def wrd_c(file):
#     wrd_count={}

# read_check(file, find)

def is_string_present(file_path, target_string):
    with open(file_path, 'r') as file:
        content = file.read().lower()  # Read file content and convert to lowercase for case-insensitive check
        return target_string.lower() in content

def word_count(file_path):
    word_counts = {}
    with open(file_path, 'r') as file:
        content = file.read().lower()
        words = content.split()

        for word in words:
            # Remove punctuation from words (if any)
            word = word.strip(".,!\?\"/'()[]{}")
            
            if word in word_counts:
                word_counts[word] += 1
            else:
                word_counts[word] = 1

    return word_counts

def print_word_counts(word_counts):
    for word, count in word_counts.items():
        print(f"{word}: {count}")

# Example usage:
file_path = 'python/task6.txt'  # Replace 'example.txt' with your file path
search_string = 'love'  # Replace 'example' with the string you want to search

# Check if the string is present in the file
if is_string_present(file_path, search_string):
    print(f"The string '{search_string}' was found in the file.")
else:
    print(f"The string '{search_string}' was not found in the file.")

# Get word counts and print them
counts = word_count(file_path)
print("Word counts in the file:")
print_word_counts(counts)
