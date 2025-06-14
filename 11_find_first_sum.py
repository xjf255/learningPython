"""
Dado un array de números y un número goal, encuentra los dos primeros números del array que sumen el número goal y devuelve sus índices. Si no existe tal combinación, devuelve None.

nums = [4, 5, 6, 2]
goal = 8

find_first_sum(nums, goal)  # [2, 3]
"""

def find_first_sum(nums: list[int], goal:int) -> list[int] | None:
    if nums is None or len(nums) < 2:
        return None
    
    seen = {}
    for i, num in enumerate(nums):
        complement = goal - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    
    return None