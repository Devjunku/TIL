package `카드 게임(retry)`

import java.io.BufferedReader
import java.io.InputStreamReader

fun main() = with(BufferedReader(InputStreamReader(System.`in`))) {
    val testCaseNum = readLine().toInt()
    var sb = StringBuilder()
    for (testCase in 0 until testCaseNum) {
        val n = readLine().toInt()
        val carArr = readLine().split(" ").map { it.toInt() }.toIntArray()
        var left = 0
        var right = n-1

        var gu = 0
        var mu = 0

        while (left < right) {
            if (carArr[left] < carArr[right]) {
                gu += carArr[right]
                right -= 1
            } else  {
                gu += carArr[left]
                left += 1
            }

            if ( left == right ) {
                mu += carArr[left]
                break
            }

            if (carArr[left] < carArr[right]) {
                mu += carArr[right]
                right -= 1
            } else  {
                mu += carArr[left]
                left += 1
            }
        }
        if (gu > mu) {
            sb.append("${gu}\n")
        } else {
            sb.append("${mu}\n")
        }
    }
    println(sb)
}