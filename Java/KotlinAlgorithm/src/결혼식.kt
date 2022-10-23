import java.io.BufferedReader
import java.io.InputStreamReader
import java.util.*
import kotlin.properties.Delegates



private var nodeNum: Int = 0
private var arrNum by Delegates.notNull<Int>()
fun main() {
    val br = BufferedReader(InputStreamReader(System.`in`))
    nodeNum = br.readLine().toInt()
    arrNum = br.readLine().toInt()

    val graph = Array(nodeNum) { ArrayList<Int>() }

    for (i in 0 until arrNum) {
        var startEnd = br.readLine().split(" ").map { it.toInt() }
        graph[startEnd[0]-1].add(startEnd[1]-1)
        graph[startEnd[1]-1].add(startEnd[0]-1)
    }

}