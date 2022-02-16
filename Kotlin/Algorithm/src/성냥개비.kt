import java.io.BufferedReader
import java.io.InputStreamReader
import kotlin.math.*

fun main() = with(BufferedReader(InputStreamReader(System.`in`))) {
    val n = readLine().toInt()
    val minDP = LongArray(101) {Long.MAX_VALUE}
    val maxDP = Array<String>(101) { "" }
    val arr = IntArray(8)
    var sb = StringBuilder()

    arr[2] = 1
    arr[3] =7
    arr[4] =4
    arr[5] =2
    arr[6] =0
    arr[7] =8
    minDP[2]=1
    minDP[3]=7
    minDP[4]=4
    minDP[5]=2
    minDP[6]=6
    minDP[7]=8
    minDP[8]=10

    for (i in 9..100) for (j in 2..7) minDP[i] = min(minDP[i], minDP[i-j]*10 + arr[j])

    maxDP[2] = "1"
    maxDP[3] = "7"

    for (i in 4..100) maxDP[i] = maxDP[i-2]+"1"
    for (i in 0 until n) {
        var num = readLine().toInt()
        sb.append("${minDP[num]} ${maxDP[num]}\n")
    }
    println(sb)
    close()
}