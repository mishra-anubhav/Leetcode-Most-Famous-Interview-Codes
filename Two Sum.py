#Brute Force method to solve two sum problem- This method's time complexity is O(nsquare)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)-1):
            for j in range(len(nums)-1):
                if i!=j+1:
                    a=nums[i]+nums[j+1]
                    #print(i,'+',j+1,'=',a)  For the understanding
                    if a == target:
                        return ([i,j+1])
                        break
                    else:
                        continue
                else:
                    continue


#Efficient method to solve two sum problem by travering the whole listat once
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for idx, val in enumerate(nums):
            if target - val in nums[idx + 1:]:
                 #(nums[idx + 1:]) this takes the value after the list
                 return [idx, nums[idx + 1:].index(target - val) + (idx + 1)]
                 # nums[idx + 1:].index(target - val) + (idx + 1) finds the index from the list plus adds the value at which first index was found 


#Most efficient method using hashmap

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        Storage={}
        for ind,val in enumerate(nums):
            if target-val in Storage:
                return [Storage[target-val], ind]
            Storage[val] = ind
