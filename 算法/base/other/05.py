# def Valid(strs,head,tail):
#     """
#     :type s: str
#     :rtype: bool
#     """
#     search_dict = {"(":")","{":"}","[":"]"}
#     if int(tail-head)%2==0:
#         return False
#
#     if head>tail:
#         return True
#     else:
#         if search_dict.get(strs[head])==None:
#             return False
#         else:
#             tail_n = strs[head:tail+1].find(search_dict[strs[head]])
#             if tail_n==-1:
#                 return False
#             elif (tail_n == tail):
#                 return Valid(strs, head + 1, tail - 1)
#             else:
#                 tail_n+=head
#                 return Valid(strs,head,tail_n) and Valid(strs,tail_n+1,tail)
#
# def isValid(strs):
#     if len(strs) == 0:
#         return False
#     return Valid(strs,0,len(strs)-1)


def isValid(s):
    """
    :type s: str
    :rtype: bool
    """
    stack = []
    for c in s:
        if c == '(' or c == '{' or c == '[':
            stack.append(c)
        elif not stack:
            return False
        elif c == ')' and stack.pop() != '(':
            return False
        elif c == '}' and stack.pop() != '{':
            return False
        elif c == ']' and stack.pop() != '[':
            return False
    return not stack


print(isValid("{}{{}}"))