package com.example.kotlinPractice

// collection class 중 map과 set임

fun main()
{
//    val a = mutableSetOf("귤", "바나나", "오렌지")
//    for (item in a)
//    {
//        println("${item}")
//    }
//    a.add("자몽")
//    println(a)
//
//    a.remove("바나나")
//    println(a)
//
//    println(a.contains("귤"))

    val b = mutableMapOf("레드벨벳" to "음파음파",
                         "트와이스" to "FANCY",
                         "ITZY" to "ICY")

    b.put("SG워너비", "라라라")

    for (entry in b)
    {
        println("${entry.key}: ${entry.value}")
    }

    b.remove("레드벨벳")

    println(b)
    println(b["SG워너비"])
}

// set은 정렬과 중복이 허용되지 않는 collection임
// 따라서 index로는 접근 불가능하고 contains로 set안에 원소가 있는지 확인하는 용도로만 사용
// set도 역시 mutable set이 존재함
// List와 같이 객체의 추가 삭제가 가능한지에 대한 여부가 있을 때 사용하게 됨

// 추가는 add
// 삭제는 remove로 하게됨

// map은 객체를 넣을 때 그 객체를 찾아줄 수 있는 key를 쌍으로 넣어주는 collection임
// mutableMap.mutableEntry로 담겨져 있음
// 이를 통해 객체의 key값으로 객체 접근하는 특징을 갖고 있음.
// 그냥 python의 dictionary와 같은거 같음
// map도 역시 추가 삭제가 가능한 mutableMap이 존재함.

// 요소 추가는 put(키, 값)
// 요소 삭제는 remove(키)로 하게 됨

