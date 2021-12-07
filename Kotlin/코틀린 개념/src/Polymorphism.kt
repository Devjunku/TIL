fun main(args: Array<String>) {

    var a = Food()
    a.eat()

    var b: Food = KoreanFood()
    b.eat()
    // b는 Food 타입이지만, KoreanFood에서 override한
    // eat 함수를 호출할 수 있다.

    // 하지만 Food 타입임으로 delicious를 호출할 수는 없다.
    // 실제로 작성해보면 참조할 수 없다고 뜰 것이다.
    // 이때는 is나 as를 통해 down-casting해야 한다.

    // is를 통해 짐시 down-casting하는 방법
    if( b is KoreanFood) // is는 조건문 안에서만 잠깐 down-casting 됨.
    {
        b.delicious()
    }

    // as를 통해 down-casting 된 자료형을 저장하여 하위 클래스의 인스턴스를 사용하는 방법
    var c = b as KoreanFood
    c.delicious()

    // 현재 밑의 코드에 참조 오류가 발생하지 않는데
    // 그 이유는 as를 사용하면 반환값 뿐만 아니라 사용한 값까지 모두 down-casting되기 때문이다.
    b.delicious()

    // 다형성은 클래스의 상속관계에서 오는 인스턴스의 호환성을 적극 활용할 수 있는 기능으로
    // 슈퍼 클래스가 같은 인스턴스를 한번에 관리하거나 인터페이스를 구현하여 사용하는 코드에서도
    // 이용되니 이해해야 한다.

}


open class Food {

    var name = "음식"

    open fun eat() {
        println("${name}을 먹습니다.")
    }
}

class KoreanFood: Food() {
    var type = "한식"

    override fun eat() {
        println("${name}중에 ${type}을 먹습니다.")
    }

    fun delicious() {
        println("${type}은 맛있습니다.")
    }
}

