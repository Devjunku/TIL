package `노드사이의 거리`

import java.io.BufferedReader
import java.io.InputStreamReader

var count = 0
private lateinit var graph: Array<MutableList<Array<Int>>>
private lateinit var visited: BooleanArray
fun main() = with(BufferedReader(InputStreamReader(System.`in`))) {
    val (n, m) = readLine().split(" ").map { it.toInt() }
    graph = Array(n+1) { mutableListOf() }
    for (i in 0 until n-1) {
        val (s, e, c) = readLine().split(" ").map { it.toInt() }
        graph[s].add(arrayOf(e, c))
        graph[e].add(arrayOf(s, c))
    }
    var sb = StringBuilder()
    for (i in 0 until m) {
        val (start, end) = readLine().split(" ").map { it.toInt() }
        visited = BooleanArray(n+1) { false }
        visited[start] = true
        count = 0
        findThedist(start, end, 0)
        sb.append("${count}\n")
    }
    println(sb)
    close()
}

private fun findThedist(s: Int, e: Int, dist: Int) {
    if (s == e) {
        count = dist
        return
    }

    for (node in graph[s]) {
        if (!visited[node[0]]) {
            visited[node[0]] = true
            findThedist(node[0], e, dist + node[1])
        }
    }
}