//package `81304_미로 탈출`
//
//
//
//fun main() {
//    val sample = Solution()
//    println(sample.solution(3, 1, 3, arrayOf(intArrayOf(1, 2, 3), intArrayOf(3, 2, 3)), intArrayOf(2)))
//}
//
//import java.util.PriorityQueue
//const val INF: Int = 1000000000
//private lateinit var d: Array<IntArray>
//private lateinit var graph: Array<MutableList<Array<Int>>>
//private lateinit var revGraph: Array<MutableList<Array<Int>>>
//private lateinit var trapIdx: IntArray
//
//class Solution {
//
//    fun solution(n: Int, start: Int, end: Int, roads: Array<IntArray>, traps: IntArray): Int {
//
//        graph = Array(1001 ) { mutableListOf() }
//        revGraph = Array(1001) { mutableListOf() }
//        trapIdx = IntArray(1001) {-1}
//        d = Array(1001) {IntArray(1024) {INF}}
//
//        roads.forEach {
//            graph[it[0]].add(arrayOf(it[1], it[2]))
//            revGraph[it[2]].add(arrayOf(it[0], it[2]))
//        }
//
//        for (i in 0 until traps.size) {
//            trapIdx[traps[i]] = i
//        }
//
//        d[start][0] = 0
//        val pq = PriorityQueue<NodeInfo>()
//        pq.add(NodeInfo(d[start][0], start, 0))
//
//        while (pq.isNotEmpty()) {
//            val (v, now, state) = pq.poll()
//            if (d[now][state] != v) continue
//            if (now == end) return v
//
//            for ((nxt, dist) in graph[now]) {
//                var rev = 0
//                if (trapIdx[now] != -1 && bitmask(state, now)) rev xor 1
//                if (trapIdx[nxt] != -1 && bitmask(state, nxt)) rev xor 1
//                if (rev == 1) continue
//
//                var nxt_state = state
//                if (trapIdx[nxt] != -1) nxt_state xor trapIdx[nxt]
//                if (d[nxt][nxt_state] > dist + v) {
//                    d[nxt][nxt_state] = dist + v
//                    pq.add(NodeInfo(d[nxt][nxt_state], nxt, nxt_state))
//                }
//            }
//
//            for ((nxt, dist) in revGraph[now]) {
//                var rev = 0
//                if (trapIdx[now] != -1 && bitmask(state, now)) rev xor 1
//                if (trapIdx[nxt] != -1 && bitmask(state, nxt)) rev xor 1
//                if (rev ==0) continue
//
//                var nxt_state = state
//                if (trapIdx[nxt] != -1) nxt_state xor (1 shl trapIdx[nxt])
//                if (d[nxt][nxt_state] > dist + v) {
//                    d[nxt][nxt_state] = dist + v
//                    pq.add(NodeInfo(d[nxt][nxt_state], nxt, nxt_state))
//                }
//            }
//        }
//        return -1
//    }
//    private fun bitmask(state: Int, idx: Int): Boolean = (1 shl trapIdx[idx]) and state != 0
//}
//
//data class NodeInfo(
//    val dist: Int,
//    val idx: Int,
//    val state: Int
//): Comparable<NodeInfo> {
//    override fun compareTo(other: NodeInfo): Int = dist - other.dist
//}