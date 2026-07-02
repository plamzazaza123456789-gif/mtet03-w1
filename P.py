import tkinter as tk
from tkinter import messagebox

# ฟังก์ชันสำหรับการกดปุ่ม
def press(num):
    global equation_text
    equation_text = equation_text + str(num)
    equation_label.set(equation_text)

def equalpress():
    global equation_text
    try:
        # คำนวณผลลัพธ์
        total = str(eval(equation_text))
        equation_label.set(total)
        equation_text = total  # เก็บผลลัพธ์ไว้คำนวณต่อได้
    except ZeroDivisionError:
        messagebox.onerror("Error", "ไม่สามารถหารด้วยศูนย์ได้")
        clear()
    except:
        messagebox.showerror("Error", "สูตรคำนวณไม่ถูกต้อง")
        clear()

def clear():
    global equation_text
    equation_text = ""
    equation_label.set("")

# สร้างหน้าต่างหลัก
window = tk.Tk()
window.title("เครื่องคิดเลขสีม่วงสุดชิค")
window.geometry("350x500")
window.configure(bg="#2D1B4E") # สีพื้นหลังม่วงเข้ม

equation_text = ""
equation_label = tk.StringVar()

# หน้าจอแสดงผล
display_frame = tk.Frame(window, bg="#2D1B4E", padx=10, pady=20)
display_frame.pack(expand=True, fill="both")

label = tk.Label(display_frame, textvariable=equation_label, font=('Arial', 28), 
                 bg="#4A2E80", fg="#FFFFFF", anchor="e", padx=15, pady=15)
label.pack(expand=True, fill="both")

# โซนปุ่มกด
button_frame = tk.Frame(window, bg="#2D1B4E", padx=10, pady=10)
button_frame.pack(expand=True, fill="both")

# กำหนดสีปุ่มโทนม่วง-ชมพู
COLOR_NUM = "#6A329F"    # สีปุ่มตัวเลข (ม่วงสว่าง)
COLOR_OP = "#9C46D0"     # สีปุ่มเครื่องหมาย (ม่วงอมชมพู)
COLOR_CLEAR = "#E056FD"  # สีปุ่ม Clear (ชมพูสว่าง)
COLOR_EQUAL = "#4834D4"  # สีปุ่มเครื่องหมายเท่ากับ (น้ำเงินม่วง)
COLOR_TEXT = "#FFFFFF"   # สีตัวอักษร (ขาว)

# โครงสร้างปุ่ม (ข้อความ, แถว, คอลัมน์, สีพื้นหลัง, คำสั่ง)
buttons = [
    ('7', 1, 0, COLOR_NUM, lambda: press(7)), ('8', 1, 1, COLOR_NUM, lambda: press(8)), ('9', 1, 2, COLOR_NUM, lambda: press(9)), ('/', 1, 3, COLOR_OP, lambda: press('/')),
    ('4', 2, 0, COLOR_NUM, lambda: press(4)), ('5', 2, 1, COLOR_NUM, lambda: press(5)), ('6', 2, 2, COLOR_NUM, lambda: press(6)), ('*', 2, 3, COLOR_OP, lambda: press('*')),
    ('1', 3, 0, COLOR_NUM, lambda: press(1)), ('2', 3, 1, COLOR_NUM, lambda: press(2)), ('3', 3, 2, COLOR_NUM, lambda: press(3)), ('-', 3, 3, COLOR_OP, lambda: press('-')),
    ('C', 4, 0, COLOR_CLEAR, clear), ('0', 4, 1, COLOR_NUM, lambda: press(0)), ('.', 4, 2, COLOR_NUM, lambda: press('.')), ('+', 4, 3, COLOR_OP, lambda: press('+')),
]

# สร้างปุ่มลงใน Grid
for (text, row, col, bg_color, cmd) in buttons:
    btn = tk.Button(button_frame, text=text, font=('Arial', 18, 'bold'), 
                    bg=bg_color, fg=COLOR_TEXT, activebackground="#B53471", activeforeground="white",
                    bd=0, relief="flat", command=cmd)
    btn.grid(row=row, column=col, sticky="nsew", padx=5, pady=5)

# ปุ่มเครื่องหมายเท่ากับ (=) แถวล่างสุดแบบเต็มความกว้าง
equal_btn = tk.Button(button_frame, text='=', font=('Arial', 18, 'bold'), 
                      bg=COLOR_EQUAL, fg=COLOR_TEXT, activebackground="#B53471", activeforeground="white",
                      bd=0, relief="flat", command=equalpress)
equal_btn.grid(row=5, column=0, columnspan=4, sticky="nsew", padx=5, pady=5)

# ตั้งค่าให้ปุ่มขยายขนาดตามหน้าต่างได้สวยงาม
for i in range(4):
    button_frame.columnconfigure(i, weight=1)
for i in range(6):
    button_frame.rowconfigure(i, weight=1)

# เริ่มทำงานโปรแกรม
window.mainloop()