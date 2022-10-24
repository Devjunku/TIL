package com.kotlinjava.jvmstatic

class HelloClass {

    companion object {
        fun hello() = "hello"
    }

}

object Hiobject {
    fun hi() = "hi"
}

fun main() {
    val helloClass = HelloClass.hello()
    val hi = Hiobject.hi()

    
}