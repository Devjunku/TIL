import java.io.BufferedReader
import java.io.InputStreamReader
import java.util.*

fun main() = with(BufferedReader(InputStreamReader(System.`in`))) {
    val t = readLine().toInt()
    val intMax: Long = 2100000000
    val dpMin = LongArray(101) { intMax }
    val count = arrayOf(6, 2, 5, 5, 4, 5, 6, 3, 7, 6)
    var queue: Queue<matchQueue> = LinkedList()

    for (i in 1 until 10) queue.add(matchQueue(i.toLong(), count[i]))

    while (queue.isNotEmpty()) {
        var cnt = queue.peek().cnt
        var make = queue.peek().make
        queue.poll()
        dpMin[cnt] = minOf(dpMin[cnt], make)

        if (dpMin[cnt] != make) continue

        for (i in 0 until 10) {
            if (cnt + count[i] <= 100) {
                queue.add(matchQueue((make.toString() + i.toString()).toLong(), cnt + count[i]))
            }
        }
    }
    for (testCase in 0 until t) {
        var p = readLine().toInt()
        var maxString: String
        var one = ""
        when {
            p % 2 == 1 -> {
                for (i in 0 until (p - 3) / 2) one = "${one}1"
                maxString = "7$one"
            }
            else -> {
                for (i in 0 until (p) / 2) one = "${one}1"
                maxString = one
            }
        }
        println("${dpMin[p]} $maxString\n")
    }
}

data class matchQueue(val make: Long, val cnt: Int)