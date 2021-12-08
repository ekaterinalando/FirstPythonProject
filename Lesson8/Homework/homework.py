with open('trimushketera.txt', 'r', encoding='UTF') as file:
    rfile = file.read().lower()
    word_count = rfile.split()
    def no_punct(string):
        punct = '.,!"()*?'
        for i in string:
            if i in punct:
                string = string.replace(i,"")
        return string
    word_count = [no_punct(word) for word in word_count]
    unique_count = set(word_count)

with open('results.txt', 'w', encoding='UTF') as wfile:
    wfile.write(f'Total words: {len(word_count)}\n')
    wfile.write(f'Total unique words: {len(unique_count)}\n')
    wfile.write(str(sorted(unique_count)))
