import java.io.BufferedReader
import java.io.InputStreamReader

private var root = 0
private var idx = 1
private lateinit var r: IntArray
private lateinit var l: IntArray
private lateinit var visited: Array<MutableList<Int>>

fun main() = with(BufferedReader(InputStreamReader(System.`in`))) {

    val n = readLine().toInt()
    r = IntArray(n+1) {-1}
    l = IntArray(n+1) {-1}
    visited = Array(n+1) { mutableListOf() }
    val parent = IntArray(n+1) {-1}

    for (i in 0 until n) {
        val (p, left, right) = readLine().split(" ").map { it.toInt() }
        l[p] = left
        r[p] = right
        if (left != -1) {
            parent[left] = p
        }
        if (right != -1) {
            parent[right] = p
        }
    }
    root = n

    findRoot(parent, 1)
    curcuit(root, 1)

    var level = 1
    var width = 1

    for ((i, v) in visited.withIndex()) {
        if (v.isEmpty()) {
            continue
        }

        if (v.last() - v.first() + 1 > width) {
            width = v.last() - v.first() + 1
            level = i
        }
    }
    println("${level} ${width}")
}

private fun findRoot(parent: IntArray, node: Int) {
    if (parent[node] == -1) {
        root = node
        return
    } else {
        findRoot(parent, parent[node])
    }
}

private fun curcuit(node: Int, start: Int) {
    if (l[node] != -1) {
        curcuit(l[node], start+1)
    }

    visited[start].add(idx)
    idx += 1

    if (r[node] != -1) {
        curcuit(r[node], start+1)
    }
}