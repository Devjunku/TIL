import java.io.BufferedReader
import java.io.InputStreamReader

fun main() {
    val br = BufferedReader(InputStreamReader(System.`in`))
    val T = br.readLine().toInt()

    val dp = IntArray(12){0}

    dp[1] = 1
    dp[2] = 2
    dp[3] = 4

    for (i in 4 until 12) {
        dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
    }

    val sb = StringBuilder()
    var n: Int
    for (i in 0 until T) {
        n = br.readLine().toInt()
        sb.append("${dp[n]}\n")
    }
    println(sb)
}