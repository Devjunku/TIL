import java.io.BufferedReader
import java.io.InputStreamReader
import java.util.*

fun main(args: Array<String>) = with(BufferedReader(InputStreamReader(System.`in`))) {
    var t = readLine().toInt()
    var idx = 0
    var sb = StringBuilder()
    for (i in 0 until t) {
        var passwordTrace = readLine()
        sb.append("${getString(passwordTrace)}\n")
    }
    println(sb)
}

fun getString(input: String): StringBuilder {
    var prefix: Deque<Char> = ArrayDeque()
    var postfix: Deque<Char> = ArrayDeque()

    var stringBuilder = StringBuilder()

    for (i in 0 until input.length) {
        var c: Char = input[i]
        when (c) {
            '<' -> {
                if (prefix.isNotEmpty()) {
                    postfix.addFirst(prefix.pollLast())
                }
            }
            '>' -> {
                if (postfix.isNotEmpty()) {
                    prefix.addLast(postfix.pollFirst())
                }
            }
            '-' -> {
                if (prefix.isNotEmpty()) {
                    prefix.pollLast()
                }
            }
            else -> {
                prefix.add(c)
            }
        }
    }
    while(prefix.isNotEmpty()) {
        stringBuilder.append(prefix.pollFirst())
    }

    while(postfix.isNotEmpty()) {
        stringBuilder.append(postfix.pollFirst())
    }
    return stringBuilder
}