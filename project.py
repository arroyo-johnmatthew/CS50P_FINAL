import tkinter as tk
import webbrowser

def main():
    # set root widget
    root = tk.Tk()
    root.geometry("500x350")
    root.title("Corporate Buddy")

    # set the bg color and size then call the widgets
    root.configure(background="#FFFFFF")
    root.resizable(False, False)
    widgets= get_widgets(root)

    # run the GUI
    widgets.pack(fill="both", expand=True)
    root.mainloop()

# TODO create a function that its param is an int and returns an int
def display_sal(val=0):
    return val 

def calculate(entry, state_label, salary_label):
    # get the entry value
    user_value = entry.get()

    # check if the value is empty
    if not user_value.strip():
        state_label.config(text="No input", fg="red")

    # if not, check if it is negative number,  a string. otherwise, it is a success
    else:
        try:
            user_value = int(entry.get())  

            if user_value < 0:
                state_label.config(text="Negative number is not allowed", fg="red")
            else:
                # Calculations and results will display on this block
                state_label.config(text="Success!", fg="green")
                salary_label.config(text=f"PHP{display_sal(user_value):,}", fg="green")

        except ValueError:
            state_label.config(text="Input must be a number", fg="red")

def switch_frame(show, hide):
    hide.pack_forget()
    show.pack(fill="both", expand=True)

def redirect(num):
    links = (
        "https://www.sss.gov.ph/become-an-sss-member/",
        "https://memberinquiry.philhealth.gov.ph/member/pinApplication.xhtml",
        "https://www.pagibigfundservices.com/virtualpagibig/Membership.aspx",
    )
    webbrowser.open(links[num])

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
                    command=lambda: switch_frame(tax_frame, main_frame),
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

    # =====================    TAX FRAME  =============================  
    tax_frame = tk.Frame(parent, bg="white")

    # tax calculator input (nested frame)
    nested_frame_1 = tk.Frame(tax_frame, bg="#a8dadc", relief="groove")
    nested_frame_1.place(x=10, y=50, height=200, width=230)

    # Monthly Salary label
    label = tk.Label(nested_frame_1, 
                     text="Monthly Salary", 
                     bg="#a8dadc", 
                     font=("Arial", 11, "bold"))
    label.pack(pady=(40, 9))

    # input field
    entry = tk.Entry(nested_frame_1, relief="flat", justify="center")
    entry.pack(pady=10)
    
    # submit button
    button = tk.Button(nested_frame_1,
                        text="Submit", 
                        font=("Arial", 8, "bold"), 
                        width=10,
                        relief="raised",
                        activebackground="#a9d6e5",
                        activeforeground="white",
                        bg="#1d3557",
                        fg="white",
                        cursor="hand2",
                        command=lambda: calculate(entry, error_label, label_sal),
                        bd=0,
                        padx=5)
    button.pack()

    # error label
    error_label = tk.Label(nested_frame_1, text="", bg="#a8dadc")
    error_label.pack(side="bottom", anchor="center", pady=(0,5))

    # display deductions (nested frame)
    nested_frame_2 = tk.Frame(tax_frame, bg="#a8dadc", )
    nested_frame_2.place(x=258, y=50, height=200, width=230)

    # You will receive
    label = tk.Label(nested_frame_2, 
                     text="You will receive", 
                     bg="#a8dadc", 
                     font=("Arial", 14, "bold"))
    label.pack(pady=(10, 0))
    label_sal = tk.Label(nested_frame_2, 
                     text="PHP", 
                     bg="#a8dadc",
                     fg="green", 
                     font=("Arial", 14, "bold"))
    label_sal.pack(pady=(1, 0))

    # sss
    label_sss = tk.Label(nested_frame_2, 
                     text="SSS: ", 
                     bg="#a8dadc",
                     fg="black", 
                     font=("Arial", 9))
    label_sss.pack(side="top", anchor="w", pady=(20,3))

    # philhealth
    label_philhealth = tk.Label(nested_frame_2, 
                     text="PHILHEALTH: ", 
                     bg="#a8dadc",
                     fg="black", 
                     font=("Arial", 9))
    label_philhealth.pack(side="top", anchor="w", pady=(0,5))

    # pagibig
    label_pagibig = tk.Label(nested_frame_2, 
                     text="PAGIBIG: ", 
                     bg="#a8dadc",
                     fg="black", 
                     font=("Arial", 9))
    label_pagibig.pack(side="top", anchor="w", pady=(0,5))

    # return to menu
    button = tk.Button(tax_frame,
                    text="⬅️ Return to Menu", 
                    font=("Arial", 11, "bold"), 
                    relief="flat",
                    activebackground="white",
                    activeforeground="#5c5d5e",
                    bg="white",
                    fg="#5c5d5e",
                    command=lambda: (error_label.config(text=""), 
                                     label_sal.config(text="PHP"), 
                                     entry.delete(0, "end"),
                                     switch_frame(main_frame, tax_frame)),
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

    # Return button
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

    return main_frame

if __name__ == "__main__":
    main()