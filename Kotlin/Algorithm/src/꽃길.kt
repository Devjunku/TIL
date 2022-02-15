import java.io.BufferedReader
import java.io.InputStreamReader

private lateinit var lawn: Array<ArrayList<Int>>
private lateinit var visited: Array<BooleanArray>
private var cost = 100000000
private var n: Int = 0
fun main() = with(BufferedReader(InputStreamReader(System.`in`))) {
    n = readLine().toInt()!!
    lawn = Array(n) { ArrayList(n) }
    for (row in 0 until n) {
        lawn[row] = readLine().split(" ").map { it.toInt() } as ArrayList<Int>
    }

    visited = Array(n) { BooleanArray(n) { false } }

    calculateMinCost(lawn, 0, 0)
    println(cost)
}

fun calculateMinCost(lawn: Array<ArrayList<Int>>, cnt: Int, num: Int) {

    if (num == 3) {
        cost = minOf(cost, cnt)
        return
    }

    for(i in 1 until n-1) {
        for (j in 1 until n-1) {
            if (!visited[i][j] && !visited[i-1][j] && !visited[i][j-1] && !visited[i+1][j] && !visited[i][j+1]) {
                visited[i][j] = true
                visited[i-1][j] = true
                visited[i][j-1] = true
                visited[i+1][j] = true
                visited[i][j+1] = true
                calculateMinCost(lawn, cnt + lawn[i][j] + lawn[i-1][j] + lawn[i][j-1] + lawn[i+1][j] + lawn[i][j+1], num+1)
                visited[i][j] = false
                visited[i-1][j] = false
                visited[i][j-1] = false
                visited[i+1][j] = false
                visited[i][j+1] = false
            }
        }
    }
}