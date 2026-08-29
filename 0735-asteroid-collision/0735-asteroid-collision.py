class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        ans=[]
        ans.append(asteroids[0])
        for i in range(1,len(asteroids)):
            if ans and ans[-1] > 0 and asteroids[i] < 0:
                valid=True
                while ans and ans[-1]*asteroids[i]<0 :
                    if abs(ans[-1])<abs(asteroids[i]):
                        ans.pop()
                    elif abs(ans[-1])==abs(asteroids[i]):
                        ans.pop()
                        valid=False
                        break 
                    elif abs(ans[-1])>abs(asteroids[i]):
                        valid=False
                        break
                if valid:
                    ans.append(asteroids[i])
            else:
                ans.append(asteroids[i])
        return ans

