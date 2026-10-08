class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        visited = {}
        left = 0
        right = left + 1
        result = [left + 1, right + 1]
        while True:
            while right < len(numbers) and numbers[left] + numbers[right] < target:
                visited[numbers[right]] = right
                right += 1
            if right < len(numbers) and numbers[left] + numbers[right] == target:
                return [left + 1, right + 1]
            while left < right:
                wanted_val = target - numbers[left]
                if wanted_val in visited and visited[wanted_val] != left:
                    return [left + 1, visited[wanted_val] + 1]
                left += 1
        return result

