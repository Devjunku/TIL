package `2263_트리의 순회`

import java.io.BufferedReader
import java.io.InputStreamReader

private lateinit var inOrder: IntArray
private lateinit var postOrder: IntArray
private lateinit var position: Array<Int>

fun main() = with(BufferedReader(InputStreamReader(System.`in`))) {

    val n = readLine().toInt()
    inOrder = readLine().split(" ").map { it.toInt() }.toIntArray()
    postOrder = readLine().split(" ").map { it.toInt() }.toIntArray()

    position = Array(n+1) { 0 }

    for (i in 0 until n) {
        position[inOrder[i]] = i
    }
    preOrder(0, n-1, 0, n-1)
}

private fun preOrder(inStart: Int, inEnd: Int, postStart: Int, postEnd: Int) {
    if (inStart > inEnd || postStart > postEnd) return

    val parents = postOrder[postEnd]
    print("$parents ")

    val left = position[parents] - inStart
    val right = inEnd - position[parents]

    preOrder(inStart, inStart+left-1, postStart, postStart+left-1)
    preOrder(inEnd-right+1, inEnd, postEnd-right, postEnd-1)

}

private class Solution(
    n: Int,
    inOrder: IntArray,
    postOrder: IntArray
) {

    val _n: Int
    val _inOrder: IntArray
    val _postOrder: IntArray
    val position: IntArray

    init {
        _n = n
        _inOrder = inOrder
        _postOrder = postOrder
        position = IntArray(_n+1) { 0 }
    }

    fun fullPosition() {
        for (i in 0 until _n) {
            position[_inOrder[i]] = i
        }
    }

    fun solution(inStart: Int, inEnd: Int, postStart: Int, postEnd: Int) {
        if (inStart > inEnd || postStart > postEnd) return

        val parents = _postOrder[postEnd]
        print("$parents ")

        val left = position[parents] - inStart
        val right = inEnd - position[parents]

        solution(inStart, inStart+left-1, postStart, postStart+left-1)
        solution(inEnd-right+1, inEnd, postEnd-right, postEnd-1)
    }
}