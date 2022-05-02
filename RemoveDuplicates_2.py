class Solution:
    def deleteDuplicates(self, head: list) -> list:
        remove = 0
        return_list = []
        for val, a in enumerate(head):
            if a != head[-1]:
                if head[val + 1] != "-" and a == head[val + 1]:
                    head[val + 1] = "-"
                    remove += 1
            else:
                return_list.append(head[-1])

        for i in range(remove):
            head.remove("-")
        return head

sol = Solution()
print(sol.deleteDuplicates(head = [1,1,2,3,5,6]))