package com.example.kotlinspringtodolist.repository

import com.example.kotlinspringtodolist.database.ToDo
import com.example.kotlinspringtodolist.database.ToDoDataBase
import org.springframework.beans.factory.annotation.Autowired
import org.springframework.stereotype.Service
import java.time.LocalDateTime


@Service
class ToDoRepositoryImpl(
    val toDoDataBase: ToDoDataBase
): ToDoRepository {

    // 여기서 DataBase가 있어야 함
    // @AutoWIred로 갖고오자
    // ToDoDataBase는 자동으로 아래에 주입됨.
    //  @Autowired
    // lateinit var toDoDataBase: ToDoDataBase
    // 이걸 안쓰고 싶으면 그냥 생성자로 주입하면 됨.


    override fun save(toDo: ToDo): ToDo? {
        /**
         * save전 index를 따야하기 때문에
         * 해당 부분을 연산하자.
         * 그리고 return 해주자.
         */

        /**
         * 1. index가 있음?
         */

        return toDo.index?.let { index ->
            // update
            findOne(index)?.apply {
                this.title = toDo.title
                this.description = toDo.description
                this.updatedAt = LocalDateTime.now()
                this.schedule = toDo.schedule
            }
        }?: run {
            // insert
            toDo.apply {
                this.index = ++toDoDataBase.index
                this.createdAt = LocalDateTime.now()
                this.updatedAt = LocalDateTime.now()
            }.run {
                toDoDataBase.toDoList.add(toDo)
                this
            }
        }
    }

    override fun saveAll(toDoList: MutableList<ToDo>): Boolean {
        return try {
            toDoList.forEach {
                save(it)
            }
            true
        } catch (e: Exception) {
            false
        }
    }

    /**
     * jpa는 save method만 제공함.
     * 여기서 index가 존재하면 update고
     * 없으면 save임
     * 그래서 update는 안함.
     */


    override fun findOne(index: Int): ToDo? {
        return toDoDataBase.toDoList.first {
            it.index == index
        }
    }

    override fun delete(index: Int): Boolean = findOne(index)?.let {
            toDoDataBase.toDoList.remove(it)
            true
        }?: run {
            false
        }

    override fun findAll(): MutableList<ToDo> = toDoDataBase.toDoList
}