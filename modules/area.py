def circle(radius:float) -> None:
    area = 3.14 * radius * radius
    print(f"Aread of circle with radius : {area}")

def rectangle(length:float , breath:float) -> None:
    area = length * breath
    print(f"Area of rectangle :{area}")

def triangle(base:float , height:float )-> None:
    area = 0.5 * height * base 
    print(f"Area of Traingle: {area}")


# here we will implement a name dunder method 


if __name__ == "__main__":
    
  circle(45.99)
  triangle(21,21)