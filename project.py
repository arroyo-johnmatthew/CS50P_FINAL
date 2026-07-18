import tkinter as tk
import webbrowser
from tkinter import ttk

def switch_frame(show, hide):
    hide.pack_forget()
    show.pack(fill="both", expand=True)

def redirect(num):
    links = [
        "https://www.sss.gov.ph/become-an-sss-member/",
        "https://memberinquiry.philhealth.gov.ph/member/pinApplication.xhtml",
        "https://www.pagibigfundservices.com/virtualpagibig/Membership.aspx",
        ]
    webbrowser.open(links[num])

def main():
    # set root widget
    root = tk.Tk()
    root.geometry("500x350")
    root.title("Corporate Buddy")

    # set the bg color and size then call the widgets
    root.configure(background="#FFFFFF")
    root.resizable(False, False)
    widgets, widgets2 = get_widgets(root)

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

    # SSS
    button = tk.Button(reg_frame,
                        text="SSS", 
                        font=("Arial", 11, "bold"), 
                        width=13,
                        relief="raised",
                        bg="#a9d6e5",
                        activebackground="white",
                        activeforeground="#a9d6e5",
                        fg="white",
                        command=lambda: redirect(0),
                        cursor="hand2",
                        bd=0,
                        padx=30)
    button.place(x=159, y=100)

    # Philhealth
    button = tk.Button(reg_frame,
                        text="PHILHEALTH", 
                        font=("Arial", 11, "bold"), 
                        width=13,
                        relief="raised",
                        bg="#a9d6e5",
                        activebackground="white",
                        activeforeground="#a9d6e5",
                        fg="white",
                        command=lambda: redirect(1),
                        cursor="hand2",
                        bd=0,
                        padx=30)
    button.place(x=159, y=140)
    
    # Pagibig
    button = tk.Button(reg_frame,
                        text="PAGIBIG", 
                        font=("Arial", 11, "bold"), 
                        width=13,
                        relief="raised",
                        bg="#a9d6e5",
                        activebackground="white",
                        activeforeground="#a9d6e5",
                        fg="white",
                        command=lambda: redirect(2),
                        cursor="hand2",
                        bd=0,
                        padx=30)
    button.place(x=159, y=180)

    button = tk.Button(reg_frame,
                    text="⬅️ Return to Menu", 
                    font=("Arial", 11, "bold"), 
                    relief="flat",
                    activebackground="white",
                    activeforeground="#5c5d5e",
                    bg="white",
                    fg="#5c5d5e",
                    command=lambda: switch_frame(main_frame, reg_frame),
                    cursor="hand2",
                    bd=0,
                    padx=20)
    button.pack(pady=15, side="bottom")

    return main_frame, reg_frame

if __name__ == "__main__":
    main()