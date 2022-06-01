# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True

def find_anagram(word, anagram):
    word = word.replace(' ', '')
    anagram = anagram.replace(' ', '')
    word = word.lower(); anagram = anagram.lower()

    return sorted(word) == sorted(anagram)

print(find_anagram('evil','Vile'))
print(find_anagram('bElow','elBow'))
print(find_anagram('whiskey','wisky'))
