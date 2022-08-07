class Solution:
    def trap(self, height):
        left = 0
        right = 1
        totalRainArea = 0

        def calcRainWater(left, right):
            if left + 1 == right and (left == 0):
                return 0

            if left + 1 == right and height[left - 1] > height[left]:
                return height[right] - height[left]

            area = (height[left]) * (right - left - 1)
            for i in range(left + 1, right):
                area -= height[i]
            return area

        while True:

            print(f"left at: {left}, \n right at: {right}")
            # 종료조건
            if left == len(height) - 1 or right == len(height):
                break

            else:
                if height[left] <= height[right]:
                    print("rainwater collected")
                    totalRainArea += calcRainWater(left, right)
                    left = right

                # Move Left Pointer
                elif right == len(height) - 1:
                    print("no rain here, moving left")
                    left += 1
                    right = left + 1
                    continue

                right += 1

        return totalRainArea


# height = [5, 4, 1, 2]
# height = [4, 2, 3]
# height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
height = [0, 7, 1, 4, 6]
answer = Solution().trap(height)
print(answer)
