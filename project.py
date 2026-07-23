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
def display_take_home_pay(val, sss, philhealth, pagibig):
    total = sss + philhealth + pagibig
    return val - total

def sss_deduction(salary):
    if salary < 5000:
        return 250
    elif salary >= 5000 and salary <= 35000:
        return salary * 0.05
    elif salary > 35000: 
        return 1750

def philhealth_deduction(salary):
    if salary < 10000:
        return 250
    elif salary >= 10000 and salary <= 100000:
        return salary * 0.025
    elif salary > 100000:
        return 2500

def pagibig_deduction(salary):
    if salary <= 1500:
        return salary * 0.01
    elif salary > 1500 and salary < 10000:
        return salary * 0.02
    elif salary >= 10000:
        return 200

# This is the function that will run once the button "submit" is pressed
def calculate(entry, state_label, salary_label):
    # get the entry value
    user_value = entry.get()

    # initialize the gov contribution deduction variables
    sss = 0
    philhealth = 0
    pagibig = 0

    # check if the value is empty
    if not user_value.strip():
        state_label.config(text="No input", fg="red")

    # if not, check if it is negative number,  a string. otherwise, it is a success
    else:
        try:
            user_value = float(entry.get())  

            if user_value < 0:
                state_label.config(text="Negative number is not allowed", fg="red")
            else:
                # Calculations and results will display on this block

                # Get the SSS deduction price
                sss = sss_deduction(user_value)
                philhealth = philhealth_deduction(user_value)
                pagibig = pagibig_deduction(user_value)

                # Display the take home pay
                state_label.config(text="Success!", fg="green")
                salary_label.config(
                    text=f"PHP{display_take_home_pay(
                        user_value, 
                        sss, 
                        philhealth, 
                        pagibig):,.2f}", 
                    fg="green"
                )

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

    # sss_deduction_frame
    sss_frame = tk.Frame(nested_frame_2, bg="#a8dadc")
    label_sss = tk.Label(sss_frame, 
                     text="SSS: ", 
                     bg="#a8dadc",
                     fg="black", 
                     font=("Arial", 9))
    label_sss.pack(side="left", anchor="w", padx=(0,140))
    label_sss_deduction = tk.Label(sss_frame, 
                         text="-P250.00", 
                         bg="#a8dadc",
                         fg="red", 
                         font=("Arial", 9))
    label_sss_deduction.pack(side="left", anchor="w")
    sss_frame.pack(pady=(15,0))

    # philhealth_deduction_frame
    philhealth_frame = tk.Frame(nested_frame_2, bg="#a8dadc")
    label_philhealth = tk.Label(philhealth_frame, 
                        text="PHILHEALTH: ", 
                        bg="#a8dadc",
                        fg="black", 
                        font=("Arial", 9))
    label_philhealth.pack(side="left", anchor="w", padx=(0,90))
    label_philhealth_deduction = tk.Label(philhealth_frame, 
                            text="-P250.00", 
                            bg="#a8dadc",
                            fg="red", 
                            font=("Arial", 9))
    label_philhealth_deduction.pack(side="left", anchor="w")
    philhealth_frame.pack(pady=(0,0))

    # pagibig_deduction_frame
    pagibig_frame = tk.Frame(nested_frame_2, bg="#a8dadc")
    label_pagibig = tk.Label(pagibig_frame, 
                        text="PAGIBIG: ", 
                        bg="#a8dadc",
                        fg="black", 
                        font=("Arial", 9))
    label_pagibig.pack(side="left", anchor="w", padx=(0,117))
    label_pagibig_deduction = tk.Label(pagibig_frame, 
                            text="-P250.00", 
                            bg="#a8dadc",
                            fg="red", 
                            font=("Arial", 9))
    label_pagibig_deduction.pack(side="left", anchor="w")
    pagibig_frame.pack(pady=(0,0))

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