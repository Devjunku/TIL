class C1 {
    static int static_variable = 1; // static이 붙어 있기 때문에 class 변수임
    int instance_variable = 1; //  단순히 int만 있기 때문에 인스턴스 변수임

    // class 메소드
    static void static_static () {
        System.out.println(static_variable);
    }

    static void static_instance() {
        // 클래스 메소드에서는 인스턴스 변수에 접근할 수 없다.
        // System.out.println(instance_variable);
    }

    // 인스턴스 메소드
    void instance_static () {
        // 인스턴스 메소드는 클래스 변수에 접근 가능하다.
        System.out.println(static_variable);
    }

    void instance_instance () {
        System.out.println(instance_variable);
    }

}

public class ClassMemberDemo {
    public static void main(String[] args) {

        C1 c1 = new C1();

        c1.static_static();

        c1.static_instance();

        c1.instance_static();

        c1.instance_instance();

        C1.static_static();
        C1.static_instance();
    }
}
