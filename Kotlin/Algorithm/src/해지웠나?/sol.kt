package `해지웠나?`

import java.io.BufferedReader
import java.io.InputStreamReader

fun main() = with(BufferedReader(InputStreamReader(System.`in`))) {
    val string = readLine().toString().split("")
    println(string)
}