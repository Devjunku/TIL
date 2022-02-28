package 입국심사

import java.io.BufferedReader
import java.io.InputStreamReader

fun main() = with(BufferedReader(InputStreamReader(System.`in`))) {
    val (n, m) = readLine().split(" ").map { it.toInt() }
    val arr = LongArray(n)

    for (i in 0 until n) {
        arr[i] = readLine().toLong()
    }

    var left: Long = 1
    var right = (arr.maxOrNull()!! * m)

    while(left < right) {
        val mid: Long = (left + right) / 2
        var total:Long = 0

        for (time in arr) {
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