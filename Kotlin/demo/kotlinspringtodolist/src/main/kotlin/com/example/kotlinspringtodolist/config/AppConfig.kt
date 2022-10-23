package com.example.kotlinspringtodolist.config

import com.example.kotlinspringtodolist.database.ToDoDataBase
import org.springframework.context.annotation.Bean
import org.springframework.context.annotation.Configuration

/**
 * 아래 값을 먼저 참조하도록 Config Class로 만들어야함.
 * 특히 Bean이 만들어질 때 특정 메소드를 참조해라! 라는 코드는 @Bean에 initMethod="특정 메소드 이름"으로
 * 설정할 수 있다.
 *
 * 이 과정이 mysql을 준비해서 craeted Table까지 한 것으로 생각하면 된다.
 */

@Configuration
class AppConfig {

    @Bean(initMethod="init")
    fun toDoDataBase(): ToDoDataBase {
        return ToDoDataBase()
    }


}