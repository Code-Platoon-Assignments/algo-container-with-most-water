def maxArea(heights: list[int]) -> int:
    def calculate_area(height: int, width: int) -> int:
        return height * width

    answer = 0
    left = 0
    right = len(heights) - 1

    while left < right:
        width = right - left
        res = 0
        if heights[left] > heights[right]:
            res = calculate_area(heights[right], width)
            right -= 1
        else:
            res = calculate_area(heights[left], width)
            left += 1
        answer = res if res > answer else answer
    
    return answer
