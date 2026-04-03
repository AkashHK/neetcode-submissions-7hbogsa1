class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash_map = {}
        for character in s:
            if character in hash_map:
                hash_map[character] += 1
            else:
                hash_map[character] = 1
        for character in t:
            if character not in hash_map:
                return False
            hash_map[character] -= 1
        for key, value in hash_map.items(): 
            if value != 0:
                return False
        return True