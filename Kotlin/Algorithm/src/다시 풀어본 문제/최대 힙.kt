package `다시 풀어본 문제`

import java.io.BufferedReader
import java.io.InputStreamReader
import java.util.*

fun main() = with(BufferedReader(InputStreamReader(System.`in`))) {
    val inputNum = readLine().toInt()
    var priorityQueue = PriorityQueue<Int>()

    var number: Int
    var sb = StringBuilder()
    for (i in 0 until inputNum) {
        number = readLine().toInt()
        when (number) {
            0 -> {
                if(priorityQueue.isNotEmpty()) {
                    sb.append("${priorityQueue.poll() * (-1)}\n")
                }
                else {
                    sb.append("0\n")
                }
            }
            else -> {
                priorityQueue.add((-1) * number)
            }
        }
    }
    println(sb)
}