#!/bin/bash

echo "Enter the radius of the circle: "
read radius 


area=$(echo "scale=2; 3.14159 * ($radius ^ 2)" | bc -l)
circumference=$(echo "scale=2; 2 * 3.14159 * $radius" | bc -l)


echo "Area of the circle: $area"
echo "Circumference of the circle: $circumference"
