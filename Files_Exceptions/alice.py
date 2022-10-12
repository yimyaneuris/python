filename = 'alice.txt'

try:
    with open(filename, encoding='UTF-8') as f:
        contents = f.read()
except FileNotFoundError:
    print(f"Upps!! the file {filename} does not exist")

else:
    words = contents
    

