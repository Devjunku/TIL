package `다시 풀어본 문제`.완전이진트리9934



import java.io.BufferedReader
import java.io.InputStreamReader

private lateinit var arr: MutableList<Int>
private lateinit var answer: Array<MutableList<Int>>

fun main(args: Array<String>) = with(BufferedReader(InputStreamReader(System.`in`))) {
    val k = readLine().toInt()
    arr = readLine().split(" ").map { it.toInt() }.toMutableList()
    answer = Array(k) { mutableListOf() }
    treeCurcuit(arr, 0)

    var sb = StringBuilder()

    answer.forEach {
        sb.append("${it.joinToString(" ")}\n")
    }
    println(sb)
}

private fun treeCurcuit(arr: List<Int>, num: Int) {
    if (arr.size == 1) {
        answer[num].add(arr[0])
        return
    }

    var length = arr.size
    var mid = length / 2
    answer[num].add(arr[mid])

    treeCurcuit(arr.subList(0, mid), num+1)
    treeCurcuit(arr.subList(mid+1, arr.size), num+1)
}