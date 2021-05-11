sent  = input("Enter a sentence:")
words = sent.split()

vowels = ['a','e','i','o','u']
vowels_words={}

for word in words:
    for letter in list(word):
        if letter in vowels:
            if vowels_words.get(letter) == None:
                vowels_words[letter] =[word]
            else:
                vowels_words.get(letter).append(word)
                
print(vowels_words)