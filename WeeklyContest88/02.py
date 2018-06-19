class Solution:
    def maxDistToClosest(self, seats):
        """
        :type seats: List[int]
        :rtype: int
        """
        list_seat = "".join([str(s) for s in seats])
        print(list_seat)
        list_distance = []
        list_empty= list_seat.split('1')
        for i,seat in enumerate(list_empty):
            if seat != "":
                list_distance.append(len(seat)//2+1)
            if i==0 and list_seat[0]!="1":
                list_distance.append(len(seat))
            if i== len(list_empty)-1 and list_seat[-1]!='1':
                list_distance.append(len(seat))
        return max(list_distance)


def main():
    sol = Solution()
    print(sol.maxDistToClosest([1,0,0,1]))


if __name__ == '__main__':
    main()
