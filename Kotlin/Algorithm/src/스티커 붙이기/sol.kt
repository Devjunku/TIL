package `스티커 붙이기`

import java.io.BufferedReader
import java.io.InputStreamReader

private lateinit var notebook: Array<IntArray>
private lateinit var sticker: Array<IntArray>

fun main() = with(BufferedReader(InputStreamReader(System.`in`))) {

    val (Y, X, k) = readLine().split(" ").map { it.toInt() }
    notebook = Array(Y) { IntArray(X) {0} }

    for (testcase in 0 until k) {
        val (y, x) = readLine().split(" ").map { it.toInt() }
        sticker = Array(y) {
            readLine().split(" ").map { it.toInt() }.toIntArray()
        }
        var chk = false
        var count = 0

        while (count < 4) {
            if (chk) {
                break
            }

            for (i in 0 until Y - sticker.size + 1) {
                if (chk) {
                    break
                }

                for (j in 0 until X - sticker[0].size + 1) {
                    if (checking(sticker, i, j)) {
                        attach(sticker, i, j)
                        chk = true
                        break
                    }
                }
            }
            sticker = rotate90(sticker)
            count += 1
        }

    }
    var answer = 0

    for (i in 0 until Y) {
        for (j in 0 until X) {
            answer += notebook[i][j]
        }
    }

    println(answer)
    close()
}

private fun checking(sticker: Array<IntArray>, i:Int, j:Int): Boolean {
    for (sy in sticker.indices) {
        for (sx in sticker[0].indices) {
            if (notebook[i+sy][j+sx] + sticker[sy][sx] > 1) {
                return false
            }
        }
    }
    return true
}

private fun attach(sticker: Array<IntArray>, i: Int, j: Int) {
    for (sy in sticker.indices) {
        for (sx in sticker[0].indices) {
            notebook[i+sy][j+sx] += sticker[sy][sx]
        }
    }
    return
}

private fun rotate90(arr:Array<IntArray>) : Array<IntArray> {
    val n = arr.size
    val m = arr[0].size

    val result = Array(m) { IntArray(n) { 0 } }

    for (i in 0 until n) {
        for (j in 0 until m) {
            result[j][n-i-1] = arr[i][j]
        }
    }
    return result
}

