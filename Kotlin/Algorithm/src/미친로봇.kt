import java.io.BufferedReader
import java.io.InputStreamReader

private lateinit var visited: Array<BooleanArray>
private lateinit var direct: Array<Int>
var number: Int = 0
var probability: Double = 0.0
val movingX: Array<Int> = arrayOf(0, 0, 1, -1)
val movingY: Array<Int> = arrayOf(1, -1, 0, 0)
fun main() = with(BufferedReader(InputStreamReader(System.`in`))) {
    val (N, e, w, n, s) = readLine().split(" ").map { it.toInt() }
    number = N
    visited = Array(31) { BooleanArray(31) { false } }
    direct = arrayOf(e, w, n, s)
    visited[15][15] = true
    crazyMoving(0, 1.0, 15, 15)
    println(probability)
}

fun crazyMoving(depth: Int, prob: Double, row: Int, col: Int) {

    if (depth >= number) {
        probability += prob
        return
    }

    for (i in 0 until 4) {
        var nRow = row + movingX[i]
        var nCol = col + movingY[i]
        if (!visited[nCol][nRow] && direct[i] != 0) {
            visited[nCol][nRow] = true
            crazyMoving(depth+1, prob*direct[i]/100, nRow, nCol)
            visited[nCol][nRow] = false
        }
    }
}