import java.util.*

fun main() {
    val sc = Scanner(System.`in`)
    val n = sc.nextInt()

    val dp = IntArray(1000001){0}
    dp[0] = 0
    dp[1] = 0
    for (i in 2 until 1000001) {
        if (i % 6 == 0) {
            dp[i] = minOf(dp[i/2]+1, dp[i/3]+1, dp[i-1]+1)
        } else if (i % 3 == 0) {
            dp[i] = minOf(dp[i/3]+1, dp[i-1]+1)
        } else if (i % 2 == 0) {
            dp[i] = minOf(dp[i/2]+1, dp[i-1]+1)
        } else {
            dp[i] = dp[i-1] + 1
        }
    }
    println(dp[n])
}