import java.io.BufferedReader
import java.io.InputStream
import java.io.InputStreamReader

fun main() = with(BufferedReader(InputStreamReader(System.`in`))) {
    val (a, b) = readLine().split(" ").map { it.toInt() }
    println(a + b);
}