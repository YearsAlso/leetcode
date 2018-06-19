def group_anagrams(anagrams):
    anagram_dict = dict()
    for anagram in anagrams:
        anagram_key = list(anagram)
        anagram_key.sort()
        anagram_key = str(anagram_key)
        if anagram_dict.get(anagram_key)==None:
        	anagram_dict[anagram_key] = []
        anagram_dict[anagram_key].append(anagram)
        anagram_dict[anagram_key].sort()

    req_list =[]
    for key,value in anagram_dict.items():
        req_list.append(value)

    return req_list


anagrams = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(group_anagrams(anagrams))
