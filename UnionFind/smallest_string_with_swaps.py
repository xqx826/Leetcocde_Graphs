from path_compression import FindUnion_PathComp

class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        groups = FindUnion_PathComp(len(s))
        for a,b in pairs:
            groups.union(a,b)
        if groups.count == 1:
            return "".join(sorted(s))
        
        letter_dict = dict()
        for i in range(len(groups.root)):
            r = groups.find(i)
            if r in letter_dict:
                letter_dict[r][0].append(i)
                letter_dict[r][1].append(s[i])
            else:
                letter_dict[r] = [[i], [s[i]]] 
        # now sort
        st = set()
        for item in letter_dict:
            print(letter_dict[item])
            letter_dict[item][1].sort()
            letter_dict[item][0].sort()
            for i in range(len(letter_dict[item][1])):
                st.add((letter_dict[item][0][i], letter_dict[item][1][i]))
        new_str = [' ' for _ in range(len(s))]
        for item in st:
            new_str[item[0]] = item[1]
        
        return "".join(new_str)