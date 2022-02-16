import java.io.BufferedReader
import java.io.InputStreamReader
import java.util.*
import kotlin.collections.HashMap

private lateinit var visit: HashMap<String, Boolean>
var init_key = ""

fun main(): Unit = with(BufferedReader(InputStreamReader(System.`in`))) {
    for (i in 0 until 3) {
        init_key = "$init_key${readLine().split(" ").joinToString("")}"
    }

    println(init_key)

    fun puzzleBfs(): Int {
        var queue: Queue<KeyValue> = LinkedList()
        visit = hashMapOf(
            init_key to true
        )

        val dx = arrayOf(0, 1, 0, -1)
        val dy = arrayOf(1, 0, -1, 0)

        while (queue.isNotEmpty()) {
            var key = queue.peek().hashKey
            var cnt = queue.peek().count

            if (key == "123456780")  return cnt

            var zero = 0
            for (i in 0 until 9) if (key[i] == '0') {
                zero = i
            }

            var row = zero / 3
            var col = zero % 3

            for (i in 0 until 4) {
                var nRow = row + dx[i]
                var nCol = col + dy[i]

                if (nRow in 0 until 3 && nCol in 0 until 3) {
                    var keyList = key.split("")
                    print(keyList)
                }
            }


        }
        return 1
    }

    puzzleBfs()

}


data class KeyValue(
    val hashKey: String,
    val count: Int
)