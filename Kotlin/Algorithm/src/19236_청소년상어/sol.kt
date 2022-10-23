package `19236_청소년상어`

import java.io.BufferedReader
import java.io.InputStreamReader
import kotlin.math.max


var answer = 0
val dx = arrayOf(-1, -1, 0, 1, 1, 1, 0, -1)
val dy = arrayOf(0, -1, -1, -1, 0, 1, 1, 1)

fun main() = with(BufferedReader(InputStreamReader(System.`in`))) {
    val bowl = Array(4) {
        val data = readLine().split(" ").map { it.toInt() }.toIntArray()

        val fish = MutableList(4) {
            mutableListOf<Int>()
        }
        for (j in 0 until 8 step 2) {
            fish[it].add(data[j])
            fish[it].add(data[j+1]-1)
        }
        fish
    }

    solution(0, 0, 0, bowl)
    println(answer)
}

fun solution(sx: Int, sy: Int, eatingScore: Int, bowl: Array<MutableList<MutableList<Int>>>) {
    val eatingScoreCopy = eatingScore + bowl[sx][sy][0]
    println(eatingScoreCopy)
    bowl[sx][sy][0] = 0
    answer = max(answer, eatingScoreCopy)
    val cBowl = bowl
    for (fishNumber in 1..16) {
        var fishX = -1
        var fishY = -1

        for (i in 0 until 4) {
            for (j in 0 until 4) {
                if (cBowl[sx][sy][0] == fishNumber) {
                    fishX = i
                    fishY = j
                    break
                }
            }
            if (fishX != -1 && fishY != -1) break
        }

        if (fishX == -1 && fishY == -1) continue

        val cd =  cBowl[sx][sy][1]
        for (i in 0 until 8) {
            val nd = (cd + i) % 8
            val nx = fishX + dx[nd]
            val ny = fishY + dy[nd]

            if (!(nx in 0 until 4 && ny in 0 until 4) || (nx == sx && ny == sy)) continue

            cBowl[fishX][fishY][1] = nd
            val temp = cBowl[fishX][fishY]
            cBowl[fishX][fishY] = cBowl[nx][ny]
            cBowl[nx][ny] = temp
            break
        }
    }
    val sharkD = cBowl[sx][sy][1]
    var sharkCurrentX = sx
    var sharkCurrentY = sy
    for (i in 0 until 4) {
        sharkCurrentX += dx[sharkD]
        sharkCurrentY += dy[sharkD]
        if (!(sharkCurrentX in 0 until 4 && sharkCurrentY in 0 until 4)) break
        if (cBowl[sharkCurrentX][sharkCurrentX][0] == 0) continue

        solution(sharkCurrentX, sharkCurrentX, eatingScoreCopy, cBowl)
    }
}
