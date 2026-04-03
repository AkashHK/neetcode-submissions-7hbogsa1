class Solution:
    def isAnagram(self, str_S, str_T) -> bool:

        count_S, count_T = {}, {}
        if len(str_S) == len(str_T):
            for i in range(len(str_S)):
                count_S[str_S[i]] = 1 + count_S.get(str_S[i], 0)
                count_T[str_T[i]] = 1 + count_T.get(str_T[i], 0)
            return count_S == count_T
        return False
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        group_anagram = []
        for i in range(len(strs)):
            added_to_group = False
            for j in range(len(group_anagram)):
                if self.isAnagram(strs[i], group_anagram[j][0]):
                    added_to_group = True
                    group_anagram[j].append(strs[i])
            if not added_to_group:
                group_anagram.append([strs[i]])
        return group_anagram

        