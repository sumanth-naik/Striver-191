# Key Idea 1: Store as array of arrays and use Binary Search

class SnapshotArray:

    def __init__(self, length: int):
        self.arrOfCellHistory = [[[-1, 0]] for _ in range(length)]
        self.nextSnapId = 0

    def set(self, index: int, val: int) -> None:
        self.arrOfCellHistory[index].append([self.nextSnapId, val])

    def snap(self) -> int:
        self.nextSnapId += 1
        return self.nextSnapId - 1

    def get(self, index: int, snap_id: int) -> int:
        # Sequence comparison follows lexicographical ordering. Anything works here
        # return self.arrOfCellHistory[index][bisect.bisect_right(self.arrOfCellHistory[index], [snap_id, 1e9])-1][1]
        # return self.arrOfCellHistory[index][bisect.bisect_left(self.arrOfCellHistory[index], [snap_id+1])-1][1]
        return self.arrOfCellHistory[index][bisect.bisect_left(self.arrOfCellHistory[index], [snap_id, 1e9])-1][1]
