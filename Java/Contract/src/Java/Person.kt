fun main(args: Array<String>) {

    var a = Person("박보영", 1990)
    var b = Person("전정국", 1997)
    var c = Person("장원영", 2004)

    var d = Person("이루다")
    var e = Person("차은우")
    var f = Person("류수정")

}


// init은 패러니터나 반환형이 없는 특수한 함수 생성자를 통해 인스터스가 만들어질 때 호출되는 함수
// 보조생성자는 기본생성자와 다른 형태의 생성자를 제공하여 인스턴스 생성시 편의를 제공하거나 추가적인 구문을 수행하는 기능을 제공하는 역할을 한다.
class Person(var name: String, val birthYear: Int) {
    // 기본 생성자
    init {
        println("${this.name}, ${this.birthYear}")
    }

    // 보조 생성자
    // 보조 생성자를 만들 때는 기본 생성자를 통해 반드시 속성을 초기화 해주어야 함.
    // 보조 생성자가 기본 생성자를 호출하도록 하려면 콜론을 붙인 후 this라는 키워드를 사용하고
    // 기본 생성자가 필요로 하는 파라미터를 괄호 안에 넣어주면 된다.
    constructor(name: String) : this(name, 1997) {
        println("보조 생성자가 실행되었습니다.")
    }

    // 기본 생성자와 보조 생성자는 다양한 방법으로 인스턴스를 생성하도록 사용자들에게 편의를 제공하는 기능임
}