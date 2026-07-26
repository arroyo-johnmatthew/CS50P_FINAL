# 💼 🇵🇭 CORPORATE BUDDY 💼

## 📓 Overview
- #### Video Demo:
- #### Description: *This is my first python project called Corporate Buddy. It's a simple tax calculator tool tailored for pre-employment citizens here in the Philippines.*

## ❓ Why Create This Project?
- As someone who is also nearing to transition to the corporate life, I have always wondered how does my government deduct my salary? On what basis do they use to apply deductions? I'm sure that others also have the same questions which is why I decided to create a simple tax calculator that follows the **2026 Philippine BIR Tax Rules**.

- Together with the **Government Statutory Contribution Rules**, this calculator can accurately display the take home pay with decimal (float) values.

## 🚦 Business Logic
- As stated above, the codebase strictly follows the **Philippine Statutory Deductions and Tax Business Rules**. 

- For context, SSS, Philhealth, and Pagibig are the three primary government-mandated benefits for workers in the Philippines. 

- They form a safety net covering retirement, housing, and healthcare.

    - SSS is the primary social insurance program. It provides monthly pension once you reach retirement, sickness benefits, maternity leave pay, unemployment benefits, salary loans, and disaster loans.

        - How does it deduct your salary?

            - The contribution rate is **5.0%** of your monthly salary. This applies between ₱5,000.00 and  ₱35,000.
            
            - If the monthly salary is **less than** ₱5,000.00, the contribution defaults to a flat ₱250.00.

            - If the monthly salary is **greater than** ₱35,000, the contribution defaults to a flat ₱1,750.00.

            - To code this out, it would look something like this: 
            ```
            IF salary < 5000 THEN SSS = 250
            ELSE IF salary >= 5000 AND salary <= 35000 THEN SSS = salary * 0.05
            ELSE IF salary > 35000 THEN SSS = 1750
            ```
            
    - PhilHealth is the government-owned universal health insurance provider. It covers hospital room subsidies, doctor fees, surgical procedures, and outpatient treatments.

        - How does it deduct your salary?

            - The contribution rate is **2.5%** (employee share) of your monthly salary. This applies between ₱10,000.00 and ₱100,000.00.

            - If the monthly salary is **less than** ₱10,000.00, the contribution defaults to a flat ₱250.00.

            - If the monthly salary is **greater than** ₱100,000.00, the contribution caps at a flat ₱2,500.00.

            - To code this out, it would look something like this:
            ```
            IF salary < 10000 THEN PhilHealth = 250
            ELSE IF salary >= 10000 AND salary <= 100000 THEN PhilHealth = salary * 0.025
            ELSE IF salary > 100000 THEN PhilHealth = 2500
            ```

    - Pag-IBIG (HDMF) is the national housing and provident savings program. It provides low-interest housing loans, emergency multi-purpose loans, and tax-free savings dividends upon retirement.

        - How does it deduct your salary?

            - For monthly salaries **up to ₱1,500.00**, the contribution rate is **1.0%** of your salary.

            - For monthly salaries **between ₱1,500.00 and ₱10,000.00**, the contribution rate is **2.0%** of your salary.

            - For monthly salaries **₱10,000.00 and above**, the contribution caps at a flat ₱200.00.

            - To code this out, it would look something like this:
            ```
            IF salary <= 1500 THEN PagIBIG = salary * 0.01
            ELSE IF salary > 1500 AND salary < 10000 THEN PagIBIG = salary * 0.02
            ELSE IF salary >= 10000 THEN PagIBIG = 200
            ```

- **BIR Withholding Tax** is calculated based on your **Taxable Income** (Monthly Salary - the sum of SSS, Philhealth, and Pagibig deductions). It comes with progressive **Brackets**. This means that the bigger your Taxable Income is, the bigger the withholding tax will become.

    - **Bracket 1 (₱20,833.00 and below):** 0% tax (Exempt).

    - **Bracket 2 (₱20,833.01 to ₱33,332.00):** 15% of the excess over ₱20,833.00.

    - **Bracket 3 (₱33,332.01 to ₱66,666.00):** ₱1,875.00 base tax + 20% of the excess over ₱33,333.00.

    - **Bracket 4 (₱66,666.01 to ₱166,666.00):** ₱8,541.80 base tax + 25% of the excess over ₱66,667.00.

    - **Bracket 5 (₱166,666.01 to ₱666,666.00):** ₱33,541.80 base tax + 30% of the excess over ₱166,677.00.

    - **Bracket 6 (Above ₱666,666.00):** ₱183,541.80 base tax + 35% of the excess over ₱666,667.00.

    - To code this out, it would look something like this:
        ```
        IF taxable_income <= 20833 THEN Tax = 0
        ELSE IF taxable_income <= 33332 THEN Tax = (taxable_income - 20833) * 0.15
        ELSE IF taxable_income <= 66666 THEN Tax = 1875.00 + ((taxable_income - 33333) * 0.20)
        ELSE IF taxable_income <= 166666 THEN Tax = 8541.80 + ((taxable_income - 66667) * 0.25)
        ELSE IF taxable_income <= 666666 THEN Tax = 33541.80 + ((taxable_income - 166677) * 0.30)
        ELSE Tax = 183541.80 + ((taxable_income - 666677) * 0.35)
        ```
- To get your **Take Home Pay**, subtract the **Withholding Tax** from the **Taxable Income**

## 🛠️ Features
- **Tax Calculator** with take home pay and deduction labels. It also comes with comprehensive error handling messages displayed on the GUI

- **Quick Links**. These are the buttons where they take you to the respective SSS, Philhealth, and Pagibig online member registration website.

- **Exit Button**. Button that exits the program when clicked

## ✅ Dependencies Used
- **Tkinter** - Python's built-in module for creating the project's Graphical User Interfaces (GUI).
- **Webbrowser** - Python's built-in module used for linking the buttons for website redirections.
- **Sys** - Also a built-in module that was used for linking the `sys.exit()` function into the "Exit" button
- **Pytest** - A Python library that was used to conduct unit testing.

## 🧪 Testing
- **test_project.py** is where the project's unit testing was implemented. **NOTE** that these were the only functions that were tested. All of them are tested correctly and remarked as "passed":

    ```
    def get_taxable_income(val, sss, philhealth, pagibig)
    def get_overall_deductions(sss, philhealth, pagibig, withholding_tax)
    def sss_deduction(salary)
    def philhealth_deduction(salary)
    def pagibig_deduction(salary)
    def calculate_withholding_tax(txbl_inc)
    ```