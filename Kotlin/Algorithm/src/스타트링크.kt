import java.io.BufferedReader
import java.io.InputStreamReader
import java.util.*

private lateinit var visited: BooleanArray

fun main() = with(BufferedReader(InputStreamReader(System.`in`))) {
    val (F, S, G, U, D) = readLine().split(" ").map { it.toInt() }
    visited = BooleanArray(F+1) { false }
    when (val answer = canGoToStartLink(U, D, S, G, F)) {
        -1 -> println("use the stairs")
        else -> println(answer)
    }
    close()
}

fun canGoToStartLink(up: Int, down: Int, start: Int, gone: Int, end: Int): Int {
    var queue: Queue<NowLoc> = LinkedList()
    queue.add(NowLoc(start, 0))
    visited[start] = true

    while (queue.isNotEmpty()) {
        var stair = queue.peek().stair
        var count = queue.peek().count
        queue.poll()

        if (stair == gone) return count

        if (stair + up <= end) {
            if (!visited[stair + up]) {
                queue.add(NowLoc(stair + up, count + 1))
                visited[stair + up] = true
            }
        }

        if (stair - down >= 1) {
            if (!visited[stair - down]) {
                queue.add(NowLoc(stair - down, count + 1))
                visited[stair - down] = true
            }
        }
    }
    return -1
}

data class NowLoc(val stair: Int, val count: Int)