class Circle {
    int radius;
    Point center;

    Circle(int radius, Point center) {
        this.radius = radius;
        this.center = center;
    }

    double area() {
        return Math.PI * radius * radius;
    }

    double perimeter() {
        return 2 * Math.PI * radius;
    }

    boolean intersect(Circle otherCircle) {

        double distance = Math.sqrt(Math.pow(center.x - otherCircle.center.x, 2) +
                Math.pow(center.y - otherCircle.center.y, 2));

        return (radius + otherCircle.radius) >= distance;
    }
}