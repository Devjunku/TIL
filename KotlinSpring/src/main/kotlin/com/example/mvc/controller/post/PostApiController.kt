package com.example.mvc.controller.post

import com.example.mvc.model.http.UserRequest
import org.springframework.web.bind.annotation.PostMapping
import org.springframework.web.bind.annotation.RequestBody
import org.springframework.web.bind.annotation.RequestMapping
import org.springframework.web.bind.annotation.RequestMethod
import org.springframework.web.bind.annotation.RestController

@RestController
@RequestMapping("/api")
class PostApiController {

    /**
     * 2가지 방식을 알아볼 것임
     * 1. 현대 방식
     * 2. 예전 방식
     */

    @PostMapping("/post-mapping")
    fun postMapping(): String = "post-mapping"

    /**
     * 동일한 method에 동일한 주소일 경우 오류가 나기 때문에 조심해야함.
     */
    @RequestMapping(method = [RequestMethod.POST], path = ["/request-mapping"])
    fun requestMapping(userRequest: UserRequest): String = "before-post-mapping"

    /**
     * JSON data가 오고 가는 것이면 object Mapper는 사용함
     * JSON -> Object
     * Object -> JSON
     */

    @PostMapping("/post-mapping/object")
    fun postObjectMapping(@RequestBody userRequest: UserRequest): UserRequest {
        // JSON -> Object
        println(userRequest)
        return userRequest // Object -> JSON
    }

    /**
     * 조금 더 복잡한 예제
     * snake_case와 camelCase 간에 변수 매칭을 할 수 없는 문제점에서 봉착하게 되는데, 이때 어떻게 해야하는가?
     * 이때는 JsonProperty를 사용한다.
     */




}