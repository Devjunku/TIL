import java.util.Scanner

fun main(args: Array<String>) {
    val sc = Scanner(System.`in`)
    val n = sc.nextInt()
    val m = sc.nextInt()

    val arr = IntArray(n+1) {0}

    for (i in 1..n) arr[i] += arr[i-1] + sc.nextInt()

    var i: Int
    var j: Int
    var sb = StringBuilder()

    for (k in 0 until m) {
        i = sc.nextInt()
        j = sc.nextInt()
        sb.append((arr[j] - arr[i-1]).toString() + "\n")
    }
    println(sb)
    sc.close()
}