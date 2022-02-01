import java.io.BufferedReader
import java.io.InputStreamReader
import kotlin.math.abs
import kotlin.math.max

fun main(args: Array<String>) = with(BufferedReader(InputStreamReader(System.`in`))) {
    val n = readLine().toInt()
    val arr = readLine().split(" ").map { it.toInt() }.toIntArray()
    val visited = BooleanArray(n)
    var answer = 0

    fun permutation(len: Int, result: IntArray, n: Int, arr:IntArray, visited:BooleanArray) {
        if(len == n) {
            var sum = 0
            for (i in 0 until n-1) {
                sum += abs(result[i]-result[i+1])
            }
            answer = max(answer, sum)
            return
        }

        for (i in 0 until n) {
            if (visited[i]) continue
            result[len] = arr[i]
            visited[i] = true
            permutation(len+1, result, n, arr, visited)
            visited[i] = false
        }
    }

    permutation(0, IntArray(n), n, arr, visited)
    println(answer)
}

