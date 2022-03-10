package `원석이와 후니와 함께하는 알고리즘`.`3월7일`.돌게임1

import java.io.BufferedReader
import java.io.InputStreamReader

fun main() = with(BufferedReader(InputStreamReader(System.`in`))) {
    var n = readLine().toInt()

    when {
        n % 2 == 1 -> println("CY")
        else -> println("SK")
    }
    close()
}