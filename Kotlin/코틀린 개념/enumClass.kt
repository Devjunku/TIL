package com.example.kotlinPractice.`코틀린 개념`

fun main() {

    var state = State.SING
    println(state)

    state = State.SLEEP
    println(state.isSleeping())

    state = State.EAT
    println(state.message)

}

enum class State(val message: String) {
    SING("노래를 부릅니다."),
    EAT("음식을 먹습니다."),
    SLEEP("잠을 잡니다.");

    fun isSleeping() = this == SLEEP
}