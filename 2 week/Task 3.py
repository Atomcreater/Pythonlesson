#187. Repeated DNA Sequences
#https://leetcode.com/problems/repeated-dna-sequences/description/?envType=problem-list-v2&envId=string
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        def findRepeatedDnaSequences(s):
            seen = set()
            repeated = set()

            for i in range(len(s) - 9):
                sequence = s[i:i + 10]
                if sequence in seen:
                    repeated.add(sequence)
                else:
                    seen.add(sequence)

            return list(repeated)

        return(findRepeatedDnaSequences(s))