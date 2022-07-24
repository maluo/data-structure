class Solution:
    """
    @param words1: a list of string
    @param words2: a list of string
    @param pairs: a list of string pairs
    @return: return a boolean, denote whether two sentences are similar or not
    """
    """
    words1[A,B,C]
    words1[B,A,C]
    PAIRS:{[A,B],[B,C],[A,C]}
    MP:{A:[A,B,C],B:{B,C}} -- check if this is possible
    """

    def isSentenceSimilarity(self, words1, words2, pairs):
        # write your code here
        if(not (len(words1) == len(words2))):
            return False

        mp = {}
        for i in range(len(pairs)):
            S = set()
            # if pairs[i][0] alreay found in hashmap
            if(not (mp.get(pairs[i][0]) == None)):
                S = mp[pairs[i][0]]
            S.add(pairs[i][1])
            mp[pairs[i][0]] = S  # make A:[A,B] - paris: {[A,B]}
        for i in range(len(words1)):
            if(words1[i] == words2[i]):
                continue
    # cause A->B and B->A could be both possible
            if((mp.get(words1[i]) == None or words2[i] not in mp[words1[i]]) and (mp.get(words2[i]) == None or words1[i] not in mp[words2[i]])):
                return False
        return True
