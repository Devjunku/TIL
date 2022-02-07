package com.example.kotlinPractice.`코틀린 개념`

fun main() {

//    read(7)
//    read("감사합니다.")

//    deliverly("짬뽕")
//    deliverly("책", 3)
//    deliverly("노트북", 30, "학교")
//
//    deliverly("선물", destination="친구집")

//    sum(1, 2, 3, 4)

    println(6 multiply 4)
    println(6.multiply(4))
}

fun read(x: Int) {
    println("숫자 $x 입니다.")
}

fun read(x: String) {
    print("문자 $x 입니다.")
}

fun deliverly(name: String, count: Int = 1, destination: String = "집") {
    println("${name} ${count}개를 ${destination}에 배달하였습니다.")
}

fun sum(vararg numbers: Int) {
    var num = 0

    for( n in numbers) {
        num += n
    }
    println(num)
}

infix fun Int.multiply(x: Int): Int = this * x