# put your code here.

paragraph = open("test.txt")
word_counts = {}

for line in paragraph:
    line = line.rstrip()
    words = line.split(" ")
    
    
    for word in words:
        word_counts[word] = word_counts.get(word, 0) + 1
    
print word_counts
        
    
