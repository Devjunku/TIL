/**
 * 제네릭
 * Type Parameter가 존재함.
 */

class MyGeneric<out T>(val t :T) {

}

class Bag<T> {
    fun saveAll(
        to: MutableList<in T>,
        from: MutableList<T>
    ) {
        to.addAll(from)
    }
}

fun main() {

    val generic = MyGeneric<String>("테스트")
    val CharGeneric: MyGeneric<CharSequence> = generic
    /**
     * PECS Producer-Extends Consumer-Super
     * 공변성, 자바 제네릭의 extends, 코틀린에서의 out
     * 반공변성, 자바 제네릭의 super, 코틀린에서의 in
     *
     * 상위 클래스를 하위 클래스로 할당은 가능함.
     */

    val bag = Bag<String>()
    bag.saveAll(mutableListOf<CharSequence>("1", "2", "3", "4"), mutableListOf<String>("5", "6", "7", "8"))



}