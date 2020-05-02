class Solution:
    def checkValidString(self, s: str) -> bool:
        star = []
        left = []
        for index, element in enumerate(s):
            #print(left, star , index, element)
            if element == '(':
                left.append(index)
            elif element == ')':
                if not left and not star:
                    return False
                elif left:
                    left.pop()
                elif not left and star:
                    if(star[-1] < index):
                        star.pop()
                    else:
                        return False
            elif element == '*':
                star.append(index)
        #print(left, star)
        if not left:
            return True
        elif left and star and len(star) >= len(left):
            i = len(left) - 1
            while(left):
                #print(left, star, "Last clear")
                if(star[-1] > left[i]):
                    star.pop()
                    left.pop()
                    i -= 1
                else:
                    return False
        else:
            return False
        if not left:
            return True
