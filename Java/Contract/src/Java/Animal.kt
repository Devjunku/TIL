fun main(args: Array<String>) {

    var a = Animal("별이", 5, "개")
    var b = Dog("별이", 5)
    a.introduce()
    b.introduce()

    b.bark()

    var c = Cat("루이", 5)

    c.introduce()
    c.meow()
}

// Kotlin에서 상속을 하기 위해서는 class 앞에서 꼭 open을 붙여주면 된다.
open class Animal(var name: String, var age: Int, var type: String) {
    fun introduce() {
        println("저는 ${type} ${name}이고 ${age}살 입니다.")
    }
}
// 생성자에서 속성을 받지만, val와 var를 넣지 않음.
// 만약에 val와 var를 넣으면 속성으로 선언되기 때문에 조심해야함.
// 따라서 일반 패러미터로 받는 것이 좋음
// 상속은 class 뒤에 :과 상속할 클래스의 이름을 붙여야 함
class Dog(name: String, age:Int): Animal(name, age, "개") {
    fun bark() {
        println("멍멍!")
    }
}

class Cat(name:String, age:Int): Animal(name, age, "고양이") {
    fun meow() {
        println("냐옹!")
    }
}