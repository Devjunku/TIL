package `20058_마법사 상어와 토네이도`

import java.io.BufferedReader
import java.io.InputStreamReader
import kotlin.math.pow

lateinit var arr: Array<IntArray>

fun main() = with(BufferedReader(InputStreamReader(System.`in`))) {
    val (N, Q) = readLine()
        .split(" ")
        .map {
            it.toInt()
        }
    arr = Array(2.0.pow(N).toInt()) {
        readLine().split(" ").map { it.toInt() }.toIntArray()
    }

    val QList = readLine()
        .split(" ")
        .map {
            it.toInt()
        }
        .toIntArray()
}