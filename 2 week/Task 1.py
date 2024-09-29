#49. Group Anagrams
#https://leetcode.com/problems/group-anagrams/description/?source=submission-ac
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def group_anagrams(strs):
            anagram_dict = {}
            for word in strs:
                sorted_word = ''.join(sorted(word))
                if sorted_word in anagram_dict:
                    anagram_dict[sorted_word].append(word)
                else:
                    anagram_dict[sorted_word] = [word]
            return list(anagram_dict.values())
        return(group_anagrams(strs))