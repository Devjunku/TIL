package `다시 풀어본 문제`.알고스팟

import java.io.InputStreamReader
import java.io.BufferedReader

fun main() = with(BufferedReader(InputStreamReader(System.`in`))) {
    val (m, n) = readLine().split(" ").map { it.toInt() }
    val maze = Array(n) {
        readLine().map { it.digitToInt() }
    }

    val visited = Array(n) {
        IntArray(m) {-1}
    }

    val dx = arrayOf(0, 1, 0, -1)
    val dy = arrayOf(1, 0, -1, 0)

    val deque = ArrayDeque<Point>()
    deque.addFirst(Point(0,0))
    visited[0][0] = 0

    while (deque.isNotEmpty()) {
        val x = deque.first().x
        val y = deque.first().y
        deque.removeFirst()

        for (i in 0 until 4) {
            val nx = x + dx[i]
            val ny = y + dy[i]
            if (nx in 0 until n && ny in 0 until m) {
                if (visited[nx][ny] == -1) {
                    if (maze[nx][ny] == 0) {
                        visited[nx][ny] = visited[x][y]
                        deque.addFirst(Point(nx, ny))
                    } else {
                        visited[nx][ny] = visited[x][y] + 1
                        deque.addLast(Point(nx, ny))
                    }
                }
            }
        }
    }
    println(visited[n-1][m-1])
}

data class Point(val x: Int, val y: Int)
