import java.io.BufferedReader
import java.io.InputStreamReader

var count: Int = 0
private lateinit var visited: BooleanArray
fun main() = with(BufferedReader(InputStreamReader(System.`in`))) {
    val testCaseNumber = readLine().toInt()
    var sb = StringBuilder()
    for (testCase in 0 until testCaseNumber) {
        var (n, m) = readLine().split(" ").map { it.toInt() }
        var graph: Array<MutableList<Int>> = Array(n+1) { mutableListOf() }

        for (i in 0 until m) {
            var (start, end) = readLine().split(" ").map { it.toInt() }
            graph[start].add(end)
            graph[end].add(start)
        }
        count = 0
        visited = BooleanArray(n+1) { false }
        findCountAirplane(1, graph)
        sb.append("${count}\n")
    }
    println(sb)
}

fun findCountAirplane(startNum: Int, graph: Array<MutableList<Int>>) {
    visited[startNum] = true
    for (nxtNode in graph[startNum]) {
        if (!visited[nxtNode]) {
            count ++
            findCountAirplane(nxtNode, graph)
        }
    }
}