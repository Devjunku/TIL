package 주식

import java.io.BufferedReader
import java.io.InputStreamReader

fun main() = with(BufferedReader(InputStreamReader(System.`in`))) {
    val T = readLine().toInt()
    var sb = StringBuilder()
    for (t in 0 until T) {
        val n = readLine().toInt()
        val stock_price = readLine().split(" ").map { it.toInt() }.toIntArray()
        var answer: Long = 0

        var mxV = stock_price[n-1]
        for (i in n-2 downTo 0 ) {
            if (mxV < stock_price[i]) {
                mxV = stock_price[i]
            } else {
                answer += (mxV - stock_price[i]).toLong()
            }
        }
        sb.append("${answer}\n")
    }
    println(sb)
}