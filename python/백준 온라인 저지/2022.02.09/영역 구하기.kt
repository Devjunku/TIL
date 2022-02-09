import java.io.BufferedReader
import java.io.InputStreamReader

private lateinit var visited: Array<BooleanArray>
private lateinit var arr: Array<IntArray>
private var cnt: Int = 1
private val dx = arrayOf(0, 1, -1, 0)
private val dy = arrayOf(1, 0, 0, -1)
private var nx: Int = 0
private var ny: Int = 0

fun main(args: Array<String>) = with(BufferedReader(InputStreamReader(System.`in`))) {
    val (n, m, k) = readLine().split(" ").map{ it.toInt() }
    arr = Array(n) { IntArray(m) { 0 } }
    visited = Array(n) { BooleanArray(m) {false} }
    for (i in 1 until k+1) {
        var (x1, y1, x2, y2) = readLine().split(" ").map{ it.toInt() }
        for (x in x1 until x2) {
            for (y in y1 until y2) {
                arr[y][x] = -1
            }
        }
    }
    
    var answer: MutableList<Int> = mutableListOf()
    for (i in 0 until n) {
        for (j in 0 until m) {
            if (!visited[i][j] && arr[i][j] == 0) {
                cnt = 1
                dfs(i, j, n, m)
                answer.add(cnt)
            }
        }
    }
    answer.sort()
    var sb = StringBuilder()
    for (i in 0 until answer.size) {
        sb.append("${answer[i]} ")
    }
    println(answer.size)
    println(sb)
}

fun dfs(x: Int, y: Int, n: Int, m: Int) {
    visited[x][y] = true

    for (i in 0 until 4) {
        nx = x + dx[i]
        ny = y + dy[i]
        if (nx in 0 until n && ny in 0 until m) {
            if (!visited[nx][ny] && arr[nx][ny] != -1) {
                cnt += 1
                dfs(nx, ny, n, m)
            }
        }
    }
}