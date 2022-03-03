package 토마토

import java.io.BufferedReader
import java.io.InputStreamReader
import java.util.LinkedList
import java.util.Queue

private val dx = arrayOf(0, 1, 0, -1)
private val dy = arrayOf(1, 0, -1, 0)

fun main() = with(BufferedReader(InputStreamReader(System.`in`))) {
    val (m, n) = readLine().split(" ").map { it.toInt() }
    var tomatoBox = Array(n) { r ->
        readLine().split(" ").map { it.toInt() }.toIntArray()
    }

    var tomatoDoneLoc: Queue<TomatoLoc> = LinkedList()
    for (i in 0 until n) {
        for (j in 0 until m) {
            if (tomatoBox[i][j] == 1) {
                tomatoDoneLoc.add(TomatoLoc(i, j))
            }
        }
    }


    val newTomatoDoneArr = bfs(tomatoDoneLoc, tomatoBox, n, m)
    if (!isCompleted(newTomatoDoneArr, n, m)) println(-1)
    else println(findMaxValue(newTomatoDoneArr, n, m))

}

private fun isCompleted(tomatoBox: Array<IntArray>, n: Int, m: Int): Boolean {
    for (i in 0 until n) {
        for (j in 0 until m) {
            if (tomatoBox[i][j] == 0) {
                return false
            }
        }
    }
    return true
}

private fun findMaxValue(tomatoBox: Array<IntArray>, n: Int, m: Int): Int {
    var answer = 0
    for (i in 0 until n) {
        for (j in 0 until m) {
            if (tomatoBox[i][j] > answer) {
                answer = tomatoBox[i][j]
            }
        }
    }
    return answer - 1
}


private fun bfs(tomatoDoneLoc: Queue<TomatoLoc>, tomatoBox: Array<IntArray>, n: Int, m: Int): Array<IntArray> {
    while (tomatoDoneLoc.isNotEmpty()) {
        val xLoc = tomatoDoneLoc.peek().xLoc
        val yLoc = tomatoDoneLoc.peek().yLoc
        tomatoDoneLoc.poll()
        for (i in 0 until 4) {
            var nxLoc = xLoc + dx[i]
            var nyLoc = yLoc + dy[i]
            if (nxLoc in 0 until n && nyLoc in 0 until m) {
                if (tomatoBox[nxLoc][nyLoc] == 0) {
                    tomatoBox[nxLoc][nyLoc] = tomatoBox[xLoc][yLoc] + 1
                    tomatoDoneLoc.add(TomatoLoc(nxLoc, nyLoc))
                }
            }
        }
    }
    return tomatoBox
}

data class TomatoLoc(val xLoc: Int, val yLoc: Int)