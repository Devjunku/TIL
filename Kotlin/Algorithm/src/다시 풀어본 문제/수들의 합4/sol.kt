package `다시 풀어본 문제`.`수들의 합4`

import java.io.BufferedReader
import java.io.InputStreamReader

fun main() = with(BufferedReader(InputStreamReader(System.`in`))) {
    val (n, k) = readLine().split(" ").map { it.toInt() }
    val numberArr = readLine().split(" ").map { it.toLong() }.toLongArray()
    for (i in 1 until n) {
        numberArr[i] += numberArr[i-1]
    }

    val hashTable = mutableMapOf<Long, Long>()
    var count: Long = 0

    for (i in 0 until n) {
        if (numberArr[i] == k.toLong()) {
            count ++
        }
        count += hashTable.getOrDefault((numberArr[i]-k), 0)
        hashTable[numberArr[i]] = hashTable.getOrDefault(numberArr[i], 0) + 1
    }
    println(count)
}