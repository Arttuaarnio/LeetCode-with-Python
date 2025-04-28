# Vastaus kopioitu suoraan LeetCode:n editorista

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1_counter = Counter(nums1)
        result = []
        for number in nums2:
            if nums1_counter[number] > 0:
                result.append(number)
                nums1_counter[number] -= 1
        return result