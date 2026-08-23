class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()

        n = len(citations)

        for i in range(n):
            papers = n - i

            if citations[i] >= papers:
                return papers

        return 0