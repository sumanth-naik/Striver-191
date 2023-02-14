rooms = [[1],[2],[3],[]]

def canVisitAllRooms(rooms):
    visited = {0}
    stack = [0]
    while stack:
        roomNum = stack.pop()
        for key in rooms[roomNum]:
            if key not in visited:
                visited.add(key)
                stack.append(key)
    return len(visited)==len(rooms)
