fun main(args: Array<String>) {
    Outer.Nested().introdue()

    val outer = Outer()
    val inner = outer.Inner()

    inner.introduceInner()
    inner.introduceOuter()

    outer.text = "Changed Outer Class"
    inner.introduceOuter()
}

class Outer {
    var text = "Outer Class"

    class Nested {
        fun introdue() {
            println("Nested Class")
        }
    }

    inner class Inner {
        var text = "Inner Class"

        fun introduceInner() {
            println(text)
        }

        fun introduceOuter() {
            println(this@Outer.text) // 위와 같이 외부 클래스를 참조하면 됨
        }
    }
}

class Sunkyu {
    var study = "study"
}