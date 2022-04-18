package `청소년 상어`

import java.io.BufferedReader
import java.io.InputStreamReader

fun main() = with(BufferedReader(InputStreamReader(System.`in`))) {
    val bowl = Array(4) { i ->
        val data = readLine().split(" ").map { it.toInt() }.toIntArray()
        Array(4) { j ->
            println("${2*j} ${2*j+1}")
//            arrayOf(data[2*j], data[2*j+1])
        }
    }






//    val bowl = arrayOf(
//        arrayOf(arrayOf(0,0), arrayOf(0,0), arrayOf(0,0), arrayOf(0,0)),
//        arrayOf(arrayOf(0,0), arrayOf(0,0), arrayOf(0,0), arrayOf(0,0)),
//        arrayOf(arrayOf(0,0), arrayOf(0,0), arrayOf(0,0), arrayOf(0,0)),
//        arrayOf(arrayOf(0,0), arrayOf(0,0), arrayOf(0,0), arrayOf(0,0))
//    )
}