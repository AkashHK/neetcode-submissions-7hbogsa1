class Solution:
    # def isAnagram(self, str_S, str_T) -> bool:

    #     count_S, count_T = {}, {}
    #     if len(str_S) == len(str_T):
    #         for i in range(len(str_S)):
    #             count_S[str_S[i]] = 1 + count_S.get(str_S[i], 0)
    #             count_T[str_T[i]] = 1 + count_T.get(str_T[i], 0)
    #         return count_S == count_T
    #     return False
    def makeHash(self, str_S) -> tuple[int]:

        hash_list = [0] * 26
        for i in range(len(str_S)):
            hash_list[ord(str_S[i]) - ord('a')] += 1
        return tuple(hash_list)
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        group_anagram = []
        anagram_list = {}
        for i in range(len(strs)):
            temp_hash = self.makeHash(strs[i])
            if temp_hash in anagram_list:
                anagram_list[temp_hash].append(strs[i])
            else:
                anagram_list[temp_hash] = [strs[i]]
        for key, value in anagram_list.items():
            group_anagram.append(value)
        return group_anagram

        