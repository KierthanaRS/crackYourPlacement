class Solution:
    def isValid(self, s: str) -> bool:
        st=[]
        if len(s)%2==1:
            return False
        d={")":"(","}":"{","]":"["}
        for i in s:
            if i in "({[":
                st.append(i)
            else:
                if st:
                    k=st.pop()
                    if k!=d[i]:
                        return False
                else:
                    return False
        return len(st)==0

        