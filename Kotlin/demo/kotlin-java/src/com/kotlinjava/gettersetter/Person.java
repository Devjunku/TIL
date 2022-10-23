package com.kotlinjava.gettersetter;


import java.time.LocalDate;
import java.util.UUID;

public class Person {

    private String name;

    private int age;

    private String address;

    private LocalDate birthDate;

    public String getBirthDate() {
        return this.birthDate.toString();
    }

    public void setBirthDate(LocalDate birthDate) {
        this.birthDate = birthDate;
    }

    public String getName() {
        return this.name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getAddress() {
        return this.address;
    }

    public void setAddress(String address) {
        this.address = address;
    }

    public int getAge() {
        return this.age;
    }

    public void setAge(int age) {
        this.age = age;
    }

    public String getUUID() {
        return UUID.randomUUID().toString();
    }

}
