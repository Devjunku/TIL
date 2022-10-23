package com.example.kotlinspringtodolist.model.dateformatvalidator

import com.example.kotlinspringtodolist.model.dateformatannotation.StringFormatDateTimeAnnotation
import java.time.LocalDateTime
import java.time.format.DateTimeFormatter
import javax.validation.ConstraintValidator
import javax.validation.ConstraintValidatorContext

class StringFormatDateTimeValidator: ConstraintValidator<StringFormatDateTimeAnnotation, String> {

    private var pattern: String? = null

    override fun initialize(constraintAnnotation: StringFormatDateTimeAnnotation?) {
        this.pattern = constraintAnnotation?.pattern
        super.initialize(constraintAnnotation)
    }

    override fun isValid(value: String?, context: ConstraintValidatorContext?): Boolean {
        return try {
            LocalDateTime.parse(value,  DateTimeFormatter.ofPattern(pattern))
            true
        } catch (e: Exception) {
            false
        }
    }
}