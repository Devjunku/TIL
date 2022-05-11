package `1285_동전 뒤집기`

import java.io.BufferedReader
import java.io.InputStreamReader

fun main() = with(BufferedReader(InputStreamReader(System.`in`))) {
    val n = readLine().toInt()

    val arr = Array(n) { r ->
        readLine().toCharArray()
    }

    arr.forEach {
        println(it)
    }


}