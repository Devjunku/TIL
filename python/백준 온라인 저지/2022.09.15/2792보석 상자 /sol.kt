import java.io.BufferedReader
import java.io.InputStreamReader

fun main() = with(BufferedReader(InputStreamReader(System.`in`))) {
    val (n, m) = readLine().split(" ").map { it.toInt() }
    val jy = IntArray(m) { 0 }

    for (i in 0 until m) {
        jy[i] = readLine().toInt()
    }
    println(solution(jy, n))
}

private fun solution(jy: IntArray, target: Int): Int {

    var result = 0
    var start = 1
    var end = jy.maxOrNull()!!

    while (start <= end) {
        val mid = (start + end) / 2
        var count = 0
        for (j in jy) {
            val div = j % mid
            when (div) {
                0 -> count += j / mid
                else -> count += (j/mid + 1)
            }
        }

        if (count > target) {
            start = mid + 1
        } else {
            result = mid
            end = mid - 1
        }
    }
    return result
}