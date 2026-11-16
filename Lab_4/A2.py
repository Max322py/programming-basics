n = int(input())
m = int(input())
print("ПРЯМОУГОЛЬНИК 5x10:")
for i in range(n):
    print("#" * m)
print("ПРАВЫЙ ТРЕУГОЛЬНИК:") 
for i in range(n):
    print("#"*(i+1))
print("РАМКА 5*10:")
print("#" * m)
for i in range(n-2):
    print("#", " " * (m-2), "#", sep="")
print("#" * m)