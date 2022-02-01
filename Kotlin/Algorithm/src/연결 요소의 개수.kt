import java.io.BufferedReader
import java.io.InputStreamReader

fun main() = with(BufferedReader(InputStreamReader(System.`in`))) {
    val (node, edge) = readLine().split(" ").map {it.toInt()}
    val graph = Array(node + 1) { ArrayList<Int>() }
    val visited = BooleanArray(node+1)
    var answer = 0

    repeat(edge) {
        val (s, e) = readLine().split(" ").map { it.toInt() }
        graph[s].add(e)
        graph[e].add(s)
    }

    fun dfs(now:Int) {
        visited[now] = true
        for (i in graph[now]) {
            when {
                !visited[i] -> dfs(i)
            }
        }
    }

    for (i in 1..node) {
        when {
            !visited[i] -> {
                dfs(i)
                answer ++
            }
        }
    }
    println(answer)
}