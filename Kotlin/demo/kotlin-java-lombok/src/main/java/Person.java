import lombok.Getter;
import lombok.Setter;

import java.util.Objects;

//@Getter
//@Setter
public class Person {

    /**
     * lombok를 통해 getter와 setter를 만들어 줄 수 있음.
     * 근데 lombok은 kotlin complier가 읽을 수는 없음.
     */

    private String name;

    private int age;

    private String address;

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        Person person = (Person) o;
        return age == person.age && Objects.equals(name, person.name) && Objects.equals(address, person.address);
    }

    @Override
    public String toString() {
        return "Person{" +
                "name='" + name + '\'' +
                ", age=" + age +
                ", address='" + address + '\'' +
                '}';
    }

    @Override
    public int hashCode() {
        return Objects.hash(name, age, address);
    }

    public String getName() {
        return name;
    }
    public void setName(String name) {
        this.name = name;
    }

    public int getAge() {
        return age;
    }

    public void setAge(int age) {
        this.age = age;
    }

    public String getAddress() {
        return this.address;
    }

    public void setAddress(String address) {
        this.address = address;
    }

    public static void main(String [] args) {
        PersonKotlin person = new PersonKotlin();
        person.setName("junku");
        person.setAge(30);
        person.setAddress("seoul");
    }

    /**
     * 근데 이제 이걸 매번하기에는 좀.. 번거로우니까.
     * 그냥 kotlin code로 작성하는 것이 더 효율적임.
     */


}
