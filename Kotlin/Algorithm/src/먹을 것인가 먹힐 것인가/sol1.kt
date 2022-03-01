package `먹을 것인가 먹힐 것인가`

import java.io.BufferedReader
import java.io.InputStreamReader

fun main() = with(BufferedReader(InputStreamReader(System.`in`))) {
    val testCaseNumber = readLine().toInt()
    var sb = StringBuilder()
    for (t in 0 until testCaseNumber) {
        val (n, m) = readLine().split(" ").map { it.toInt() }
        val nArr = readLine().split(" ").map { it.toInt() }.sorted().toIntArray()
        val mArr = readLine().split(" ").map { it.toInt() }.sorted().toIntArray()

        var ans = 0

        for (na in nArr) {
            ans += binerySearch(mArr, na) + 1
        }

        sb.append("$ans\n")
    }
    println(sb)
    close()
}

fun binerySearch(il: IntArray, a: Int): Int {
    var s = 0
    var e = il.size - 1
    var res = -1
    while (s <= e) {
        val mid = (s+e) / 2

        if (il[mid] < a) {
            res = mid
            s = mid + 1
        } else {
            e = mid - 1
        }
    }
    return res
}