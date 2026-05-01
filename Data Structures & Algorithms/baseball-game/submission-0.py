class Solution:
    def calPoints(self, operations: List[str]) -> int:
        result = []

        for o in operations:
            if o == '+':
                sum_val = result[-1] + result[-2]
                result.append(sum_val)
            elif o == 'D':
                doubled_val = result[-1]*2
                result.append(doubled_val)
            elif o == 'C':
                result.pop()
            else:
                result.append(int(o))
        
        return sum(result)
        