#Библиотеки
from tkinter import *
import random
from PIL import Image, ImageTk
import pygame


def main():
    root = Tk() #окно
    root.resizable(width=False, height=False) #нельзя поменять размер окошки
    root.geometry("1080x720")   #размер окошки

    pygame.mixer.init()  #библиотека звука

    pygame.mixer.music.load("bgmusic/music.mp3")
    pygame.mixer.music.set_volume(0.1) #громкость
    pygame.mixer.music.play(-1) #музыка играет бесконечно

    click_sound = pygame.mixer.Sound("btsound/button.mp3") #звук клика

    root.title("Rock Paper Scissors") # Название окошки
    root.iconbitmap(r'rock-paper-scissors.ico') #иконка .exe файла

    #фон
    background_image = Image.open("img/background.jpg")
    background_photo = ImageTk.PhotoImage(background_image)
    background_label = Label(root, image=background_photo)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    name = Label(root, text="Rock Paper Scissors - Human vs Computer", font="150", bg="LightSteelBlue")
    name.place(x="385", y="100")

    player = Label(root, text="Human", font="80", bg="LightSteelBlue")
    player.place(x="200", y="200")

    bot = Label(root, text="Computer", font="80", bg="LightSteelBlue")
    bot.place(x="800", y="200")

    #картинки
    rock_png = ImageTk.PhotoImage(file="img/Rock.png")
    paper_png = ImageTk.PhotoImage(file="img/Paper.png")
    scissor_png = ImageTk.PhotoImage(file="img/Scissors.png")
    human_png = ImageTk.PhotoImage(file="img/Human.png")
    robot_png = ImageTk.PhotoImage(file="img/Robot.png")
    reset_png= ImageTk.PhotoImage(file="img/Reset.png")

    human = Label(root, image=human_png, bg="LightSteelBlue")
    human.place(x="165", y="50")

    robot = Label(root, image=robot_png, bg="LightSteelBlue")
    robot.place(x="770", y=50)

    user_image = Label(root, image="", bg="LightSteelBlue")
    user_image.place(x="165", y="300")

    computer_image = Label(root, image="", bg="LightSteelBlue")
    computer_image.place(x="775", y="300")

    result = Label(root, text="", font="100", bg="LightSteelBlue")
    result.place(x="490", y="350")

    human_wins = 0
    computer_wins = 0

    score_label = Label(root, text="Score: Human {} - Computer {}".format(human_wins, computer_wins), font="12", bg="LightSteelBlue")
    score_label.place(x="430", y="400")

    def update_score(): #счет
        score_label.config(text="Score: Human {} - Computer {}".format(human_wins, computer_wins))

    def reset_score(): #сбросить счет
        nonlocal human_wins, computer_wins
        play_click_sound()
        human_wins = 0
        computer_wins = 0
        update_score()

    def play_click_sound(): #звуки клика
        click_sound.play()

    def Rock():
        nonlocal human_wins, computer_wins
        play_click_sound()
        user = "Rock"
        computer = random.choice(["Rock", "Paper", "Scissors"])
        user_image.config(image=rock_png)

        if user == computer:
            result.config(text="Tie")
            computer_image.config(image=rock_png)
        elif computer == "Paper":
            computer_wins += 1
            result.config(text="Computer Win")
            computer_image.config(image=paper_png)
        else:
            human_wins += 1
            result.config(text="Human Win")
            computer_image.config(image=scissor_png)

        update_score()

    b1 = Button(root, image=rock_png, bg="LightSteelBlue", font="Arial 12", text="Rock", compound=TOP, command=Rock)
    b1.place(x="320", y="500")

    def Paper():
        nonlocal human_wins, computer_wins
        play_click_sound()
        user = "Paper"
        computer = random.choice(["Rock", "Paper", "Scissors"])
        user_image.config(image=paper_png)

        if user == computer:
            result.config(text="Tie")
            computer_image.config(image=paper_png)
        elif computer == "Scissors":
            computer_wins += 1
            result.config(text="Computer Win")
            computer_image.config(image=scissor_png)
        else:
            human_wins += 1
            result.config(text="Human Win")
            computer_image.config(image=rock_png)

        update_score()

    b2 = Button(root, image=paper_png, bg="LightSteelBlue", font="Arial 12", text="Paper", compound=TOP, command=Paper)
    b2.place(x="460", y="500")

    def Scissors():
        nonlocal human_wins, computer_wins
        play_click_sound()
        user = "Scissors"
        computer = random.choice(["Rock", "Paper", "Scissors"])
        user_image.config(image=scissor_png)

        if user == computer:
            result.config(text="Tie")
            computer_image.config(image=scissor_png)
        elif computer == "Paper":
            human_wins += 1
            result.config(text="Human Win")
            computer_image.config(image=paper_png)
        else:
            computer_wins += 1
            result.config(text="Computer Win")
            computer_image.config(image=rock_png)
        update_score()

    b3 = Button(root, image=scissor_png, bg="LightSteelBlue", font="Arial 12", text="Scissors", compound=TOP, command=Scissors)
    b3.place(x=600, y=500)

    #кнопка сброса счета
    reset_button = Button(root, image=reset_png, text="Reset Score", compound=TOP,command=reset_score, font="Arial 10", bg="LightSteelBlue")
    reset_button.place(x="0", y="600")

    root.mainloop()

if __name__ == "__main__":
    main()
