import java.io.BufferedReader
import java.io.InputStreamReader

fun main() = with(BufferedReader(InputStreamReader(System.`in`))) {
    val n = readLine().toInt()
    val numberList = readLine().split(" ").map { it.toInt() }.toList().sorted()

    var answer = 0

    for (i in 0 until n) {
        val subList = numberList.subList(0, i) + numberList.subList(i+1, n)

        var start = 0
        var end = subList.size - 1

        while (start < end) {
            val mid = subList[start] + subList[end]

            when {
                numberList[i] < mid -> {
                    end -= 1
                }
                numberList[i] > mid -> {
                    start += 1
                }
                else -> {
                    answer += 1
                    break
                }
            }
        }
    }
    println(answer)
}