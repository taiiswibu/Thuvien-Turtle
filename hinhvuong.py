import turtle

# Tạo một cửa sổ đồ họa và đặt tên là "Goku"
window = turtle.Screen()
window.title("Goku")

# Tạo một Turtle và đặt màu sắc và độ dày cho đường vẽ
goku = turtle.Turtle()
goku.color("red")
goku.pensize(5)

# Vẽ hình vuông bằng cách di chuyển Turtle
goku.forward(100)
goku.right(90)
goku.forward(100)
goku.right(90)
goku.forward(100)
goku.right(90)
goku.forward(100)

# Đóng cửa sổ đồ họa khi kết thúc
turtle.done()
