import kotlin.collections.ArrayList

fun main() {
//    println(integerTriangle([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))
}

fun integerTriangle(triangle: ArrayList<IntArray>): Int {
    for (i in 1 until triangle.size) {
        for (j in 0 until i + 1) {
            when {
                j == 0 -> triangle[i][j] += triangle[i - 1][j]
                i == j -> triangle[i][j] += triangle[i - 1][j - 1]
                else -> triangle[i][j] += maxOf(triangle[i - 1][j], triangle[i - 1][j - 1])
            }
        }
    }
    return triangle[triangle.size].maxOf { it }
}