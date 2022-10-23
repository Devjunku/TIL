package `1976_여행 가자`

import java.io.BufferedReader
import java.io.InputStreamReader
import java.util.*

fun main() = with(BufferedReader(InputStreamReader(System.`in`))) {
    val n = readLine().toInt()
    val m = readLine().toInt()
    val graph = Array<MutableSet<Int>>(n) { mutableSetOf() }

    for (i in 0 until n) {
        val nodeInfo = readLine().split(" ").map { it.toInt() }.toIntArray()
        for (j in 0 until n) {
            if (nodeInfo[j] == 1) {
                graph[i].add(j)
                graph[j].add(i)
            }
        }
    }

    val directory = readLine().split(" ").map { it.toInt() - 1 }.toIntArray()
    val answer = Solution(n, directory, graph)
    println(answer.solution())
}

class Solution(
    private val _n: Int,
    private val _directory: IntArray,
    private val _graph: Array<MutableSet<Int>>
) {
    fun solution(): String {
        val Q: Queue<Int> = LinkedList()
        val visited = Array(_n) {0}

        visited[_directory[0]] = 1
        Q.add(_directory[0])
        while (Q.isNotEmpty()) {
            val nowLoc = Q.poll()
            for (i in _graph[nowLoc]) {
                when (visited[i]) {
                    1 -> continue
                    else -> {
                        visited[i] = 1
                        Q.add(i)
                    }
                }
            }
        }

        var toggle = true
        for (i in _directory) {
            if (visited[i] == 0) {
                toggle = false
                break
            }
        }
        if (toggle) return "YES"
        else return "NO"
    }
}