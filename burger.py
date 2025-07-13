import tkinter as tk

root = tk.Tk()
root.title("Burger ka Sa'kin - Mark Lenard Baluyot")

canvas = tk.Canvas(root, width=600, height=400, bg="#5317A1")
canvas.pack()

x0, y0 = 200, 120
width, height = 200, 160

# Top bun
top_bun_arc = canvas.create_arc(
    x0, y0, x0 + width, y0 + 80,
    start=0, extent=180,
    fill="#d99a2b",
    outline="#a66c12",
    width=3,
    style=tk.PIESLICE
)
top_bun_rect = canvas.create_rectangle(
    x0, y0 + 40, x0 + width, y0 + 60,
    fill="#d99a2b",
    outline="#a66c12",
    width=3
)

# Lettuce
lettuce = canvas.create_rectangle(x0 + 5, y0 + 60, x0 + width - 5, y0 + 75, fill="#4CAF50", outline="#388E3C")

# Tomato
tomato = canvas.create_rectangle(x0 + 10, y0 + 75, x0 + width - 10, y0 + 90, fill="#e53935", outline="#b71c1c")

# Onions
onion1 = canvas.create_rectangle(x0 + 15, y0 + 90, x0 + 50, y0 + 95, fill="#9c27b0", outline="#6a1b9a")
onion2 = canvas.create_rectangle(x0 + 55, y0 + 90, x0 + 90, y0 + 95, fill="#9c27b0", outline="#6a1b9a")
onion3 = canvas.create_rectangle(x0 + 95, y0 + 90, x0 + width - 15, y0 + 95, fill="#9c27b0", outline="#6a1b9a")

# Cheese slice
cheese = canvas.create_polygon(
    x0 + 15, y0 + 95, x0 + width - 15, y0 + 95,
    x0 + width - 25, y0 + 110, x0 + 25, y0 + 110,
    fill="#FFEB3B", outline="#FBC02D"
)

# Pickles
pickle1 = canvas.create_oval(x0 + 20, y0 + 110, x0 + 40, y0 + 120, fill="#7CB342", outline="#558B2F")
pickle2 = canvas.create_oval(x0 + 50, y0 + 110, x0 + 70, y0 + 120, fill="#7CB342", outline="#558B2F")
pickle3 = canvas.create_oval(x0 + 80, y0 + 110, x0 + 100, y0 + 120, fill="#7CB342", outline="#558B2F")

# Bacon strips
bacon1 = canvas.create_rectangle(x0 + 110, y0 + 110, x0 + 140, y0 + 120, fill="#A0522D", outline="#7B3F00")
bacon2 = canvas.create_rectangle(x0 + 145, y0 + 110, x0 + 175, y0 + 120, fill="#A0522D", outline="#7B3F00")

# Patty 1
patty1 = canvas.create_rectangle(x0 + 20, y0 + 120, x0 + width - 20, y0 + 140, fill="#4E342E", outline="#3E2723")

# Cheese slice 2
cheese2 = canvas.create_polygon(
    x0 + 15, y0 + 140, x0 + width - 15, y0 + 140,
    x0 + width - 25, y0 + 155, x0 + 25, y0 + 155,
    fill="#FFEB3B", outline="#FBC02D"
)

# Patty 2
patty2 = canvas.create_rectangle(x0 + 20, y0 + 155, x0 + width - 20, y0 + 175, fill="#4E342E", outline="#3E2723")

# Bottom bun
bottom_bun_rect = canvas.create_rectangle(
    x0, y0 + 175, x0 + width, y0 + 195,
    fill="#d99a2b",
    outline="#a66c12",
    width=2
)
bottom_bun_arc = canvas.create_arc(
    x0, y0 + 150, x0 + width, y0 + 230,
    start=180, extent=180,
    fill="#d99a2b",
    outline="#a66c12",
    width=2,
    style=tk.PIESLICE
)

# Name label
name_text = canvas.create_text(x0 + width // 2, y0 + 105, text="Mark Lenard Baluyot", font=("Arial", 12, "bold"), fill="black")

# Grouping all parts
burger_parts = [
    top_bun_arc, top_bun_rect,
    lettuce, tomato,
    onion1, onion2, onion3,
    cheese,
    pickle1, pickle2, pickle3,
    bacon1, bacon2,
    patty1,
    cheese2,
    patty2,
    bottom_bun_rect, bottom_bun_arc,
    name_text
]

# Movement
dx, dy = 2, 2
is_moving = True  # Animation control flag

def move_burger():
    global dx, dy
    if is_moving:
        for part in burger_parts:
            canvas.move(part, dx, dy)

        x1, y1, x2, y2 = canvas.bbox(top_bun_arc)

        if x1 <= 0 or x2 >= 600:
            dx *= -1
        if y1 <= 0 or y2 >= 250:
            dy *= -1

    canvas.after(15, move_burger)

# Pause and play functions
def pause_burger():
    global is_moving
    is_moving = False

def play_burger():
    global is_moving
    if not is_moving:
        is_moving = True
        move_burger()

# Buttons
button_frame = tk.Frame(root, bg="#5317A1")
button_frame.pack(pady=10)

pause_button = tk.Button(button_frame, text="Pause", command=pause_burger, bg="#f44336", fg="white", font=("Arial", 10, "bold"))
pause_button.pack(side=tk.LEFT, padx=10)

play_button = tk.Button(button_frame, text="Play", command=play_burger, bg="#4CAF50", fg="white", font=("Arial", 10, "bold"))
play_button.pack(side=tk.LEFT, padx=10)

# Start animation
move_burger()

root.mainloop()