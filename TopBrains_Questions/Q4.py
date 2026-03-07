class Solution:
    def find_duplicate_words(self, sentence):
        words = sentence.lower().split(" ")
        duplicates = []
        #Write your code here
        for i in range(0, len(words)-1):
            if words[i] in duplicates:
                continue
            if words[i] == words[i+1]:
                duplicates.append(words[i])
    
        return duplicates