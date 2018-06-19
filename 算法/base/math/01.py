def fizzBuzz(n):
    """
    :type n: int
    :rtype: List[str]
    """
    i = 1
    req_list = []
    while i <= n:
        num_str = ""
        if int(i % 15) == 0:
            num_str = 'FizzBuzz'
        elif int(i % 5) == 0:
            num_str = 'Buzz'
        elif int(i % 3) == 0:
            num_str = 'Fizz'
        else:
            num_str = str(i)
        req_list.append(num_str)
        i += 1
    return req_list