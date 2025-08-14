class Solution:
    """
    题意：一维直线上小行星依次出现，正数表示向右、负数表示向左；
         两颗相向而行才会碰撞（右>0 遇 左<0）。碰撞时绝对值大的存活，大小相等同归于尽。
         返回所有碰撞结束后的剩余序列（保持相对顺序）。

    解法（栈模拟）：
    - 用栈维护“当前稳定”的小行星序列。
    - 对于每个新小行星 a：
        * 只有当“栈顶向右 (stack[-1] > 0)”且“当前向左 (a < 0)”时会发生碰撞；
        * 比较 |a| 与 栈顶：
            - 若 |a| > 栈顶：栈顶被炸掉，继续与新的栈顶比较（循环）；
            - 若 |a| == 栈顶：栈顶出栈，a 也销毁（结束比较）；
            - 若 |a| < 栈顶：a 被销毁（结束比较）。
        * 若没有被销毁（包括根本不相撞），把 a 入栈。
    - 栈中剩余即为答案。

    复杂度：每个元素最多入栈出栈一次，时间 O(n)，空间 O(n)（最坏）。
    """
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        n = len(asteroids)
        stack = []
        for i in range(n):
            destroyed = False
            while stack and stack[-1] > 0 and asteroids[i] < 0 and not destroyed:
                if -asteroids[i] < stack[-1]:
                    destroyed = True
                elif -asteroids[i] > stack[-1]:
                    stack.pop(-1)
                else:
                    stack.pop(-1)
                    destroyed = True
            if not destroyed:
                stack.append(asteroids[i])
        return stack