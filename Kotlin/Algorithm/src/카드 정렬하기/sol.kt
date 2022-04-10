package `카드 정렬하기`


import java.io.BufferedReader
import java.io.InputStreamReader
import java.util.PriorityQueue

fun main() = with(BufferedReader(InputStreamReader(System.`in`))) {
    val n = readLine().toInt()
    val pq = PriorityQueue<Int>()

    for (i in 0 until n) {
        pq.add(readLine().toInt())
    }

    var answer = 0
    while (pq.size > 1) {
        val num = pq.poll()  + pq.poll()
        answer += num
        if (pq.isEmpty()) break
        pq.add(num)
    }
    println(answer)
}