fun main(args: Array<String>) {
    UsingGeneric(A()).sleeping() // A가 잡니다
    UsingGeneric(B()).sleeping() // B가 잡니다
    UsingGeneric(B()).sleeping() // C가 잡니다

    sleeping(A()) // A가 접니다.
    sleeping(B()) // B가 접니다.
    sleeping(C()) // C가 접니다.
}

fun <T:A> sleeping(t: T) {
    t.sleep()
}

open class A {
    open fun sleep() {
        println("A가 잡니다")
    }
}

class B: A() {
    override fun sleep() {
        println("B가 잡니다")
    }
}

class C: A() {
    override fun sleep() {
        println("C가 잡니다")
    }
}

class UsingGeneric<T: A> (val t: T){
    fun sleeping() {
        t.sleep()
    }
}