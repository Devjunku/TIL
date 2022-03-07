package `다시 풀어본 문제`.완전이진트리9934

import java.io.BufferedReader
import java.io.InputStreamReader

private lateinit var answer: Array<MutableList<Int>>
fun main() = with(BufferedReader(InputStreamReader(System.`in`))) {
    val k = readLine().toInt()
    val building = readLine().split(" ").map { it.toInt() }.toMutableList()

    answer = Array(k) {
        mutableListOf()
    }

    curcuitTree(building, 0)

    var sb = StringBuilder()

    answer.forEach {
        sb.append("${it.joinToString(" ")}\n")
    }

    println(sb)
    close()
}

private fun curcuitTree(list: List<Int>, n: Int) {
    if (list.size == 1) {
        answer[n].add(list[0])
        return
    }

    val mid = list.size / 2
    answer[n].add(list[mid])
    curcuitTree(list.subList(0, mid), n+1)
    curcuitTree(list.subList(mid+1, list.size), n+1)
}