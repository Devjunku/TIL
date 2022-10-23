package com.example.kotlinspringtodolist.error.model

import com.fasterxml.jackson.annotation.JsonProperty
import java.time.LocalDateTime

data class ErrorResponse(
    @JsonProperty("result_code")
    var resultCode: String? = null,

    @JsonProperty("http_status")
    var httpStatus: String? = null,

    @JsonProperty("http_method")
    var httpMethod: String? = null,

    var message: String? = null,

    var path: String? = null,

    @JsonProperty("timestamp")
    var timeStamp: LocalDateTime? = null,

    var errors: MutableList<Error>? = null
)


