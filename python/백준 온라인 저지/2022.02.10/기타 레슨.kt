import java.io.BufferedReader
import java.io.InputStreamReader
import kotlin.collections.maxOrNull as maxOrNull1

fun main(args: Array<String>) = with(BufferedReader(InputStreamReader(System.`in`))) {
    val (n, m) = readLine().split(" ").map { it.toInt() }
    val arr = readLine().split(" ").map { it.toInt() }.toIntArray()

    var start = arr.maxOrNull1()!!
    var end = arr.sum()!!

    var mid: Int
    var cnt: Int
    var pt: Int

    while (start <= end) {
        mid = (start + end) / 2
        cnt = 0
        pt = 0
        for (i in 0 until n) {
            when {
                pt + arr[i] > mid -> {
                    cnt += 1
                    pt = 0
                }
            }
            pt += arr[i]
        }

        cnt += if (pt != 0) 1 else 0
        when {
            cnt <= m -> {
                end = mid - 1
            }
            else -> {
                start = mid + 1
            }
        }
    }
    println(start)
}