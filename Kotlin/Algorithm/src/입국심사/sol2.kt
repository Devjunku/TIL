package 입국심사

import java.io.BufferedReader
import java.io.InputStreamReader

fun main() = with(BufferedReader(InputStreamReader(System.`in`))) {
    val (n, m) = readLine().split(" ").map { it.toInt() }
    val waitTimeArr = LongArray(n) { element ->
        readLine().toLong()
    }

    var left: Long = 1
    var right: Long = (waitTimeArr.maxOrNull()!! * m)
    while (left < right) {
        val mid: Long = (left + right) / 2
        var total: Long = 0

        for (time in waitTimeArr) {
            total += (mid / time)
        }

        if (total >= m) {
            right = mid
        } else {
            left = mid + 1
        }
    }
    println(left)
    close()
}