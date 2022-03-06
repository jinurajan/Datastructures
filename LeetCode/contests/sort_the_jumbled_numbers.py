


from typing import List
class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        map_values = {}
        for idx, val in enumerate(mapping):
            map_values[idx] = val
        
        def find_map(val):
            result = 0
            denomination = 0
            if val < 10:
                return map_values[val]
            while val:
                carry, val = val % 10, val // 10
                print(val, carry)
                map_val = map_values[carry]
                result += map_val * pow(10, denomination)
                denomination += 1
            print(result)
            return result
        mapped_values = [(find_map(val), idx) for idx,val in enumerate(nums)]
        print(mapped_values)
        mapped_values = sorted(mapped_values)
        result = []
        for val, idx in mapped_values:
            result.append(nums[idx])
        return result

# mapping = [8,9,4,0,2,1,3,5,7,6]
# nums = [991,338,38]
# print(Solution().sortJumbled(
#     mapping=mapping,
#     nums=nums))
# mapping = [0,1,2,3,4,5,6,7,8,9]
# nums = [789,456,123]
# print(Solution().sortJumbled(
#     mapping=mapping,
#     nums=nums))

mapping = [9,8,7,6,5,4,3,2,1,0]
nums = [0,1,2,3,4,5,6,7,8,9]

print(Solution().sortJumbled(
    mapping=mapping,
    nums=nums) == [9,8,7,6,5,4,3,2,1,0])


                
                
        