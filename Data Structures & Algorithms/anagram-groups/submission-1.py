class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        anagram = defaultdict(list)

        for string in strs:

            key = "".join(sorted(string))
            anagram[key].append(string)

        return list(anagram.values())



        