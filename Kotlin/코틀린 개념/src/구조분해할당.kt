data class Tuple(
    val a: Int,
    val b: Int
    )

fun plus(pair: Pair<Int, Int>) = pair.first + pair.second

fun main() {

    println(plus(Pair(1, 3)))
}