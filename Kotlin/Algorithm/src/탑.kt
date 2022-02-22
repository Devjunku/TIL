import java.io.BufferedReader
import java.io.InputStreamReader
import java.util.Stack

fun main() = with(BufferedReader(InputStreamReader(System.`in`))) {
    val n = readLine().toInt()
    val arr = readLine().split(" ").map { it.toInt() }

    var stack = Stack<StackElement>()
    var sb = StringBuilder()

    for (i in 0 until n) {
        while (stack.isNotEmpty()) {
            when {
                stack.last().value > arr[i] -> {
                    sb.append("${stack.last().index + 1} ")
                    break
                }
                else -> {
                    stack.pop()
                }
            }
        }
        if (stack.isEmpty()) {
            sb.append("${0} ")
        }
        stack.push(StackElement(i, arr[i]))
    }
    println(sb)
}

data class StackElement(val index: Int, val value: Int)