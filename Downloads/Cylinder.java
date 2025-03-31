public class Cylinder {
    // Class variable to track the number of Cylinder objects created
    private static int count = 0;

    // Instance variables for radius and height
    private double radius;
    private double height;

    // Parameterized constructor to initialize dimensions
    public Cylinder(double radius, double height) {
        this.radius = radius;
        this.height = height;
        count++; // Increment count when a new object is created
    }

    // Method to calculate surface area of the cylinder
    public double calculateSurfaceArea() {
        return 2 * Math.PI * radius * (radius + height);
    }

    // Method to calculate volume of the cylinder
    public double calculateVolume() {
        return Math.PI * radius * radius * height;
    }

    // Accessor method for radius
    public double getRadius() {
        return radius;
    }

    // Mutator method for radius
    public void setRadius(double radius) {
        this.radius = radius;
    }

    // Accessor method for height
    public double getHeight() {
        return height;
    }

    // Mutator method for height
    public void setHeight(double height) {
        this.height = height;
    }

    // Accessor method for count
    public static int getCount() {
        return count;
    }

    // main function is optional
    public static void main(String[] args) {
        // Example usage
        Cylinder cylinder1 = new Cylinder(3, 5);
        System.out.println("Surface Area: " + cylinder1.calculateSurfaceArea()); // Output: Surface Area: 150.79644737231007
        System.out.println("Volume: " + cylinder1.calculateVolume()); // Output: Volume: 141.3716694115407
    }
}
