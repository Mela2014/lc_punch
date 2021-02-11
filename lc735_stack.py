# ast > 0 fly to right, won't crash previous
# ast < 0 fly to left, if previous same dir, won't crash either
# ast < 0 fly to left, previous fly to right, crash(previous crash, ast crash, both crash)
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for ast in asteroids:
            if ast > 0:
                stack.append(ast)
            elif not stack or stack[-1] < 0:
                stack.append(ast)
            else:
                while stack and stack[-1] > 0 and stack[-1] < -ast:
                    stack.pop()
                if not stack or stack[-1] < 0:
                    stack.append(ast)
                elif stack[-1] == -ast:
                    stack.pop()
        return stack

# ast crashed previous asteroid in the stack
# ast and previous both crash
# ast crash
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for ast in asteroids:
            while stack and stack[-1] > 0 > ast:
                if stack[-1] < -ast:
                    stack.pop()
                    continue
                elif stack[-1] == -ast:
                    stack.pop()
                break
            else:
                stack.append(ast)
        return stack
