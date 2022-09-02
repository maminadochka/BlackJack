from tkinter import *
from tkinter import ttk
from Server import *
from BlackJack import *
from tkinter import messagebox


def listen_server():
    try:
        server = Server(port.get(), int(decks))
        label_info['text'] = server.info_port()
        server.s.listen()
        messagebox.showinfo("Connection", "[*] Waiting for Connections...")
    except:
        messagebox.showerror("ERROR", "Error!")
        return

    while server.in_game is False:
        conn, addr = server.s.accept()
        if conn not in [player.connection for player in server.players]:
            data = conn.recv(1024)
            player = Player(data.decode())
            player.set_connection(conn)
            server.players.append(player)
            if len(server.players) == numb_user.get():
                server.in_game = True
                server.broadcast('[*] All players have joined the game')
                label_info['text'] = "[*] Game start"
    game = Blackjack(server.players, server.decks)

    game.play()


server_window = Tk()
server_window.geometry("550x550+550+100")
server_window.title("Server")
server_window.configure(bg="gray")
server_window.resizable(False, False)

label_info = Label(server_window, font='Courier 15', bg="gray", fg="white")
label_info.place(x=20, y=50)

Label(server_window, text="Enter port:", font='Courier 15', bg="gray", fg="white").place(x=20, y=100)

port = IntVar()
name_port = Entry(server_window, width=83, textvariable=port)
name_port.place(x=20, y=150)

Label(server_window, text="Enter number of players:", font='Courier 15', bg="gray", fg="white").place(x=20, y=200)

numb_user = IntVar()
numb = Entry(server_window, width=83, textvariable=numb_user)
numb.place(x=20, y=270)

Label(server_window, text="Enter number of decks:", font='Courier 15', bg="gray", fg="white").place(x=20, y=396)

combo = ttk.Combobox(server_window, values=[1, 2, 3, 4, 5], state="readonly")
combo.place(x=380, y=400)
combo.current(0)

decks = combo.get()

start = Button(server_window, width=40, height=2, text="START GAME", bg="white", command=listen_server)
start.place(x=130, y=440)


server_window.mainloop()
