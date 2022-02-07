import java.io.BufferedReader
import java.io.InputStreamReader

private lateinit var arr: MutableList<Int>
private lateinit var res: Array<MutableList<Int>>

fun main(args: Array<String>) = with(BufferedReader(InputStreamReader(System.`in`))) {
    val k = readLine().toInt()
    arr = readLine().split(" ").map { it.toInt() }.toMutableList()
    res = Array(k) { mutableListOf(0) }

    fun treeCurcuit(arr: List<Int>, depth: Int) {
        if (arr.size == 1)  {
            res[depth].add(arr[0])
            return
        }

        var length = arr.size
        var mid = length / 2
        res[depth].add(arr[mid])
        treeCurcuit(arr.subList(0,(mid)), depth+1)
        treeCurcuit(arr.subList(mid+1,arr.size), depth+1)
    }
    treeCurcuit(arr, 0)
    var sb = StringBuilder()
    for (ele in res) {
        sb.append("${ele.subList(1, ele.size).joinToString(" ")}\n")
    }
    println(sb)
}