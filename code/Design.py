from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import socket

ClientSocket = socket.socket()
host = '127.0.0.1'

state = ""

ClientSocketSocket = socket.socket()

menu_back_color = '#1f4f16'
window_back_color = '#006400'


def waiting():
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            ClientSocket.connect((host, port.get()))
            ClientSocket.sendall(name.get().encode())
    except socket.error:
        messagebox.showerror("ERROR", "Check the number of port")
        return

    while True:
        response = ClientSocket.recv(1024)
        answer = response.decode('utf-8')
        if answer == '[*] All players have joined the game':
            break
    game()


def game():
    def recv_round_text():
        response = ClientSocket.recv(1024)
        answer = response.decode('utf-8')
        while answer != "end":
            if answer == "point":
                ClientSocket.send(str.encode("sent"))
                response = ClientSocket.recv(1024)
                answer = response.decode('utf-8')
               # messagebox.showerror("ERROR9", answer)
                player_points.delete(0, END)
                player_points.insert(0, str(answer))
            else:
                player_text.insert(END, answer)
            response = ClientSocket.recv(1024)
            answer = response.decode('utf-8')
            ClientSocket.send(str.encode("sent"))

    def recv_text():
        response = ClientSocket.recv(1024)
        answer = response.decode('utf-8')
        while answer != "end":
            if answer == "results":
                ClientSocket.send(str.encode("sent"))
                response = ClientSocket.recv(1024)
                answer = response.decode('utf-8')
                messagebox.showinfo("End_of_the_round1", answer)
                ClientSocket.send(str.encode("sent"))
                response = ClientSocket.recv(1024)
                answer = response.decode('utf-8')
                wins_text.delete('1.0', END)
                wins_text.insert('1.0', answer)
                ClientSocket.send(str.encode("sent"))
            elif answer == "exit":
                messagebox.showinfo("End_of_the_Game", "The deck is over")
                window.destroy()
                break
            elif answer == "point":
                ClientSocket.send(str.encode("sent"))
                response = ClientSocket.recv(1024)
                answer = response.decode('utf-8')
               # messagebox.showerror("ERROR3", answer)
                player_points.delete(0, END)
                player_points.insert(0, str(answer))
            elif answer == "point_dealer":
                ClientSocket.send(str.encode("sent"))
                response = ClientSocket.recv(1024)
                answer = response.decode('utf-8')
            else:
                player_text.insert(END, answer)
            ClientSocket.send(str.encode("sent"))
            response = ClientSocket.recv(1024)
            answer = response.decode('utf-8')

    def exit():
        ClientSocket.send(str.encode("exit_play"))
        window.destroy()

    def yes():
        response = ClientSocket.recv(1024)
        answer = response.decode('utf-8')
        if answer == "y/n":
            ClientSocket.send(str.encode("y"))
        recv_text()

    def no():
        response = ClientSocket.recv(1024)
        answer = response.decode('utf-8')
        if answer == "y/n":
            ClientSocket.send(str.encode("n"))
            messagebox.showinfo("End_of_the_round", "The round will end after the dealer's move")  # сделать вывод в label ОЧКИ
        recv_text()

    def game_progress():
        player_text.delete('1.0', END)
        ClientSocket.send(str.encode("play"))
        recv_round_text()

    menu.destroy()

    # Основное окно для игры
    window = Tk()
    window.geometry("500x500+550+100")
    window.title("BlackJack")
    window.configure(bg=window_back_color)
    window.resizable(False, False)

    Label(window, text=user.get(), font=20, bg=window_back_color, fg="white").place(x=30, y=20)

    Label(window, text="Number of points:", font="Arial 15", bg=window_back_color, fg="white").place(x=275, y=140)

    Label(window, text="Total score:", font="Arial 15", bg=window_back_color, fg="white").place(x=290, y=20)

    player_points = Entry(window, font=15, bg=window_back_color, fg="white", width=8)
    player_points.place(x=370, y=170)

    player_text = Text(window, width=27, height=22)
    player_text.place(x=10, y=50)

    wins_text = Text(window, width=27, height=3)
    wins_text.place(x=270, y=50)
    wins_text.insert('1.0', 'Here you can see the total score after the round')

    take_card = Button(window, width=20, height=2, text="Take a card", bg="#08457e", fg="white", command=yes)
    take_card.place(x=290, y=270)

    refuse_card = Button(window, width=20, height=2, text="Don't take a card", bg="#08457e", fg="white", command=no)
    refuse_card.place(x=290, y=320)

    new_round = Button(window, width=30, height=1, text="New round", bg="#08457e", fg="white", command=game_progress)
    new_round.place(x=20, y=430)

    end_round = Button(window, width=30, height=1, text="End game", bg="#08457e", fg="white", command=exit)
    end_round.place(x=265, y=430)
    window.mainloop()


# Окно меню
menu = Tk()
menu.geometry("550x550+550+100")
menu.title("Меню")
menu.configure(bg=menu_back_color)
menu.resizable(False, False)

img = ImageTk.PhotoImage(Image.open("K:\\курсовая реп\\blackjack.jpg"))
b = Label(image=img)
b.place(x=10, y=30)
b.pack()

Label(menu, text="Enter your name:", font='Courier 15', bg=menu_back_color, fg="white").place(x=20, y=342)

user = StringVar()
name = Entry(menu, width=83, textvariable=user)
name.place(x=20, y=370)

Label(menu, text="Enter port:", font='Courier 15', bg=menu_back_color, fg="white").place(x=20, y=400)

port = IntVar()
name_port = Entry(menu, width=26, textvariable=port)
name_port.place(x=190, y=400)

start = Button(menu, width=40, height=2, text="CONNECT", bg="white", command=waiting)
start.place(x=130, y=440)

stop = Button(menu, width=40, height=2, text="EXIT", bg="white", command=menu.destroy)
stop.place(x=130, y=490)

menu.mainloop()
