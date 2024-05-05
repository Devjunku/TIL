package `음식물 피하기`

import java.io.BufferedReader
import java.io.InputStreamReader
import java.util.LinkedList
import java.util.Queue

private lateinit var visited: Array<BooleanArray>
private lateinit var arr: Array<IntArray>

fun main() = with(BufferedReader(InputStreamReader(System.`in`))) {

    val (N, M, K) = readLine().split(" ").map { it.toInt() }

    arr = Array(N) {
        IntArray(M) {0}
    }

    visited =Array(N) {
        BooleanArray(M) { false }
    }

    for (i in 0 until K) {
        val (r, c) = readLine().split(" ").map { it.toInt() }
        arr[r-1][c-1] = 1
    }
    var answer = 1
    for (i in 0 until N) {
        for (j in 0 until M) {
            if (arr[i][j] == 1) {
                val update = bfs(
                    i,
                    j,
                    N,
                    M
                )
                if (answer < update) {
                    answer = update
                }
                println(update)
            }
        }
    }

//    println(answer)

}

private fun bfs(r: Int, c: Int, N: Int, M: Int): Int {

    visited[r][c] = true
    val Q: Queue<PointQ> = LinkedList()
    Q.add(PointQ(r, c))

    var num = 1
    val dx = arrayOf(0, 1, 0, -1)
    val dy = arrayOf(1, 0, -1, 0)

    while (Q.isNotEmpty()) {
        val pointQ = Q.poll()
        val cx = pointQ.x
        val cy = pointQ.x

        for (i in 0 until 4) {
            val nx = cx + dx[i]
            val ny = cy + dy[i]
            if (!(nx in 0 until N && ny in 0 until M)) continue
            if (visited[nx][ny]) continue
            if (arr[nx][ny] == 0) continue

            visited[nx][ny] = true
            Q.add(PointQ(nx, ny))
            num ++
        }
    }
    return num
}

data class PointQ(
    val x: Int,
    val y: Int
)