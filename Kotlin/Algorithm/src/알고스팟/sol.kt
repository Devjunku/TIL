package 알고스팟

import java.io.BufferedReader
import java.io.InputStreamReader

private val dx = arrayOf(0, 1, 0, -1)
private val dy = arrayOf(1, 0, -1, 0)

fun main() = with(BufferedReader(InputStreamReader(System.`in`))) {

    val (n, m) = readLine().split(" ").map { it.toInt() }
    val room = Array(m) {
        IntArray(n)
    }

    for (i in 0 until m) {
        val str = readLine().trim()
        for (j in 0 until n) {
            room[i][j] = str[j].digitToInt()
        }
    }

    val visited = Array(m) {
        IntArray(n) {-1}
    }

    visited[0][0] = 0

    val deque = ArrayDeque<Node>()
    deque.addFirst(Node(0, 0))

    while (deque.isNotEmpty()) {

        val x = deque.first().x
        val y = deque.first().y
        deque.removeFirst()

        for (i in 0 until 4) {
            val nx = x + dx[i]
            val ny = y + dy[i]

            if (nx in 0 until m && ny in 0 until n) {
                if (visited[nx][ny] == -1) {
                    if (room[nx][ny] == 0) {
                        visited[nx][ny] = visited[x][y]
                        deque.addFirst(Node(nx, ny))
                    } else {
                        visited[nx][ny] = visited[x][y] + 1
                        deque.addLast(Node(nx, ny))
                    }
                }
            }
        }
    }
    println(visited[m-1][n-1])
    close()
}

data class Node(val x: Int, val y: Int)