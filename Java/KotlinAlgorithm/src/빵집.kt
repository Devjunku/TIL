import java.io.BufferedReader
import java.io.InputStreamReader

fun main() = with(BufferedReader(InputStreamReader(System.`in`))) {
    val (r, c) = readLine().split(" ").map { it.toInt() }
    val board = Array(r) { i->
        readLine()!!.split("")
    }

    for (i in 0 until r) {
        for (j in 0 until c) {
            println(board[i][j])
        }
    }
}