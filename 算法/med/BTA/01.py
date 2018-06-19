
class Solution:
    def __init__(self):
        self.dt = {'1': '',
                   '2': 'abc',
                   '3': 'def',
                   '4': 'ghi',
                   '5': 'jkl',
                   '6': 'mno',
                   '7': 'pqrs',
                   '8': 'tuv',
                   '9': 'wxyz',
                   '0': ''}

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if len(digits) == 0:
            return []
        elif len(digits) == 1:
            return [s for s in self.dt[digits[0]]]

        elif len(digits) == 2:
            return [a + b for a in self.dt[digits[0]] for b in self.dt[digits[1]]]

        else:
            str_list = self.letterCombinations(digits[1:])
            return [a + b for a in self.dt[digits[0]] for b in str_list]