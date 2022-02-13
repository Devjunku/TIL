import java.io.BufferedReader
import java.io.InputStreamReader

fun main() = with(BufferedReader(InputStreamReader(System.`in`))) {
    val testCaseNum = readLine().toInt()

    var arrayElementNumber: Int
    var array: IntArray

    for (testCase in 0 until testCaseNum) {
        arrayElementNumber = readLine().toInt()
        array = readLine().split(" ").map { it.toInt() }.toIntArray()

        for ( elementNumber in 1 until arrayElementNumber ) {
            array[elementNumber] += array[elementNumber-1]
        }

        var maxNumber: Int = array.maxOrNull()!!

        for (interval in 1 until arrayElementNumber+1) {
            for (start in 0 until arrayElementNumber-interval) {
                maxNumber = maxOf(maxNumber, array[start+interval] - array[start])
            }
        }
        println(maxNumber)
    }
}