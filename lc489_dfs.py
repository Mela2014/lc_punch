class Solution:
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """
        def move_back():
            robot.turnLeft()
            robot.turnLeft()
            robot.move()
            robot.turnLeft()
            robot.turnLeft()

        def dfs(x, y, d):
            visited.add((x, y))
            robot.clean()
            for i in range(4):
                curr_d = (d+i)%4
                curr_x, curr_y = x + directions[curr_d][0], y+directions[curr_d][1]
                if (curr_x, curr_y) not in visited and robot.move():
                    dfs(curr_x, curr_y, curr_d)
                    move_back()
                robot.turnLeft()
        directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        visited = set()
        dfs(0, 0, 0)
