import collections


class Solution:
    def find_empty(self, list_tasks):
        i = 0
        for value in list_tasks.reverse():
            if value == "*":
                i += 1
            else:
                return i
        return i
    
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        list_task = [0]
        if len(tasks) == 0:
            return 0
        dict_task = collections.Counter(tasks)
        list_task = sorted(dict_task.items(), key=lambda x: x[1])
        task_length = len(list_task)
        
        max_task = list_task[0][1]
        
        list_tasks = [['*'] * n + ['w']] * max_task
        print(list_tasks)
        
        for tasks in list_tasks:
            j = 0
            for i, task in enumerate(tasks):
                print(list_task[j])
                if task == "*":
                    if list_task[j][1] <= 0 and j >= task_length:
                        tasks[i] = '*'
                    else:
                        tasks[i] = list_task[j][0]
                        list_task[j][1] -= 1
                        j += 1
        print(list_tasks)
        return max_task * n - self.find_empty(list_tasks[-1])


print(Solution().leastInterval(["A", "A", "A", "A", "A", "B", "B", "B"], 2))
