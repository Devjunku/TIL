package `강의실 배정`

import java.io.BufferedReader
import java.io.InputStreamReader
import java.util.PriorityQueue

fun main() = with(BufferedReader(InputStreamReader(System.`in`))) {
    val n = readLine().toInt()
    val lecture = Array(n) {
        val (s, e) = readLine().split(" ").map { it.toInt() }
        StartEnd(s, e)
    }

    lecture.sortBy {
        it.start
    }

    val priorityQueue = PriorityQueue<Int>()

    priorityQueue.add(lecture[0].end)

    for (i in 1 until n) {
        if (priorityQueue.first() > lecture[i].start) {
            priorityQueue.add(lecture[i].end)
        } else {
            priorityQueue.poll()
            priorityQueue.add(lecture[i].end)
        }
    }
    println(priorityQueue.size)
}

data class StartEnd(val start: Int, val end: Int)