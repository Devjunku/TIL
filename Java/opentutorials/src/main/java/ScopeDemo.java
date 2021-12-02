class C {
  int left, right;

  public C(int left, int right) {
      this.left = left;
      this.right = right;
  }

  public void sum() {
      System.out.println(this.left + this.right);
  }

  public void avg() {
      System.out.println((this.left + this.right)/2);
  }

}

public class ScopeDemo {
    public static void main(String[] args) {
        C c1 = new C(10, 20);
        c1.sum();
        c1.avg();

        C c2 = new C(20, 40);
        c2.sum();
        c2.avg();

    }
}