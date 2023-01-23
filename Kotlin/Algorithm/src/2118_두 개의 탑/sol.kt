package `2118_두 개의 탑`

import java.io.BufferedReader
import java.io.InputStreamReader
import java.lang.Integer.max
import java.lang.Integer.min
import kotlin.math.abs

fun main() = with(BufferedReader(InputStreamReader(System.`in`))) {
    val n = readLine().toInt()
    val eachDistance = IntArray(n) { i->
        readLine().toInt() }
    val cumSumEachDistance = IntArray(n+1) { 0 }

    for (i in 1 until n+1) {
        cumSumEachDistance[i] += cumSumEachDistance[i-1] + eachDistance[i-1]
    }
    cumSumEachDistance.forEach {
        print("$it ")
    }
    println()

    val totalSum = cumSumEachDistance.last()

    var idxLeftBef = 0
    var idxRightBef = 1
    var answer = min(cumSumEachDistance[idxRightBef] - cumSumEachDistance[idxLeftBef], totalSum)
    var idxRightNxt: Int
    var idxLeftNxt: Int

    while (true) {
//        println("$idxLeftBef $idxRightBef")

        if (idxRightBef+1 > n-1) idxRightNxt = 0
        else idxRightNxt = idxRightBef + 1

        if (idxLeftBef+1 > n-1) idxLeftNxt = 0
        else idxLeftNxt = idxLeftBef + 1

        val nxtNxt = abs(cumSumEachDistance[idxRightNxt] - cumSumEachDistance[idxLeftNxt])
        val nxtNxtReverse = totalSum - nxtNxt
        val nxtBef = abs(cumSumEachDistance[idxRightNxt] - cumSumEachDistance[idxLeftBef])
        val nxtBefReverse = totalSum - nxtBef

        println("$idxLeftBef $idxRightBef")
        println("$idxLeftBef $idxRightNxt -> ${min(nxtBef, nxtBefReverse)}")
        println("$idxLeftNxt $idxRightNxt -> ${min(nxtNxt, nxtNxtReverse)}")

        answer = max(answer, max(min(nxtNxt, nxtNxtReverse), min(nxtBef, nxtBefReverse)))

        if (min(nxtNxt, nxtNxtReverse) < min(nxtBef, nxtBefReverse)) {
            idxRightBef = idxRightNxt
        } else {
            idxRightBef = idxRightNxt
            idxLeftBef = idxLeftNxt
        }

        println("-----------")

        if (idxRightBef == 1) break
    }

    println(answer)

    /**

     *알고리즘 아이디어*
    1. 반시계와 정시계 중 어느 방향으로 가야 최소거리가 더 긴가? -> 최대값을 바라봄
    2. 직전과 비교했을 때, 최소거리가 축소되는가? -> 이건 의미 없음 최대값만 바라보면 됨

    투 포인터 -> 최소거리, 최대거리

    0 0 -> 0, 15 | 최소거리 0
        0 1 -> 1, 14 | 최소거리 1 (여기를 선택)
        1 1 -> 0, 15 | 최소거리 0

    0 1 -> 1, 14 | 최소거리 1
        0 2 -> 3, 14 | 최소거리 3 (여기를 선택)
        1 2 -> 2, 13 | 최소거리 2

    0 2 -> 3, 11 | 최소거리 3
        0 3 -> 6, 9  | 최소거리 6 (여기를 선택)
        1 3 -> 5, 10 | 최소거리 5

    0 3 -> 6, 9  | 최소거리 6
        0 4 -> 10, 5 | 최소거리 5
        1 4 -> 9, 6  | 최소거리 6 (여기를 선택)

    1 4 -> 9, 6  | 최소거리 6
        1, 0 -> 14, 1 | 최소거리 1
        2, 0 -> 7, 8  | 최소거리 7 (여기를 선택)
    */

}