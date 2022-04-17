package `12014주식`

import java.io.BufferedReader
import java.io.InputStreamReader

fun main() = with(BufferedReader(InputStreamReader(System.`in`))) {
    val T = readLine().toInt()
    var sb = StringBuilder()

    for (t in 1 until T+1) {
        val (n, k) = readLine().split(" ").map { it.toInt() }
        val price = readLine().split(" ").map { it.toInt() }.toIntArray()
        val dp = mutableListOf<Int>()
        dp.add(price[0])

        for (i in 1 until n) {
            if (dp.last() < price[i]) {
                dp.add(price[i])
            } else {
                val j = bs(0, dp.size-1, price[i], dp)
                dp[j] = price[i]
            }
        }
        sb.append("Case #${t}\n")

        if (dp.size >= k) {
            sb.append("1\n")
        } else {
            sb.append("0\n")
        }
    }
    println(sb)
}

private fun bs(left: Int, right: Int, target: Int, dp: MutableList<Int>): Int {
    var l = left
    var r = right
    while (l <= r) {
        val mid = (l + r) / 2
        if (dp[mid] < target) {
            l = mid + 1
        } else {
            r = mid - 1
        }
    }
    return l
}