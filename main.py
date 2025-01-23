import turtle
import pandas

# Ekranı oluştur
screen = turtle.Screen()
screen.title("Europe Map")
image = "C:/Users/sezer/Desktop/udemy/py/day25_avrupaOyunu/Avrupa.gif"  # Avrupa haritasının yolu
screen.addshape(image)
turtle.shape(image)

# Ekran boyutunu ayarlama (haritanın boyutuna göre)
screen.setup(width=800, height=600)  # Gerekirse boyutları ayarlayın
data = pandas.read_csv("day25_avrupaOyunu/countries_coordinates.csv")

# Ülke isimlerini içeren referans listesi
countries_list = data.country.to_list()
guessed_states = []

while len(guessed_states) < len(countries_list):
    answer_state = screen.textinput(title=f"{len(guessed_states)}/{len(countries_list)} Countries Correct", prompt="Enter the name of a country (or type 'exit' to quit): ").title()
    
    if answer_state.lower() == "exit":  # Kullanıcı "exit" yazarsa oyunu bitir
        break
    
    if answer_state in countries_list:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.speed(0)
        t.hideturtle()
        t.penup()
        state_data = data[data.country == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state, align="center", font=("Arial", 18, "normal"))

# Oyun bitince bilemedikleri ülkeleri göster
for country in countries_list:
    if country not in guessed_states:
        t = turtle.Turtle()
        t.speed(0)
        t.hideturtle()
        t.penup()
        state_data = data[data.country == country]
        t.goto(int(state_data.x), int(state_data.y))
        
        # Siyah kenarlık için yazıyı önce siyah renkte yaz
        t.color("black")  # Kenarlık rengi
        t.write(country, align="center", font=("Arial", 19, "normal"))
        
        # Beyaz yazıyı üst üste yaz
        t.color("white")  # Yazı rengi
        t.write(country, align="center", font=("Arial", 18, "normal"))

screen.exitonclick()
