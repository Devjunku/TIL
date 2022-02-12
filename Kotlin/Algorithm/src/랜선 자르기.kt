import java.io.BufferedReader
import java.io.InputStreamReader

fun main(args: Array<String>) = with(BufferedReader(InputStreamReader(System.`in`))) {
    val (k, n) = readLine().split(" ").map { it.toLong() }
    val arrInt = LongArray(k.toInt()) {0}

    for (i in 0 until k) arrInt[i.toInt()] = readLine().toLong()

    var left: Long = 1
    var right = arrInt.maxOrNull()!!
    var mid: Long
    var count: Long

    while (left <= right) {

        mid = (left + right) / 2
        count = 0

        for (i in 0 until k) count += (arrInt[i.toInt()] / mid)

        when {
            count < n -> {
                right = mid - 1
            }
            else -> {
                left = mid + 1
            }
        }
    }

    when (left) {
        1.toLong() -> println("$left")
        else -> println("${left - 1}")
    }

    if (left == 1.toLong()) {
        println("$left")
    } else {
        println("${left - 1}")
    }


}