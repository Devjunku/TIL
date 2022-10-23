package com.kotlinjava.gettersetter;

import java.time.LocalDate;

public class JavaGetterSetterExample {

    public static void main(String [] args) {
        Student student = new Student();
        student.name = "스티브로저스";
        student.setBirthDate(LocalDate.of(1918, 7, 4));

        System.out.println(student.name);
        System.out.println(student.getBirthDate());

        student.changeGrade("A");

        System.out.println(student.getGrade());

        // jvm field annotation을 사용해서 kotlin property에 접근하는 방식에 대해 살펴보자.

        /**
         * kotlin의 property를 java로 변환할 때는 getter setter를 통해서만 접근이 가능함.
         * 하지만, JvmField annotation을 사용하면 getter setter를 사용하지 않고 변경이 가능하여 java property로 접근이 가능함.
         */

    }
}
