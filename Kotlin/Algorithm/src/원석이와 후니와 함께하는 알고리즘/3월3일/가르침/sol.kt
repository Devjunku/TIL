package `원석이와 후니와 함께하는 알고리즘`.`3월3일`.가르침

import java.io.BufferedReader
import java.io.InputStreamReader
import java.lang.Integer.max

private var alphabetTable = mutableMapOf(
    'a' to true,
    'b' to false,
    'c' to true,
    'd' to false,
    'e' to false,
    'f' to false,
    'g' to false,
    'h' to false,
    'i' to true,
    'j' to false,
    'k' to false,
    'l' to false,
    'n' to true,
    'm' to false,
    'o' to false,
    'p' to false,
    'q' to false,
    'r' to false,
    's' to false,
    't' to true,
    'u' to false,
    'v' to false,
    'w' to false,
    'x' to false,
    'y' to false,
    'z' to false
)

private val anotherAlphaKey = arrayOf(
    'b', 'd', 'e', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'o', 'p', 'q', 'r', 's', 'u', 'v', 'w', 'x', 'y', 'z'
)

private var count = 0
private var u: Int = 0

fun main() = with(BufferedReader(InputStreamReader(System.`in`))) {
    val (n, k) = readLine().split(" ").map { it.toInt() }
    val stringArray = Array(n) {
        readLine().trim()
    }

    when {
        k < 5 -> println(0)
        else -> {
            u = k - 5
            canReadWord(0, mutableListOf(), 0, stringArray)
            println(count)
        }
    }
}

private fun canReadWord(n: Int, charList: MutableList<Char>, idx: Int, stringArray: Array<String>) {
    if (n == u) {
        count = max(count, readWord(stringArray))
        return
    }

    if (idx >= anotherAlphaKey.size) return

    for (i in idx until anotherAlphaKey.size) {
        if (alphabetTable[anotherAlphaKey[i]] == false) {
            alphabetTable[anotherAlphaKey[i]] = true
            canReadWord(n+1, charList, i + 1, stringArray)
            alphabetTable[anotherAlphaKey[i]] = false
        }
    }
}

private fun readWord(stringArray: Array<String>): Int {
    var cnt = 0
    var toggle = false

    for (element in stringArray) {
        for (str in element) {
            if (alphabetTable[str] == false) {
                toggle = true
                break
            }
        }
        if (toggle) {
            toggle = false
            continue
        } else {
            cnt += 1
        }
    }
    return cnt
}