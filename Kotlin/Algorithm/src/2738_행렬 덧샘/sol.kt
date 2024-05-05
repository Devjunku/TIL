package `2738_행렬 덧샘`

import java.io.BufferedReader
import java.io.InputStreamReader
fun main() = with(BufferedReader(InputStreamReader(System.`in`))) {

    val (n, m) = readLine().split(" ").map { it.toInt() }
    val aMatrix = Array(n) { i ->
        readLine().split(" ").map{ it.toInt() }.toIntArray()
    }

    val bMatrix = Array(n) { i ->
        readLine().split(" ").map{ it.toInt() }.toIntArray()
    }

    val andMatrix = Array(n) {
        IntArray(m) { 0 }
    }

    var sb = StringBuilder()
    for (i in 0 until n) {
        for  (j in 0 until m) {
            andMatrix[i][j] = aMatrix[i][j] + bMatrix[i][j]
            sb.append("${andMatrix[i][j]} ")
        }
        sb.append("\n")
    }

    println(sb)
}