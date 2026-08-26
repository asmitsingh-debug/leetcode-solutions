class Solution:
    def compress(self, chars: List[str]) -> int:
        if len(chars)==1:
            return 1
        i=0
        j=0
        while j<len(chars):
            char=chars[j]
            start=j
            while j<len(chars) and chars[j]==char:
                j+=1
            count=j-start
            chars[i]=char
            i+=1
            if count>1:
                for digit in str(count):
                    chars[i]=digit
                    i+=1
        return i