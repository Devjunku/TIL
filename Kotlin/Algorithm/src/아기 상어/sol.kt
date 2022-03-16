package `아기 상어`

import java.io.BufferedReader
import java.io.InputStreamReader
import java.util.LinkedList
import java.util.Queue

private val dx = arrayOf(0, -1, 0, 1)
private val dy = arrayOf(1, 0, -1, 0)

fun main() = with(BufferedReader(InputStreamReader(System.`in`))) {
    val n = readLine().toInt()
    val fishBowl = Array(n) {
        readLine().split(" ").map { it.toInt() }.toIntArray()
    }

    var sharkSize = 2

    var sharkR = 0
    var sharkC = 0
    for (i in 0 until n) {
        for (j in 0 until n) {
            if (fishBowl[i][j] == 9) {
                sharkR = i
                sharkC = j
                break
            }
        }
    }

    var t = 0
    var eatCount = 0

    while (true) {
        val result = findFeed(sharkSize, sharkR, sharkC, n, fishBowl)
        if (result.dist == -1) {
            println(t)
            break
        }

        t += result.dist

        eatCount += 1
        if (eatCount == sharkSize) {
            eatCount = 0
            sharkSize += 1
        }

        fishBowl[sharkR][sharkC] = 0
        fishBowl[result.x][result.y] = 0
        sharkR = result.x
        sharkC = result.y
    }
}


private fun findFeed(sharkSize: Int, r: Int, c:Int, n: Int, fishBowl: Array<IntArray>): DistRC {

    val visited = Array(n) { BooleanArray(n) { false } }
    val queue: Queue<DistRC> = LinkedList()
    queue.offer(DistRC(0, r, c))

    val canEatList = mutableListOf<DistRC>()

    while (queue.isNotEmpty()) {
        val cx = queue.peek().x
        val cy = queue.peek().y
        val dist = queue.peek().dist
        queue.poll()
        for (i in 0 until 4) {
            val nx = cx + dx[i]
            val ny = cy + dy[i]
            if (nx in 0 until n && ny in 0 until n) {
                if (!visited[nx][ny]) {
                    if (fishBowl[nx][ny] == sharkSize || fishBowl[nx][ny] == 0) {
                        visited[nx][ny] = true
                        queue.offer(DistRC(dist+1, nx, ny))
                    } else if (fishBowl[nx][ny] < sharkSize) {
                        visited[nx][ny] = true
                        canEatList.add(DistRC(dist+1, nx, ny))
                        queue.offer(DistRC(dist+1, nx, ny))
                    }
                }
            }
        }
    }

    canEatList.sortWith(compareBy<DistRC>{ it.dist }.thenBy { it.x }.thenBy { it.y })

    if (canEatList.isNotEmpty()) {
        return canEatList[0]
    } else {
        return DistRC(-1, -1, -1)
    }
}

data class DistRC(
    val dist: Int,
    val x: Int,
    val y: Int
)