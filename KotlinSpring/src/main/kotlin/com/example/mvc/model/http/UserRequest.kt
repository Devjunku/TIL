package com.example.mvc.model.http

import com.fasterxml.jackson.annotation.JsonProperty
import com.fasterxml.jackson.databind.PropertyNamingStrategies

import com.fasterxml.jackson.databind.annotation.JsonNaming

/**
 * 회사에 따라서 아래와 같이 클래스에 해당 타입을 지정해줄 수 있음
 * PropertyNamingStrategies에서 새로운 case 타입을 지정한 후 ::class를 넣으면 됨
 */

@JsonNaming(PropertyNamingStrategies.SnakeCaseStrategy::class)
data class UserRequest(
    var name: String? = null,
    var age: Int? = null,
    var email: String? = null,
    var address: String? = null,

    @JsonProperty("phone_number")
    var phoneNumber: String? = null
)