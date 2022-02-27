package `순서쌍의 곱의 합`

import java.io.BufferedReader
import java.io.InputStreamReader

fun main() = with(BufferedReader(InputStreamReader(System.`in`))) {
    val n = readLine().toInt()
    val arr = readLine().split(" ").map { it.toInt() }
    val cumArr = IntArray(n)
    cumArr[0] = arr[0]
    for (i in 1 until n) {
        cumArr[i] = cumArr[i-1] + arr[i]
    }
    var answer: Long = 0
    for (i in 0 until n-1) {
        answer += ((cumArr[n-1].toLong()-cumArr[i].toLong())*arr[i].toLong())
    }
    print(answer)
    close()
}