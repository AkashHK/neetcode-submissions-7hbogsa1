class Solution:
    def isValid(self, s: str) -> bool:
        stack_list = []
        valid_forms = ('()', '{}', '[]')
        for bracket in s:
            if bracket in ('(', '[', '{'):
                stack_list.append(bracket)
            else:
                if not stack_list:
                    return False
                if (stack_list.pop() + bracket) not in valid_forms:
                    return False
        print(f"stack_list is {stack_list}")
        if not stack_list:
            return True
        return False