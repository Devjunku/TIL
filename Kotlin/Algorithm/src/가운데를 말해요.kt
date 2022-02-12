import java.io.BufferedReader
import java.io.InputStreamReader
import java.util.*

fun main() = with(BufferedReader(InputStreamReader(System.`in`))) {

    val n = readLine().toInt()
    var number: Short
    var tmp: Short
    var sb = StringBuilder()
    var minHeap = PriorityQueue<Short> {o1, o2 -> o1 - o2}
    var maxHeap = PriorityQueue<Short> {o1, o2 -> o2 - o1}

    for (i in 1 until n+1) {
        number = readLine().toShort()
        when {
            minHeap.size == maxHeap.size -> maxHeap.offer(number)
            else -> minHeap.offer(number)
        }

        when { minHeap.isNotEmpty() && maxHeap.isNotEmpty() -> {
                if (minHeap.peek() < maxHeap.peek()) {
                    tmp = minHeap.poll()
                    minHeap.offer(maxHeap.poll())
                    maxHeap.offer(tmp)
                }
            }
        }
        sb.append("${maxHeap.peek()}\n")
    }
    println(sb)
}