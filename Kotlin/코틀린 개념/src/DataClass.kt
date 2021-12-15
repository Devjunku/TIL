fun main(args: Array<String>) {

    val list = listOf(
        Data("보영", 212),
        Data("루다", 306),
        Data("아린", 618)
    )
    // 위 데이터가 담긴 Data 객체의 내용을 for문으로 모두 순회하려면

    for((a, b) in list) {
        println("이름은 ${a}이고 ID는 ${b}입니다.")
    }

}

class General(val name: String, val id:Int)

data class Data(val name: String, val id: Int)