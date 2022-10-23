package `4485녹색 옷 입은 애가 젤다지?`

import java.io.BufferedReader
import java.io.InputStreamReader
import kotlin.math.max

fun main() = with(BufferedReader(InputStreamReader(System.`in`))) {
    val (n, k) = readLine().split(" ").map {
        it.toInt()
    }
    val pail = Array(1000010) { 0 }
    for (i in 0 until n) {
        val (g, x) = readLine().split(" ").map {
            it.toInt()
        }
        pail[x] = g
    }

    var left = 0
    var right = 2 * k

    var answer = sum(left, right, pail)
    var value = sum(left, right, pail)

    while (true) {
        value -= pail[left]
        left += 1; right += 1;

        if (right >= 1000001) break

        value += pail[right]
        answer = max(answer, value)
    }
    println(answer)
    close()
}


private fun sum(left: Int, right: Int, pail: Array<Int>): Int {
    var result = 0
    for (i in left until right+1) {
        result += pail[i]
    }
    return result
}