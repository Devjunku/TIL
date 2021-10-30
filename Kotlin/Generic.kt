package com.example.kotlinPractice

fun main() {

    UsingGeneric(A()).doShouting()
    UsingGeneric(B()).doShouting()
    UsingGeneric(C()).doShouting()

    doShouting(B())

}

fun <T : A> doShouting(t: T) {
    t.shout()
}

open class A {
    open fun shout() {
        println("A가 소리칩니다")
    }
}

class B : A() {
    override fun shout() {
        println("B가 소리칩니다")
    }
}

class C : A() {
    override fun shout() {
        println("C가 소리칩니다")
    }
}

class UsingGeneric<T : A> (val t : T) {
    fun doShouting() {
        t.shout()
    }
}