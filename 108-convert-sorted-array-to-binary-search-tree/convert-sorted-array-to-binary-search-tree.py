# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:  
        def array(left,right):
            if left>right:
                return None
            mid=(left+right)//2
            node=TreeNode(nums[mid])
            node.left=array(left,mid-1)
            node.right=array(mid+1,right)
            return node
        return array(0,len(nums)-1)
        