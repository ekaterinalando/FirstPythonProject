with open('python.jpg', 'rb') as file:
    chunk_size = 4096
    file_content = file.read(chunk_size)
    print(file_content)

    with open('python_copy.jpg', 'wb') as wfile:
        wfile.write(file_content)


