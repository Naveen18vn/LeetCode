class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        d=defaultdict(list)
        for i in strs:
            count=[0]*26
            for j in i:
                count[ord(j)-97]+=1
            a=tuple(count)
            d[a].append(i)
        return d.values()
            


        