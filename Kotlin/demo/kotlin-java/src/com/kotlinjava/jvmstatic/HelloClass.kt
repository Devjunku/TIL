package com.kotlinjava.jvmstatic

class HelloClass {

    companion object {
        @JvmStatic
        fun hello() = "hello"
    }

}

object Hiobject {
    @JvmStatic
    fun hi() = "hi"
}

fun main() {
    val helloClass = HelloClass.hello()
    val hi = Hiobject.hi()


}