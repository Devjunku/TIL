package `2206_벽 부수고 이동하기`

import java.io.BufferedReader
import java.io.InputStreamReader
import java.util.*

val dx = arrayOf(0, 1, -1, 0)
val dy = arrayOf(-1, 0, 0, 1)

fun main() = with(BufferedReader(InputStreamReader(System.`in`))) {

    val (N, M) = readLine().split(" ").map { it.toInt() }

    val arr = Array(N) {
        readLine().trim().toCharArray()
    }

    val visited = Array(2) {
        Array(N) {
            BooleanArray(M) { false }
        }
    }

    val Q: Queue<Point> = LinkedList()
    visited[0][0][0] = true
    Q.add(Point(0, 0, 1, 0))

    var answer = 0

    while (Q.isNotEmpty()) {

        val nowX = Q.peek().x
        val nowY = Q.peek().y
        val nowCnt = Q.peek().cnt
        val nowWall = Q.peek().wall
        Q.poll()

        if (nowX == N-1 && nowY == M-1) {
            answer = nowCnt
            break
        }
        for (i in 0 until 4) {
            val nxtX = nowX + dx[i]
            val nxtY = nowY + dy[i]

            if (!( nxtX in 0 until N && nxtY in 0 until M)) continue
            if (nowWall > 1) continue
            if (visited[nowWall][nxtX][nxtY]) continue

            if (arr[nxtX][nxtY] == '0') {
                visited[nowWall][nxtX][nxtY] = true
                Q.add(Point(nxtX, nxtY, nowCnt + 1, nowWall))
                continue
            }

            if (arr[nxtX][nxtY] == '1' && nowWall < 1) {
                visited[nowWall][nxtX][nxtY] = true
                Q.add(Point(nxtX, nxtY, nowCnt + 1, nowWall + 1))
                continue
            }

        }
    }
    if (answer != 0) println(answer)
    else println(-1)
}

data class Point(
    val x: Int,
    val y: Int,
    val cnt: Int,
    val wall: Int
)