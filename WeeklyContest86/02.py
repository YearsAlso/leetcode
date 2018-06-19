class Solution:
    def canVisitAllRoomsCore(self,rooms,list_lock,i):
        if list_lock[i]==False and i>0:
            return
        list_lock[i] = False
        print(i)
        if len(rooms[i])==0:
            return
        else:
            for key in rooms[i]:
                self.canVisitAllRoomsCore(rooms, list_lock, key)
        return
    
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        list_lock = [True]*len(rooms)
        list_lock[0] = False
        self.canVisitAllRoomsCore(rooms,list_lock,0)
        return not sum(list_lock)
    
    
    
def main():
    sol = Solution()
    print(sol.canVisitAllRooms( [[1],[2],[3],[]]))
    
if __name__ == '__main__':
    main()
