class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        mx = 0
        for i in sentences :
            li = i.split(" ")
            le = len(li)
            mx = max(le , mx)

        # mx = 0
        # li = sentences.split(",")

        # for i in li :
        #     count = 0
        #     count = i.count(" ")
        #     mx = max(mx , count)

        return mx
