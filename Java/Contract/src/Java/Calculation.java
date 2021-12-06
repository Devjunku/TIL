package Java;

class Math {
    int left, right, third;
    int forth = 0;

    public void setOprand(int left, int right, int third) {
        System.out.println("setOprand(int left, int right, int third)");
        this.left = left;
        this.right = right;
        this.third = third;
    }

    public int setOprand(int left, int right, int third, int forth) {
        System.out.println("setOprand(int left, int right, int third, int forth)");
        this.setOprand(left, right, third);
        this.forth = forth;
        return left + right + third + forth;
    }

}

public class Calculation {
    public static void main(String[] args) {
        Math m = new Math();
        m.setOprand(10, 20, 30);
        m.setOprand(10, 20, 30, 40);
    }
}
