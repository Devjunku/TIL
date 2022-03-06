package `공유기 설치`

import java.io.BufferedReader
import java.io.InputStreamReader

fun main() = with(BufferedReader(InputStreamReader(System.`in`))) {
    val (n, c) = readLine().split(" ").map { it.toInt() }
    val house = Array(n) {
        readLine().toInt()
    }

    house.sort()
    var start = 1
    var end = house[n-1] - house[0]
    var answer = 0

    while (start <= end) {
        val mid = (start + end) / 2
        var current = house[0]
        var count = 1

        for (i in 1 until n) {
            if (house[i]  - current >= mid) {
                current = house[i]
                count += 1
            }
        }

        if (count >= c) {
            answer = mid
            start = mid + 1
        } else {
            end = mid - 1
        }
    }
    println(answer)
    close()
}