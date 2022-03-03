package 로프

import java.io.BufferedReader
import java.io.InputStreamReader

fun main() = with(BufferedReader(InputStreamReader(System.`in`))) {
    val n = readLine().toInt()
    val arr = IntArray(n) {
        element -> readLine().toInt()
    }
    arr.sort()

    var maxValue = 0

    for (idx in 0 until n) {
        if (arr[idx]*(n-idx) > maxValue) {
            maxValue = arr[idx]*(n-idx)
        }
    }
    println(maxValue)
}