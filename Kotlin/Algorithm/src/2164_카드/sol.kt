package `2164_카드`

import java.io.BufferedReader
import java.io.InputStreamReader
import java.util.LinkedList
import java.util.Queue

fun main() = with(BufferedReader(InputStreamReader(System.`in`))) {

    var n = readLine().toInt()
    var q: Queue<Int> = LinkedList()
    for (i in 1 until n+1) {
        q.offer(i)
    }
    var number = 0
    while ( n > 1) {
        number = q.poll()
        n -= 1
        number = q.poll()
        q.offer(number)
    }

    number = q.poll()
    println(number)
}