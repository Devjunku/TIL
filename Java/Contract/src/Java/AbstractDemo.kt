package Java


var a: String = "패키지 스코프"

class Scope{
    val a = "클래스 스코프"
    fun print() {
        var a = "함수 스코프"
        println(a)
    }
}

fun main(args: Array<String>) {
    val a = "함수 스코프"
    println(a)
    val s = Scope()
    s.print()
}