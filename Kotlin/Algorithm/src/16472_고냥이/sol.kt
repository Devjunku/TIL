package `16472_고냥이`

import java.io.BufferedReader
import java.io.InputStreamReader
import kotlin.math.max

fun main() = with(BufferedReader(InputStreamReader(System.`in`))) {
    val N = readLine().toInt()
    val catLang = readLine().toCharArray()

    val alphabetArr = arrayOf('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')
    val catLangLen = catLang.size
    var left = 0
    var right = 0
    var answer = 0
    var catLangDic = mutableMapOf<Char, Int>()
    for (alphabet in alphabetArr) {
        catLangDic[alphabet] = 0
    }
    var catLangSet = mutableSetOf(catLang[0])

    while (left <= right && right < catLangLen) {
        if (catLangSet.size <= N) {
            var value = 0
            for (k in catLangDic) {
                value += k.value
            }
            answer = max(answer, value)
            right += 1

            if (right < catLangLen) {
                catLangDic[catLang[right]]?.plus(1)
                catLangSet.add(catLang[right])
            }
        } else {
            if (left < catLangLen) {
                catLangDic[catLang[left]]?.plus(-1)
                if (catLangDic[catLang[left]] == 0) {
                    catLangSet.remove(catLang[left])
                }
                left -= 1
            }
        }
    }
    println(answer)
}