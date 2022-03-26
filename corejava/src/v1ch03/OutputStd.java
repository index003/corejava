package v1ch03;

import java.util.Date;

public class OutputStd {
    public static void main(String[] args) {
        double  x = 1000.0 / 3.0;
        System.out.println(x);
        System.out.printf("%8.2f\n", x);
        String name = "Victor";
        int age = 42;
        System.out.printf("Hello %s. Next year, you'll be %d.\n", name, age);
        System.out.printf("%tc\n", new Date());
        System.out.printf("%s %tB %<te, %<tY\n", "Due date:", new Date());
    }
}
