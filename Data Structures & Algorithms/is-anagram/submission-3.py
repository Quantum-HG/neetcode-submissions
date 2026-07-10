class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) == len(t):
            dict_s = {}
            for word in s:
                if word not in dict_s:
                    dict_s[word] = 1
                else:
                    dict_s[word] += 1
            
            dict_t = {}
            for word in t:
                if word not in dict_t:
                    dict_t[word] = 1
                else:
                    dict_t[word] += 1
                    
            for key_s, value_s in dict_s.items():
                if value_s != dict_t.get(key_s):
                    return False
                    
            
            return True
            
        else:
            return False
            
            
