package 음양더하기

class Solution {
    fun solution(absolutes: IntArray, signs: BooleanArray): Int {
        val intSigns = signs.map { if (it) 1 else -1 }.toIntArray()
        return absolutes.zip(intSigns).map { it.first * it.second }.sum()
    }
}



