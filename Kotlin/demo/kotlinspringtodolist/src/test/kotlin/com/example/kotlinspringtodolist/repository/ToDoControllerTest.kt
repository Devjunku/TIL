package com.example.kotlinspringtodolist.repository

import com.example.kotlinspringtodolist.config.AppConfig
import com.example.kotlinspringtodolist.controller.api.todo.ToDoApiController
import org.junit.jupiter.api.extension.ExtendWith
import org.springframework.boot.test.context.SpringBootTest
import org.springframework.test.context.junit.jupiter.SpringExtension


@ExtendWith(SpringExtension::class)
@SpringBootTest(classes = [ToDoApiController::class, AppConfig::class])
class ToDoControllerTest {





}