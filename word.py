#fin = open('words.txt')
#line = fin.readline()
#print(line)

#fin = open('words.txt')
#for line in fin:
 #   word = line.strip()
  #  print (word)

#def find_long_word():
    #fin = open('words.txt')
    #for line in fin:
   #     word = line.strip()
  #      if len(word) > 20:
 #           print (word)

#find_long_word()

def has_no_e(word):
    for letter in word:
        if 'e' in word:
            return True


    return False

#print(has_no_e('chicken'))

def find_words_no_e():
    fin = open('words.txt')
    counter_no_e = 0
    counter_total = 0
    for line in fin:
            counter_total +=1
            word = line.strip()
            if has_no_e(word):
                counter_no_e +=1
                #print(word)
    return counter_no_e/counter_total
    
print(find_words_no_e())



def avoids(word, forbidden):
    for letter in word:
        if letter in forbidden:
            return False

    return True

def find_words_no_vowels():
    fin = open('words.txt')
    counter_no_vowel = 0
    counter_total = 0
    for line in fin:
            counter_total +=1
            word = line.strip()
            if avoids(word, 'aeiou' ):
                counter_no_e +=1
                #print(word)
    return counter_no_vowel/counter_total

print('The percentage of the words with vowel letters is {:.2f}%.'.format(find_words_no_vowels()*100))

