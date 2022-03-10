package `원석이와 후니와 함께하는 알고리즘`.`3월3일`.동전1

import java.io.BufferedReader
import java.io.InputStreamReader

fun main() = with(BufferedReader(InputStreamReader(System.`in`))) {
    val (n, k) = readLine().split(" ").map { it.toInt() }
    val coinSet = Array(n) {
        readLine().toInt()
    }

    val dp = Array(k+1) {0}
    dp[0] = 1

    for (coin in coinSet) {
        for (i in 1 until k+1) {
            if (i - coin >= 0) {
                dp[i] += dp[i-coin]
            }
        }
    }
    println(dp[k])
    close()
}