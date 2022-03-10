package `다시 풀어본 문제`.`나무 탈출`

import java.io.BufferedReader
import java.io.InputStreamReader

private lateinit var graph: Array<MutableList<Int>>
private lateinit var visited: BooleanArray
private lateinit var distance: IntArray

fun main() = with(BufferedReader(InputStreamReader(System.`in`))) {
    val n = readLine().toInt()
    graph = Array(n+1)  {
        mutableListOf()
    }
    visited = BooleanArray(n+1) { false }
    distance = IntArray(n+1) { 0 }

    for (i in 0 until n-1) {
        val (parent, child) = readLine().split(" ").map { it.toInt() }
        graph[parent].add(child)
        graph[child].add(parent)
    }

    dfs(1)

    var answer = 0
    for (i in 2 until n+1) {
        if (graph[i].size == 1) {
            answer += distance[i]
        }
    }

    when {
        answer % 2 == 1 -> println("Yes")
        else -> println("No")
    }
    close()
}

private fun dfs(node: Int) {
    visited[node] = true
    for (nextNode in graph[node]) {
        if (!visited[nextNode]) {
            distance[nextNode] = distance[node] + 1
            dfs(nextNode)
        }
    }
}