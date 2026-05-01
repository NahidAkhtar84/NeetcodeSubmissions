class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        fp, sp = 0, len(numbers)-1

        while sp > fp:
            sm = numbers[fp] + numbers[sp]

            if sm == target:
                return [fp+1, sp+1]
            elif sm > target:
                sp -= 1
            else:
                fp += 1

