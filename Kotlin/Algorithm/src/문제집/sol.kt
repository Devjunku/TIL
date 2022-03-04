package 문제집

/**
 * 트리문제임
 */


import java.io.BufferedReader
import java.io.InputStreamReader
import java.util.PriorityQueue

fun main() = with(BufferedReader(InputStreamReader(System.`in`))) {

    val (n, m) = readLine().split(" ").map { it.toInt() }
    val problemList = Array<MutableList<Int>>(n+1) { mutableListOf() }
    val indegree = IntArray(n+1) { 0 }
    var priorityQueue = PriorityQueue<Int>()
    var sb = StringBuilder()

    for (i in 0 until m) {
        val (s, e) = readLine().split(" ").map{ it.toInt() }
        problemList[s].add(e)
        indegree[e] += 1
    }

    for (i in 1 until n+1) {
        if (indegree[i] == 0) {
            priorityQueue.add(i)
        }
    }

    while (priorityQueue.isNotEmpty()) {
        val temp = priorityQueue.poll()
        sb.append("$temp ")
        for (problem in problemList[temp]) {
            indegree[problem] -= 1
            if (indegree[problem] == 0) {
                priorityQueue.add(problem)
            }
        }
    }
    println(sb)
    close()
}