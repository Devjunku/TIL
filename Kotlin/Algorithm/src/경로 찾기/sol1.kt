package `경로 찾기`

import java.io.BufferedReader
import java.io.InputStreamReader
import java.util.*

private var vertex = 0
private lateinit var originalMatrix: Array<IntArray>
private lateinit var visitedMatrix: Array<IntArray>
private lateinit var visitedVertex: BooleanArray

fun main() = with(BufferedReader(InputStreamReader(System.`in`))) {
    vertex = readLine().toInt()

    originalMatrix = Array(vertex) { IntArray(vertex) }
    visitedMatrix = Array(vertex) { IntArray(vertex) }
    visitedVertex = BooleanArray(vertex)

    for (i in 0 until vertex) {
        val str = readLine().split(" ")
        for (j in 0 until vertex) {
            originalMatrix[i][j] = (str[j]+"").toInt()
        }
    }

    for (i in 0 until vertex) {
        canGoToVertex(i)
        for (j in 0 until vertex) {
            if (visitedVertex[j]) {
                visitedMatrix[i][j] = 1
            }
        }
        Arrays.fill(visitedVertex, false)
    }

    var sb = StringBuilder()

    for (i in 0 until vertex) {
        for (j in 0 until vertex) {
            sb.append("${visitedMatrix[i][j]} ")
        }
        sb.append("\n")
    }
    println(sb)
}

fun canGoToVertex(startVertex: Int) {
    for (i in 0 until vertex) {
        if (!visitedVertex[i] && originalMatrix[startVertex][i] == 1) {
            visitedVertex[i] = true
            canGoToVertex(i)
        }
    }
}



