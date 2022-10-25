package com.kotlinjava.extensions;

public class ExtensionExample {
    public static void main(String [] args) {
        // 확장함수는 java에서 static method가 됨.
        System.out.println(MyExtensionsKt.first("ABCD"));
        System.out.println(MyExtensionsKt.addFirstChar("ABCD", 'Z'));
    }
}
