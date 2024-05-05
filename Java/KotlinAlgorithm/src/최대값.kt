import java.io.BufferedReader
import java.io.InputStreamReader

fun main() = with(BufferedReader(InputStreamReader(System.`in`))) {
    val arr = IntArray(9) { 0 }
    for (i in 0 until 9) {
        arr[i] = readLine().toInt()
    }

    var answer = arr[0];
    var idx = 0;

    for (i in 0 until arr.size) {
        if (answer < arr[i]) {
            answer = arr[i]
            idx = i
        }
    }
    println(answer)
    println(idx+1)
}