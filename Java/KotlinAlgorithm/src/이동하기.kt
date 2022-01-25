import java.io.BufferedReader
import java.io.InputStreamReader

fun main() {
    val br = BufferedReader(InputStreamReader(System.`in`))
    val ex = br.readLine().split(" ").map { it.toInt() }
    val n = ex[0] + 1
    val m = ex[1] + 1

    val dp = Array(n){ IntArray(m){0} }

    for (i in 1 until n) {
        var candy = br.readLine().split(" ").map { it.toInt() }
        for (j in 1 until m) {
            dp[i][j] = candy[j-1]
        }
    }

    for (i in 1 until n) {
        for (j in 1 until m) {
            dp[i][j] += maxOf(dp[i-1][j], dp[i][j-1])
        }
    }
    println(dp[n-1][m-1])
}