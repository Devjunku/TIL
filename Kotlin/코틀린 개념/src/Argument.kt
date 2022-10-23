val property = "pt"

fun ff(): String {
    return "hi"
}

fun main(args: Array<String>) {





    println(6 multiply 4)
    // 6이 this에 해당하고
    // 4가 x에 해당함
    // 위와 같은 의미를 갖는 코드는 다음과 같음
    println(6.multiply(4))

}

infix fun Int.multiply(x: Int): Int = this * x