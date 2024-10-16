def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        
        #curr_anagram_ind = len(s)+1
        lttrs = set(p)
        p_key = [0]*26
        for l in p:
            p_key[ord(l)-ord('a')]+=1
        #p_dict = {}
        curr_anagram_len = 0
        curr_an_start = 0
        start_indices = []
        curr_key = [0]*26
        for i in range(len(s)):
            if s[i] in lttrs :
                if curr_anagram_len == 0:
                    curr_an_start = i
                    curr_anagram_len= 1
                    curr_key[ord(s[i])-ord('a')]+=1
                elif curr_anagram_len == len(p)-1:
                    if curr_key[ord(s[i])-ord('a')]+1 > p_key[ord(s[i])-ord('a')]:
                        curr_an_start=i
                        curr_anagram_len = 1
                        curr_key = [0]*26
                        p_key[ord(s[i])-ord('a')]+=1
                    else:
                        start_indices.append(curr_an_start)
                        #curr_anagram_len =
                        curr_key[ord(s[curr_an_start])-ord('a')]-=1
                        p_key[ord(s[i])-ord('a')]+=1
                        curr_an_start+=1
                else:
                    if curr_key[ord(s[i])-ord('a')] + 1 > p_key[ord(s[i])-ord('a')]:
                        curr_anagram_len = 1
                        curr_key = [0]*26
                        curr_an_start = i
                        curr_key[ord(s[i])-ord('a')]+=1
                    else:
                        curr_key[ord(s[i])-ord('a')]+=1
                        curr_anagram_len+=1
            elif curr_anagram_len > 0:
                curr_anagram_len = 0
                curr_key = [0]*26
        return start_indices