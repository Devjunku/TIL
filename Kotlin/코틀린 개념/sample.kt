package com.example.kotlinPractice.`코틀린 개념`

// Kotlin은 Java와 다르게 class 사용시 class를 open하지 않으면, 사용할 수 없음.
// 따라서 open을 따로 해주어야 상속이 가능하다는 것을 명심하자.
// 나아가서 class 내부에 있는 메소드도 open 해주어야 override가 사용가능하다.
open class Human( val name: String = "Anonymous") {

    constructor(name: String, age: Int) : this(name) {
        println("My name is ${name}, ${age}years old")
    }

    fun eatingCake() {
        println("this is so yummy")
    }

    open fun singASong() {
        println("lalala")
    }
}
// 상속
// override
class Korean : Human() {
    override fun singASong() {
        super.singASong() // 위 클래스를 알려줄 때
        println("라라")
    }
}


fun main() {
    val korea = Korean()
    korea.singASong()
}