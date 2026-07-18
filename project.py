import tkinter as tk
import webbrowser
from tkinter import ttk

def validate():
    pass

def switch_frame(show, hide):
    hide.pack_forget()
    show.pack(fill="both", expand=True)

def main():
    # set root widget
    root = tk.Tk()
    root.geometry("500x350")
    root.title("Corporate Buddy")

    # set the bg color and size then call the widgets
    root.configure(background="#FFFFFF")
    root.resizable(False, False)
    widgets = get_widgets(root)

    # run the GUI
    widgets.pack(fill="both", expand=True)
    root.mainloop()


def get_widgets(parent):
    # =====================    MAIN FRAME  ============================= 
    main_frame = tk.Frame(parent)
    main_frame.configure(bg="white")

    # set the text
    label = tk.Label(main_frame, 
                     text="🇵🇭 Corporate Buddy", 
                     font=("Arial", 21, "bold"), 
                     bg="white")
    label.pack(pady=20)

    # set the buttons
    button = tk.Button(main_frame,
                    text="Tax Calculator", 
                    font=("Arial", 11, "bold"), 
                    width=10,
                    relief="raised",
                    bg="#a9d6e5",
                    activebackground="white",
                    activeforeground="#a9d6e5",
                    fg="white",
                    command=lambda: switch_frame(reg_frame, main_frame),
                    cursor="hand2",
                    bd=0,
                    padx=20)
    button.pack(pady=8)

    button = tk.Button(main_frame,
                    text="Setup Your Government Contributions", 
                    font=("Arial", 11, "bold"), 
                    relief="flat",
                    activebackground="white",
                    activeforeground="#5c5d5e",
                    bg="white",
                    fg="#5c5d5e",
                    command=lambda: switch_frame(reg_frame, main_frame),
                    cursor="hand2",
                    bd=0,
                    padx=20)
    button.pack(pady=15, side="bottom")

    # =====================    REGISTER FRAME  =============================  
    reg_frame = tk.Frame(parent)
    reg_frame.config(bg="white")

    # set the label (Click to Register)
    label = tk.Label(reg_frame, 
                     text="Click to Register", 
                     font=("Arial", 21, "bold"), 
                     bg="white")
    label.pack(pady=20)

    # define all the 3 buttons and the return button
    button = tk.Button(reg_frame,
                        text="⬅️ Return to Menu", 
                        font=("Arial", 11, "bold"), 
                        width=13,
                        relief="raised",
                        bg="#a9d6e5",
                        activebackground="white",
                        activeforeground="#a9d6e5",
                        fg="white",
                        command=lambda: switch_frame(main_frame, reg_frame),
                        cursor="hand2",
                        bd=0,
                        padx=30)
    button.pack(pady=20, side="bottom")

    return main_frame

if __name__ == "__main__":
    main()