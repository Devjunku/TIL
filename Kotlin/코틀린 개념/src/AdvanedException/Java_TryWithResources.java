package AdvanedException;

/**
 * finally 코드에서 FileWriter에서 close 처리를 해주어야 한다.
 * try catch를 사용하면 자동으로 close 처리릏 해주게 된다.
 * 실제 코드를 확인해보자.
 */

import java.io.FileWriter;
import java.io.IOException;

public class Java_TryWithResources {

    public static void main(String [] args) {
        try(FileWriter fileWriter = new FileWriter("test.txt")) {
            fileWriter.write("hello java");

        } catch(IOException e) {
            System.out.println(e.getMessage());
        }
    }
}
