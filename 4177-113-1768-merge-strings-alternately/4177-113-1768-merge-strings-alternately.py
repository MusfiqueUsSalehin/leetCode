class Solution:
    def mergeAlternately(self,w1, w2):
        strn=""
        for i in range(len(w1)):
            if len(w1)>len(w2):
                strn+=w1[i]
                if i<len(w2):
                    strn+=w2[i]
            elif len(w1)<len(w2):
                strn+=w1[i]
                strn+=w2[i]
                if i==len(w1)-1:
                    for j in range(len(w2)):
                        if j>i:
                            strn+=w2[j]

                
            else:
                strn+=w1[i]
                strn+=w2[i]
        return strn
                
word1 = "abc"
word2 = "pqr"
f=Solution()
print(f.mergeAlternately(word1,word2))