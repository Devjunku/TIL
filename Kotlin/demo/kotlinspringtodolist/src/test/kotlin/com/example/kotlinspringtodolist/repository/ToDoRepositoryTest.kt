package com.example.kotlinspringtodolist.repository

import com.example.kotlinspringtodolist.config.AppConfig
import com.example.kotlinspringtodolist.database.ToDo
import org.junit.jupiter.api.Assertions
import org.junit.jupiter.api.BeforeEach
import org.junit.jupiter.api.Test
import org.junit.jupiter.api.extension.ExtendWith
import org.springframework.beans.factory.annotation.Autowired
import org.springframework.boot.test.context.SpringBootTest
import org.springframework.test.context.junit.jupiter.SpringExtension
import java.time.LocalDateTime

/**
 * @SpringBootTest → 테스트할거라고 알려주긴 하는데
 * 아무것도 안 적으면 모든 것 다 complie하기 때문에
 * 테스트가 많으면 시간이 오래 걸리므로 테스트할 클래스를 정해주는 것이 중요함.
 * 확장 기능을 사용하겠는가? → @ExtendWith → SpringExtention::class 추가
 */


@ExtendWith(SpringExtension::class)
@SpringBootTest(classes = [ToDoRepositoryImpl::class, AppConfig::class])
class ToDoRepositoryTest {

    @Autowired
    lateinit var toDoRepositoryImpl: ToDoRepositoryImpl

    @BeforeEach
    fun before() {
        // Test가 시작될 때 데이터 베이스 초기화!
        toDoRepositoryImpl.toDoDataBase.init()
    }

    @Test
    fun saveTest() {
        val toDo = ToDo().apply {
            this.title = "테스트 일정"
            this.description = "테스트"
            this.schedule = LocalDateTime.now()
        }

        val result = toDoRepositoryImpl.save(toDo)

        Assertions.assertEquals(1, result?.index)
        Assertions.assertNotNull(result?.createdAt)
        Assertions.assertNotNull(result?.updatedAt)
        Assertions.assertEquals("테스트 일정", result?.title)
        Assertions.assertEquals("테스트", result?.description)
    }

    @Test
    fun saveAllTest() {
        val toDoList = mutableListOf(
            ToDo().apply {
                this.title = "테스트 일정1"
                this.description = "테스트1"
                this.schedule = LocalDateTime.now()
            },
            ToDo().apply {
                this.title = "테스트 일정2"
                this.description = "테스트2"
                this.schedule = LocalDateTime.now()
            },
            ToDo().apply {
                this.title = "테스트 일정3"
                this.description = "테스트3"
                this.schedule = LocalDateTime.now()
            }
        )

        val result = toDoRepositoryImpl.saveAll(toDoList)
        Assertions.assertEquals(true, result)
    }

    @Test
    fun findOneTest() {

        val toDoList = mutableListOf(
            ToDo().apply {
                this.title = "테스트 일정1"
                this.description = "테스트1"
                this.schedule = LocalDateTime.now()
            },
            ToDo().apply {
                this.title = "테스트 일정2"
                this.description = "테스트2"
                this.schedule = LocalDateTime.now()
            },
            ToDo().apply {
                this.title = "테스트 일정3"
                this.description = "테스트3"
                this.schedule = LocalDateTime.now()
            }
        )
        toDoRepositoryImpl.saveAll(toDoList)

        val result = toDoRepositoryImpl.findOne(2)
        println("여기!!!!!! $result")
        Assertions.assertNotNull(result)
        Assertions.assertEquals("테스트 일정2", result?.title)
    }

    @Test
    fun updateTest() {
        val toDo = ToDo().apply {
            this.title = "업데이트 전 title"
            this.description = "업데이트 전 description"
            this.schedule = LocalDateTime.now()
        }

        val insertToDo = toDoRepositoryImpl.save(toDo)

        val updateToDo = ToDo().apply {
            this.index = insertToDo?.index
            this.title = "업데이트 후 title"
            this.description = "업데이트 후 description"
            this.updatedAt = LocalDateTime.now()
        }

        val result = toDoRepositoryImpl.save(updateToDo)

        Assertions.assertNotNull(result)
        Assertions.assertEquals(updateToDo.index, result?.index)
        Assertions.assertEquals(updateToDo.title, result?.title)
        Assertions.assertEquals(updateToDo.description, result?.description)
    }

    @Test
    fun deleteTest() {
        val toDoList = mutableListOf(
            ToDo().apply {
                this.title = "테스트 일정1"
                this.description = "테스트1"
                this.schedule = LocalDateTime.now()
            },
            ToDo().apply {
                this.title = "테스트 일정2"
                this.description = "테스트2"
                this.schedule = LocalDateTime.now()
            },
            ToDo().apply {
                this.title = "테스트 일정3"
                this.description = "테스트3"
                this.schedule = LocalDateTime.now()
            }
        )
        toDoRepositoryImpl.saveAll(toDoList)
        val result = toDoRepositoryImpl.delete(1)
        Assertions.assertNotNull(result)
        Assertions.assertEquals(true, result)
    }
}