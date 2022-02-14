import java.io.BufferedReader
import java.io.InputStreamReader
import java.util.*

fun main() = with(BufferedReader(InputStreamReader(System.`in`))) {
    var bracketString = readLine().split("").toMutableList()
    var stack = Stack<String>()

    for (bracket in bracketString) {
        when {
            stack.isEmpty() -> stack.push(bracket)
            else -> {
                if (bracket == "(") {
                    stack.push(bracket)
                }
                else {
                    if (stack.peek() == "(" && bracket == ")") {
                        stack.pop()
                    }
                    else {
                        stack.push(bracket)
                    }
                }
            }
        }
    }
    println(stack.size - 2)
}