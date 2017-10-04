def test_triple_double(word):
    count = 0
    i = 0
    while i < len(word)-1:
        if word[i] == word[i+1]:
            count = count + 1
            if count == 3:
                return True
            i = i + 2
        else:
            count = 0
            i = i + 1
    return False

def find_triple_double():
    fin = open('words.txt')
    for line in fin:
        word = line.strip()
        if test_triple_double(word):
            print(word)

print(find_triple_double())