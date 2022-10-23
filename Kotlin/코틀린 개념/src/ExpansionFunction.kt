fun String.first(): Char = this[0]

fun String.addFirst(char: Char): String = char + this.substring(0)

/**
 * 실제 class는 확장맴버 보다는 기존 맴버가 우선시 됨.
 * 왜 그럴까?
 * kotlin complier가 class를 우선으로 complie을 해버림
 * 또한 확장함수의 경우 기존 클래스에 해당 method가 존재하는지 확인해야 함.
 *
 * 그럼 이걸 왜쓸까?
 * ??
 */

class MyExample() {
    fun myMessage() = println("class member")
}

fun MyExample.myMessage(message: String) = println(message)

fun MyExample?.printNullOrNotNull() {
    if (this == null) println("null")
    else println("notNull")
}



fun main() {
    var myExample: MyExample? = null
    myExample.printNullOrNotNull()

    myExample = MyExample()
    myExample.printNullOrNotNull()
    MyExample().myMessage("확장 출력")

    println("ABCD".first())
    println("ABCD".addFirst('E'))

    val generic = MyGeneric<String>("테스트")

    // PECS


}