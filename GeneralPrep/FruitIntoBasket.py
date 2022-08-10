class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        visited_fruit = dict()
        length = 0
        left = 0
        
        for right in range(len(fruits)):
            if fruits[right] in visited_fruit:
                visited_fruit[fruits[right]] += 1
            else:
                visited_fruit[fruits[right]] = 1
            
            while len(visited_fruit) > 2:
                visited_fruit[fruits[left]] -= 1
                if visited_fruit[fruits[left]] < 1:
                    del visited_fruit[fruits[left]]
                left += 1
            length = max(length, right-left+1)
        return length
