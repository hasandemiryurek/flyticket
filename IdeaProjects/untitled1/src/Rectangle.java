class Point {
    int x;
    int y;

    Point(int x, int y) {
        this.x = x;
        this.y = y;
    }
}

class Rectangle {
    int sideA;
    int sideB;
    Point topLeft;

    Rectangle(int sideA, int sideB, Point topLeft) {
        this.sideA = sideA;
        this.sideB = sideB;
        this.topLeft = topLeft;
    }

    int area() {
        return sideA * sideB;
    }

    int perimeter() {
        return 2 * (sideA + sideB);
    }

    Point[] corners() {
        Point[] corners = new Point[4];
        corners[0] = topLeft;
        corners[1] = new Point(topLeft.x + sideA, topLeft.y);
        corners[2] = new Point(topLeft.x + sideA, topLeft.y + sideB);
        corners[3] = new Point(topLeft.x, topLeft.y + sideB);
        return corners;
    }
}