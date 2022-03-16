package 괄호10422

import java.io.BufferedReader
import java.io.BufferedWriter
import java.io.InputStreamReader
import java.io.OutputStreamWriter

val cache = IntArray(2501) { -1 }
private const val MOD = 1000000007
fun main() = with(BufferedReader(InputStreamReader(System.`in`))) {
    val bw = BufferedWriter(OutputStreamWriter(System.out))
    val t = readLine().toInt()
    repeat(t) {
        val input = readLine().toInt()
        when {
            input % 2 == 1 -> bw.append("${0}\n")
            else -> bw.append("${makeDP(input / 2)}\n")
        }
    }
    bw.flush()
    bw.close()
    close()
}

private fun makeDP(n: Int): Int {
    if (n == 0) {
        return 1
    } else if (cache[n] != -1){
        return cache[n]
    }

    var result = 0
    for (i in 0 until n) {
        result += ((makeDP(i).toLong() * makeDP(n-i-1)) % MOD) .toInt()
        result %= MOD
    }
    cache[n] = result
    return result
}
