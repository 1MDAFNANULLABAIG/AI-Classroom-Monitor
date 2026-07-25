import tkinter as tk
from tkinter import messagebox
import os
import cv2

from database import register_student

os.makedirs("dataset", exist_ok=True)


def capture_faces(student_id):
    folder = os.path.join("dataset", student_id)
    os.makedirs(folder, exist_ok=True)

    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        messagebox.showerror("Error", "Could not open camera.")
        return

    count = 0

    while True:

        ret, frame = cap.read()

        if not ret:
            break

        cv2.putText(
            frame,
            f"Captured: {count}/100",
            (20, 30),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (0, 255, 0),
            2
        )

        cv2.imshow("Capture Faces", frame)

        key = cv2.waitKey(1) & 0xFF

        if key == ord("c"):
            count += 1
            cv2.imwrite(
                os.path.join(folder, f"{count}.jpg"),
                frame
            )

        elif key == ord("q"):
            break

        if count >= 100:
            break

    cap.release()
    cv2.destroyAllWindows()


def save_student():

    student_id = entry_id.get().strip()
    student_name = entry_name.get().strip()
    department = entry_dept.get().strip()
    semester = entry_sem.get().strip()
    section = entry_sec.get().strip()

    if student_id == "" or student_name == "":
        messagebox.showerror(
            "Error",
            "Student ID and Name are required."
        )
        return

    register_student(
        student_id,
        student_name,
        department,
        semester,
        section
    )

    capture_faces(student_id)

    messagebox.showinfo(
        "Success",
        "Student Registered Successfully!"
    )


root = tk.Tk()
root.title("AI Classroom Student Registration")
root.geometry("450x420")
root.resizable(False, False)

tk.Label(
    root,
    text="Student Registration",
    font=("Arial", 18, "bold")
).pack(pady=15)

tk.Label(root, text="Student ID").pack()
entry_id = tk.Entry(root, width=40)
entry_id.pack()

tk.Label(root, text="Student Name").pack()
entry_name = tk.Entry(root, width=40)
entry_name.pack()

tk.Label(root, text="Department").pack()
entry_dept = tk.Entry(root, width=40)
entry_dept.pack()

tk.Label(root, text="Semester").pack()
entry_sem = tk.Entry(root, width=40)
entry_sem.pack()

tk.Label(root, text="Section").pack()
entry_sec = tk.Entry(root, width=40)
entry_sec.pack()

tk.Button(
    root,
    text="Register Student",
    command=save_student,
    width=25,
    height=2,
    bg="green",
    fg="white"
).pack(pady=25)

root.mainloop()