//fun main(args: Array<String>) {
//    println(solution("one4seveneight"))
//    println(solution("23four5six7"))
//    println(solution("2three45sixseven"))
//    println(solution("123"))
//}

//pravate fun solution(s: String): Int {
//    val dicNumber: HashMap<String, String>
//    dicNumber = hashMapOf(
//        "one" to "1",
//        "two" to "2",
//        "three" to "3",
//        "four" to "4",
//        "five" to "5",
//        "six" to "6",
//        "seven" to "7",
//        "eight" to "8",
//        "nine" to "9",
//        "zero" to "0"
//    )
//    var answer = ""
//    var stringNumber: String = ""
//    for (str in s) {
//        if (str.isDigit()) answer += str
//        else {
//            stringNumber += str
//        }
//        if (dicNumber.containsKey(stringNumber)) {
//            answer += dicNumber[stringNumber]
//            stringNumber = ""
//        }
//    }
//    return answer.toInt()
//}