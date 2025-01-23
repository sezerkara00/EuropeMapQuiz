import turtle
import pandas

# Ekranı oluştur
screen = turtle.Screen()
screen.title("Avrupa Haritası")
image = "C:/Users/sezer/Desktop/udemy/py/day25_avrupaOyunu/Avrupa.gif"  # Avrupa haritasının yolu
screen.addshape(image)
turtle.shape(image)

# Ekran boyutunu ayarlama (haritanın boyutuna göre)
screen.setup(width=800, height=600)  # Gerekirse boyutları ayarlayın

# Koordinatları yazdıracak fonksiyon
def get_mouse_click_coor(x, y):
    print(f"Tıkladığınız koordinatlar: ({x}, {y})")
    
    # Kullanıcıdan ülke adını al
    country_name = screen.textinput(title="Ülke Adı", prompt="Hangi ülke?").strip()
    
    # Yeni CSV dosyasına yazma
    with open("day25_avrupaOyunu/countries_coordinates.csv", "a") as file:
        file.write(f"{country_name},{x},{y}\n")
    
    # Yazıyı belirtilen koordinatta yazdır
    yazici = turtle.Turtle()
    yazici.hideturtle()  # Turtle'ı gizle
    yazici.penup()
    yazici.goto(x, y)  # Koordinatlara git
    yazici.pendown()
    yazici.color("red")  # Yazı rengi
    yazici.write(country_name, align="center", font=("Arial", 12, "bold"))  # Yazıyı yazdır

# Mevcut ülkeleri CSV dosyasından oku ve haritada göster
def display_existing_countries():
    try:
        with open("day25_avrupaOyunu/countries_coordinates.csv") as file:
            for line in file:
                if line.strip():  # Eğer satır boş değilse
                    parts = line.strip().split(",")
                    if len(parts) == 3:  # Eğer üç parçaya ayrılabiliyorsa
                        country_name, x, y = parts
                        try:
                            # Koordinatları float'a dönüştürmeden önce kontrol et
                            x_float = float(x)
                            y_float = float(y)
                            # Yazıyı belirtilen koordinatta yazdır
                            yazici = turtle.Turtle()
                            yazici.hideturtle()  # Turtle'ı gizle
                            yazici.penup()
                            yazici.goto(x_float, y_float)  # Koordinatlara git
                            yazici.pendown()
                            yazici.color("black")  # Yazı rengi
                            yazici.write(country_name, align="center", font=("Arial", 18, "bold"))  # Yazıyı yazdır
                        except ValueError:
                            print(f"Hatalı koordinat: x={x}, y={y}")  # Hatalı koordinatları yazdır
    except FileNotFoundError:
        print("CSV dosyası bulunamadı. Henüz ülke eklenmemiş olabilir.")

# Turtle nesnesini oluştur
yazici = turtle.Turtle()
yazici.hideturtle()  # Turtle'ı gizle

# Mevcut ülkeleri göster
display_existing_countries()

# Mouse tıklama olayını bağla
turtle.onscreenclick(get_mouse_click_coor)

# Turtle döngüsünü başlat
turtle.mainloop()
