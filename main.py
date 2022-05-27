# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(word, anagram):

    anagramTestList = [word,anagram]
    for i in anagramTestList:
        if word.lower() == anagram.lower():
            return True

r = find_anagram('best','fre')
print(bool(r))

