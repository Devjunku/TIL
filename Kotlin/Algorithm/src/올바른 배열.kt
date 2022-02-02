import java.util.*

fun main() = with(Scanner(System.`in`)) {
    val n = nextInt()
    val intArr = IntArray(n)
    for (i in 0 until n) {
        intArr[i] = nextInt()
    }
    intArr.sort()
    var left = 0
    var right = 0
    var cnt = 0
    while (right < n) {
        when {
            intArr[left] + 5 > intArr[right] -> {
                right ++
                cnt ++
            }
            else -> {
                left ++
                right ++
            }
        }

    }
    when {
        cnt > 5 -> println(0)
        else -> println(5-cnt)
    }
}