class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []

        ans = []

        p_count = [0] * 26
        window = [0] * 26

        for ch in p:
            p_count[ord(ch) - ord('a')] += 1

        for i in range(len(p)):
            window[ord(s[i]) - ord('a')] += 1

        if window == p_count:
            ans.append(0)

        for i in range(len(p), len(s)):
            # Add new character
            window[ord(s[i]) - ord('a')] += 1

            # Remove character leaving the window
            window[ord(s[i - len(p)]) - ord('a')] -= 1

            if window == p_count:
                ans.append(i - len(p) + 1)

        return ans