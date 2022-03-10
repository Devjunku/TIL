package `나무 탈출`

import java.io.BufferedReader
import java.io.InputStreamReader

private lateinit var graph: Array<MutableList<Int>>
private lateinit var visited: BooleanArray
private lateinit var distance: IntArray

fun main() = with(BufferedReader(InputStreamReader(System.`in`))) {
    val n = readLine().toInt()
    graph = Array(n+1) { mutableListOf() }

    for (i in 0 until n-1) {
        val (x, y) = readLine().split(" ").map { it.toInt() }
        graph[x].add(y)
        graph[y].add(x)
    }

    visited = BooleanArray(n+1) { false }
    distance = IntArray(n+1) { 0 }

    dfs(1)
    var ans = 0
    for (i in 2 until n+1) {
        if (graph[i].size == 1) {
            ans += distance[i]
        }
    }
    when {
        ans % 2 == 1 -> println("Yes")
        else -> println("No")
    }
    close()
}


private fun dfs(c: Int) {
    visited[c] = true
    for (nxt in graph[c]) {
        if (!visited[nxt]) {
            distance[nxt] = distance[c] + 1
            dfs(nxt)
        }
    }
}