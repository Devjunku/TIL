package com.example.kotlinspringtodolist.database

/**
 * DataBase가 Spring에서 관리할 수 있도록 Bean으로 등록
 * 스프링의 모든 것은 Bean임
 */

data class ToDoDataBase(
    var index: Int = 0,
    var toDoList: MutableList<ToDo> = mutableListOf(),

) {
    fun init() {
        /**
         * 초기화 할 때 모든 property를 초기화할 수 있도록 해야함.
         */

        this.index = 0
        this.toDoList = mutableListOf()

        println("[DEBUG] ToDo DataBase Init!!")
    }
}
