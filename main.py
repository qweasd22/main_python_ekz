import cv2
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import filedialog


def detect_faces(frame):
    # Преобразуем кадр в оттенки серого
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Используем классификатор Хаара для обнаружения лиц
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    # Рисуем прямоугольники вокруг обнаруженных лиц
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

    return frame

def show_frame():
    ret, frame = cap.read()

    if not ret:
        print("Конец видео или ошибка при чтении кадра")
        return

    # Ваш код для обработки кадра и обнаружения лиц
    frame = detect_faces(frame)

    # Отображение изображения в GUI
    cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
    img = Image.fromarray(cv2image)
    imgtk = ImageTk.PhotoImage(image=img)
    label.imgtk = imgtk
    label.configure(image=imgtk) 

    label.after(10, show_frame)

def open_file():
    global cap
    file_path = filedialog.askopenfilename()
    if file_path:
        cap = cv2.VideoCapture(file_path)
        if not cap.isOpened():
            print("Не удалось открыть файл")
        else:
            show_frame()

# Создание окна Tkinter
root = tk.Tk()
root.title("Обнаружение лиц")
root.state('zoomed')


# Кнопка для выбора файла
button = tk.Button(root, text="Выбрать файл", command=open_file)
button.pack()

# Метка для отображения изображения
label = tk.Label(root)
label.pack()

root.mainloop()