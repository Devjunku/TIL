package com.example.mvcex.controller.post

import com.example.mvcex.model.http.UserRequest
import org.springframework.web.bind.annotation.PostMapping
import org.springframework.web.bind.annotation.RequestBody
import org.springframework.web.bind.annotation.RequestMapping
import org.springframework.web.bind.annotation.RequestMethod
import org.springframework.web.bind.annotation.RestController

@RestController
@RequestMapping("/api")
class PostApiController {

    @PostMapping("/post-mapping")
    fun postMapping(): String {
        return "Post Mapping Complete"
    }

    @RequestMapping(method = [RequestMethod.POST], path = ["/order-post-mapping"])
    fun requestMapping(): String {
        println("order-post-mapping")
        return "Order Post Mapping Complete"
    }

    /**
     * spring에서 데이터가 왔다갔다 거릴때는 object mapper를 사용함.
     * json -> object, object -> json를 해주고 있음.
     */

    // json -> object
    @PostMapping("/post-mapping/object")
    fun objectMappingObject(@RequestBody userRequest: UserRequest): UserRequest {
        println(userRequest)
        // object -> json
        return userRequest
    }

}