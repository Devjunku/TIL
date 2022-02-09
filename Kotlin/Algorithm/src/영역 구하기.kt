import java.io.BufferedReader
import java.io.InputStreamReader
import java.util.*

private lateinit var visited: Array<BooleanArray>

fun main(args: Array<String>) = with(BufferedReader(InputStreamReader(System.`in`))) {
    val (n, m, k) = readLine().split(" ").map{ it.toInt() }
    val arr: Array<IntArray> = Array(m) { IntArray(n) { 0 } }
    visited = Array(n) { BooleanArray(m) }
    for (i in 1 until k+1) {
        var (x1, y1, x2, y2) = readLine().split(" ").map{ it.toInt() }
        for (x in x1 until x2) {
            for (y in y1 until y2) {
                arr[x][y] += 1
            }
        }
    }
    val answer: MutableList<Int> = mutableListOf()

    for (i in 0 until n) {
        for (j in 0 until m) {
            if (!visited[i][j] && arr[i][j] == 0) {
                answer.add(bfs(arr, i, j, n, m))
            }
        }
    }
    var sb = StringBuilder()
    for (ele in answer) {
        sb.append("$ele ")
    }
    println(answer.size)
    println(sb)
}

fun bfs(array: Array<IntArray>, x: Int, y:Int, n: Int, m: Int): Int {
    var queue: Queue<Points> = LinkedList()
    queue.offer(Points(x, y, 1))

    val dx = arrayOf(0, 1, 0, -1)
    val dy = arrayOf(1, 0, -1, 0)
    var point: Points
    var cx: Int
    var cy: Int
    var number = 1
    var nx: Int
    var ny: Int
    while (queue.isNotEmpty()) {
        point = queue.poll()
        cx = point.xPoint
        cy = point.yPoint
        number = point.num
        for (i in 0 until 4) {
            nx = cx + dx[i]
            ny = cy + dy[i]
            if (nx in 0 until n && ny in 0 until m) {
                if (array[nx][ny] == 0 && !visited[nx][ny]) {
                    queue.offer(Points(nx, ny, number+1))
                    visited[nx][ny] = true
                }
            }
        }
    }
    return number
}

data class Points(val xPoint: Int, val yPoint: Int, val num: Int)