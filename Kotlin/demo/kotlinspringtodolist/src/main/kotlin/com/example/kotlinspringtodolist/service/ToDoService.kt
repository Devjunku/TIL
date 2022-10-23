package com.example.kotlinspringtodolist.service

import com.example.kotlinspringtodolist.database.ToDo
import com.example.kotlinspringtodolist.database.convertToDo
import com.example.kotlinspringtodolist.model.http.ToDoDto
import com.example.kotlinspringtodolist.model.http.convertToDoDto
import com.example.kotlinspringtodolist.repository.ToDoRepositoryImpl
import org.springframework.stereotype.Service

/**
 * 지금 현재 코드는 협업에서 많이 쓰는 것은 아님
 * 많이 쓰는 변환 방법
 * 1. model mapper
 * 2. kotlin reflection
 *
 */


@Service
class ToDoService(
    val toDoRepositoryImpl: ToDoRepositoryImpl
) {
    /**
     * impl의 경우 DB 동작이 어떻게 될지?
     * Service의 경우 request 요청이 들어왔을 때, 화면 단에 어떤 로직이 수행되어야 할지?
     * controller는 이러한 요청이 들어왔을 때 어떻게 처리할지?
     */


    // C
    fun create(toDoDto: ToDoDto): ToDoDto? {
        return toDoDto.let {
            ToDo().convertToDo(it)
        }.let {
            toDoRepositoryImpl.save(it)
        }?.let {
            ToDoDto().convertToDoDto(it)
        }
    }

    // R
    // 단 건 읽기
    fun read(index: Int): ToDoDto? = toDoRepositoryImpl.findOne(index)?.let {
        ToDoDto().convertToDoDto(it)
    }

    // 다 건 읽기
    fun readAll(): MutableList<ToDoDto> = toDoRepositoryImpl
        .findAll()
        .map {
            ToDoDto()
                .convertToDoDto(it)
    }
        .toMutableList()

    // U
    fun update(toDoDto: ToDoDto): ToDoDto? {
        return toDoDto.let {
            ToDo().convertToDo(it)
        }.let {
            toDoRepositoryImpl.save(it)
        }?.let {
            ToDoDto().convertToDoDto(it)
        }
    }

    // D
    fun delete(index: Int): Boolean = toDoRepositoryImpl.delete(index)

}