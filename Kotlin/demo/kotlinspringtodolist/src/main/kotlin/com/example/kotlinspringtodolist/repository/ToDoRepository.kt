package com.example.kotlinspringtodolist.repository

import com.example.kotlinspringtodolist.database.ToDo

interface ToDoRepository {

    /**
     * 반드시 있어야 하는 CRUD
     * TODO
     * 1. save
     * 2. save all
     * 3. update → save에 넘김
     */

    fun save(toDo: ToDo): ToDo?

    fun saveAll(toDoList: MutableList<ToDo>): Boolean

    // fun update(toDo: ToDo): ToDo

    fun delete(index: Int): Boolean

    fun findOne(index: Int): ToDo?

    fun findAll(): MutableList<ToDo>

}