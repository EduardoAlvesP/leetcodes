class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        mergeword = ""
        if len(word1) >= len(word2):
            smalllen = len(word2)
            bigstring = word1
        else:
            smalllen = len(word1)
            bigstring = word2
        for i in range(smalllen):
            mergeword = mergeword + word1[i] + word2[i]
        if(smalllen != len(bigstring)):
            for j in range(smalllen,len(bigstring)):
                mergeword = mergeword + bigstring[j]
        return mergeword

    