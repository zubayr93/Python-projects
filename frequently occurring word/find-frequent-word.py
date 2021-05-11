filename = input("Enter the file name: ")
if len(filename) < 1 : 
    filename = 'clown.txt'
words = []
word_count = {}
hand = open(filename)


# spliting words on the basis of spaces    
for l9 in hand:
    words = l9.split()
        
    # counting words appearing in the text
    for i in words :
        if word_count.get(i) == None:
            
        # key does not exist add it
            word_count[i] = 1
        
        else:
        # key already exist, increment the count
            word_count[i] = word_count[i] + 1
            
#print(word_count)    
largest = -1
theword= None
for k,v in word_count.items():
    #print (k,v)
    if v > largest:
        largest = v
        theword = k
        
print(f'the most frequent word used is {theword}, it occured {largest} times')
