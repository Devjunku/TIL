package 기능개발

import java.util.*


fun main() {
    val s = Solution_42586_1()
    println(s.solution(arrayOf(93, 30, 55).toIntArray(), arrayOf(1, 30, 5).toIntArray()))
    println(s.solution(arrayOf(95, 90, 99, 99, 80, 99).toIntArray(), arrayOf(1, 1, 1, 1, 1, 1).toIntArray()))
}

private class Solution_42586_1 {
    fun solution(progresses: IntArray, speeds: IntArray): IntArray {
        var answer: IntArray
        var queue: Queue<Int> = LinkedList()
        val n = progresses.size
        for (i in 0 until n) {
            var leftDay = 0
            leftDay = (100-progresses[i])/speeds[i]
            if ((100-progresses[i]) % speeds[i] != 0) {
                leftDay ++
            }
            queue.add(leftDay)
        }

        var result = mutableListOf<Int>()

        while (queue.isNotEmpty()) {
            var count = 1
            var first = queue.poll()

            while (queue.isNotEmpty() && queue.peek() <= first) {
                queue.remove()
                count ++

            }
            result.add(count)
        }
        answer = result.toIntArray()
        return answer
    }
}