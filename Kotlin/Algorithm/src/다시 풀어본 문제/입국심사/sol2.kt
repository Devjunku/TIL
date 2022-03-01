package `다시 풀어본 문제`.입국심사

import java.io.BufferedReader
import java.io.InputStreamReader

fun main() = with(BufferedReader(InputStreamReader(System.`in`))) {
    val (n, m) = readLine().split(" ").map { it.toInt() }
    val Immigration = Array(n) { r ->
        readLine().toLong()
    }

    var left: Long = 0
    var right = (Immigration.maxOrNull()!! * m)

    while (left <right) {
        val mid = (left + right) / 2
        var total: Long = 0

        for (time in Immigration) {
            total += (mid / time)
        }

        if (total >= m) {
            right = mid
        } else {
            left = mid + 1
        }
    }
    println(left)
}