package 기능개발

import java.util.*

private class Solution_42586_2 {
    fun solution(progresses: IntArray, speeds: IntArray): IntArray {
        val n = progresses.size
        val days = IntArray(n) { i ->
            if ((100 - progresses[i]) % speeds[i] > 0) {
                ((100 - progresses[i]) / speeds[i]) + 1
            } else {
                ((100 - progresses[i]) / speeds[i])
            }
        }

        var stack = Stack<Int>()
        val answer = mutableListOf<Int>()

        for (i in 0 until n) {
            if (stack.isNotEmpty()) {
                if (stack.maxOrNull()!! < days[i]) {
                    answer.add(stack.size)
                    stack.clear()
                }
            }
            stack.push(days[i])
        }

        if (stack.isNotEmpty()) {
            answer.add(stack.size)
        }

        return answer.toIntArray()
    }
}