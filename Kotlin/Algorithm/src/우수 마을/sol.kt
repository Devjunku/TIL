package `우수 마을`

import java.io.BufferedReader
import java.io.InputStreamReader
import java.lang.Math.max

fun main() = with(BufferedReader(InputStreamReader(System.`in`))) {
    val n = readLine().toInt()

    val cost = IntArray(1) {0} + readLine().split(" ").map{ it.toInt() }.toIntArray()

    val visited = BooleanArray(n+1) { false }

    val dp = Array(n+1) { r ->
        arrayOf(0, cost[r])
    }

    val g = Array<MutableList<Int>>(n+1) { mutableListOf() }

    for (i in 0 until n-1) {
        val (v, u) = readLine().split(" ").map { it.toInt() }
        g[v].add(u)
        g[u].add(v)
    }


    fun dfs(cur: Int) {
        visited[cur] = true
        for (u in g[cur]) {
            if (!visited[u]) {
                dfs(u)
                dp[cur][1] += dp[u][0]
                dp[cur][0] += max(dp[u][0], dp[u][1])
            }
        }
    }
    dfs(1)
    println(max(dp[1][1],dp[1][0]))
}