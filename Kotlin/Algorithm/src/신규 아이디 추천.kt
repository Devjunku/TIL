fun main(args: Array<String>) {
    println(solution("...!@BaT#*..y.abcdefghijklm"))
    println(solution(	"z-+.^."))
    println(solution("=.="))
    println(solution("123_.def"))
    println(solution("abcdefghijklmn.p"))
}

fun solution(new_id: String):String {
    // 1단계
    new_id.lowercase()

    // 2단계
    new_id.replace("#", "")
    new_id.replace("@", "")
    new_id.replace("*", "")


    // 3단계
    while (new_id.contains("...")) {
        new_id.replace("...",".")
    }

    while (new_id.contains("..")) {
        new_id.replace("..",".")
    }

    var newId = ""

    // 4단계
    if (new_id[0] == '.') {
        newId = new_id.substring(1, new_id.length-1)
    }

    if (newId[newId.length-1] == '.') {
        newId = newId.substring(0, newId.length-2)
    }

    // 5단계
    if (newId.length == 0) {
        newId = "a"
    }

    if (newId.length >= 16 ) {
        newId = newId.substring(0, 14)
    }

     while (newId.length <= 2) {
         newId += newId[newId.length-1]
     }

    return newId
}