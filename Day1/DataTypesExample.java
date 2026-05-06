public class DataTypesExample {
    public static void main(String[] args) {
        // 🔸 Primitive Data Types
        byte b = 10;
        short s = 100;
        int i = 1000;
        long l = 100000L;
        float f = 10.5f;
        double d = 99.99;
        char c = 'A';
        boolean isJavaFun = true;

        // Displaying primitive data
        System.out.println("Byte value: " + b);
        System.out.println("Short value: " + s);
        System.out.println("Int value: " + i);
        System.out.println("Long value: " + l);
        System.out.println("Float value: " + f);
        System.out.println("Double value: " + d);
        System.out.println("Char value: " + c);
        System.out.println("Boolean value: " + isJavaFun);

        // 🔹 Non-Primitive Data Types
        String name = "Sakha Abhiram";
        int[] numbers = {1, 2, 3, 4, 5};

        System.out.println("String value: " + name);
        System.out.println("Array first element: " + numbers[0]);
    }
}
