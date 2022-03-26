package v1ch04;

import java.util.Random;

public class ConstructorTest {
    public static void main(String[] args) {
        // fill the staff array with three employee objects
        Employee2[] staff = new Employee2[3];
        staff[0] = new Employee2("Harry",40000);
        staff[1] = new Employee2(60000);
        staff[2] = new Employee2();

        // print out information about all Employee objects
        for (Employee2 e : staff) {
            System.out.println("Name = " + e.getName() +
                    ",Salary = " + e.getSalary() +
                    ",id = " + e.getId());
        }
    }
}

class Employee2 {
    private static int nextId;
    private int id;
    // 实例域初始化
    private String name = "";   // instance field initialization
    private double salary;
    // 静态初始化块
    // static initialization block
    static {
        Random generator = new Random();
        // set nextId to a random number between 0 to 9999
        nextId = generator.nextInt(10000);
    }
    // 对象初始化 new的时候调用
    // object initialization block
    {
        id = nextId;
        nextId++;
    }

    // three overload constructors
    public Employee2 (String name, double salary) {
        this.name = name;
        this.salary = salary;
    }
    // 调用另外一个构造器
    public Employee2(double s) {
        // calls the Employee2(String, double) constructor
        this("Employee2 #" + nextId, s);
    }
    // 无参构造器
    // the default constructor
    public Employee2() {
        // name initialized "" -- see above
        // salary not explicitly set -- initialized to 0
        // id initialized in initialization block
    }

    public int getId() {
        return id;
    }

    public String getName() {
        return name;
    }

    public double getSalary() {
        return salary;
    }

    public void raiseSalary(double byPercent) {
        double raise = salary * byPercent / 100;
        salary += raise;
    }
}
