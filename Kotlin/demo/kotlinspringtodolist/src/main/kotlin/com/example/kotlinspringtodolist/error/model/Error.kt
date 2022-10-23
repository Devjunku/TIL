package com.example.kotlinspringtodolist.error.model

data class Error(
    var field: String? = null,
    var message: String? = null,
    var value: String? = null
)
