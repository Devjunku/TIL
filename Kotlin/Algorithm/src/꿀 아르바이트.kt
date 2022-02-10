import java.io.BufferedReader
import java.io.InputStreamReader

fun main(args:Array<String>) = with(BufferedReader(InputStreamReader(System.`in`))) {
    val (n, m) = readLine().split(" ").map { it.toInt() }
    var arr = readLine().split(" ").map { it.toInt() }.toMutableList()
    arr.add(0, 0)
    for (i in 1 until n+1) {
        arr[i] += arr[i-1]
    }
    var max = 0
    for (i in m until n+1) max = maxOf(max, arr[i] - arr[i-m])
    println(max)
}
