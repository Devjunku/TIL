import java.io.BufferedReader
import java.io.InputStreamReader

//fun main() {
//    val br = BufferedReader(InputStreamReader(System.`in`))
//    val n = br.readLine()!!.toInt()
//    val arr = br.readLine().split(" ").map { it.toInt() }
//    val delNode = br.readLine()!!.toInt()
//
//    var cnt = 0
//
//    dfs(delNode, arr)
//
//
//
//
//}
//
//private fun dfs(node: Int, arr: Array<Int>) {
//    arr[node] = -2
//    for (i in 0 until arr.size) when {
//        node == arr[i] -> dfs(i, arr)
//    }
//}