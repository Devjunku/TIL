fun main() {
    val person = Person()

    /**
     * person.name = "junku"
     * println(person.name)
     * 위와 같이 실행하면 getter, setter annotation을 만든 것은
     * Cannot access 'name': it is private in 'Person'와 같이 뜨게 됨.
     *
     *  그러면 address의 경우 어떻게 될까?
     */

    person.address = "seoul"
    println(person.address)

    /**
     * 직접 만든 set의 경우 직접 접근할 수 있음.
     * 즉 lombok의 경우 kotlin과 호환되지 않는 것을 확인할 수 있음.
     *
     * 그 이유로는 바이트코드를 생성하면서, annotation processing이 작동하는 데, 이때 중요한게 lombok으로 만든 annotation의 경우
     * 뒤늦게 바이트코드로 변환되기 때문에, kotlin이 읽지 못하는 것임. 즉
     * kotlin code -> kotlin complier -> kotlin bytecode
     * java code -> java complier -> java bytecode -> annotation processing -> bytecode -> JVM과 같은 순이기 때문에
     * annotation processing이 하기 전에 이미 kotlin에서 컴파일이 끝나 해당 lombok의 getter, setter를 읽을 수 없는 것임.
     *
     * 이러한 문제점을 없애는 것중 가장 손쉬운 방법은 lombok을 그냥 없애는 것임..
     * 지금 lombok을 없애고 intellij의 기능을 사용하여 getter, setter를 바로 생성했음.
     * 이제 오류가 나지 않을 것임.
     */

    person.name = "junku"
    person.age = 30
    println(person.name)
    println(person.age)

    /**
     * data class로 만들어서 사용하면 더욱 간편함.
     */

    val personKotlin = PersonKotlin()
    personKotlin.age = 10
    personKotlin.name = "junku"
    personKotlin.address = "seoul"

    println(personKotlin.age)
    println(personKotlin.name)
    println(personKotlin.address)

    /**
     * 중요
     * kotlin에서도 최근에 lombok plugin을 제공하고 있음.
     */
}