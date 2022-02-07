package com.example.kotlinPractice.`코틀린 개념`

fun main() {

    Outer.Nested().introduce()

    val outer = Outer()
    val inner = outer.Inner()

    inner.introduceInner()
    inner.introduceOuter()

    outer.text = "Changed Outer class"
    inner.introduceOuter()

}

class Outer {
    var text = "Outer Class"

    class Nested {
        fun introduce() {
            println("Nested class")
        }
    }

    inner class Inner {
        var text = "Inner Class"
        fun introduceInner() {
            println(text)
        }

        fun introduceOuter() {
            println(this@Outer.text)
        }
    }
}

