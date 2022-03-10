package `원석이와 후니와 함께하는 알고리즘`.`3월3일`.`수들의 합 4`

import java.io.BufferedReader
import java.io.InputStreamReader

fun main() = with(BufferedReader(InputStreamReader(System.`in`))) {
    val (n, k) = readLine().split(" ").map { it.toLong() }
    val arr = readLine().split(" ").map { it.toLong() }.toLongArray()
    val table = mutableMapOf<Long, Long>()
    var count: Long = 0

    for (i in 1 until n) {
        arr[i.toInt()] += arr[(i-1).toInt()]
    }

    for (i in 0 until n) {

        if (arr[i.toInt()] == k) {
            count ++
        }
        count += table.getOrDefault(arr[i.toInt()]-k, 0)
        table[arr[i.toInt()]] = table.getOrDefault(arr[i.toInt()], 0) + 1

    }
    println(count)
}