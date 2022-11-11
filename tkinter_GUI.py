# Import module
from tkinter import *
from PIL import ImageTk, Image
import tkinter as tk

# Create object
root = Tk()
root.title("MINDSPACE")
root.iconbitmap('F:/ANUSHKA/TE/HCI/Tkinter/Images/icon.ico')

# Adjust size
root.geometry("282x490")

# Add image file
bg = ImageTk.PhotoImage(Image.open("Images/background.png"))
# Create Canvas
canvas = Canvas(root, width=282, height=490)
canvas.grid(row=0, column=0)
# Display image
canvas.create_image(0, 0, image=bg, anchor="nw")

# Add Text
canvas.create_text(140, 100, text="What's on your mind?",
                   font=('PencilUL 10 bold'))
canvas.create_text(
    138, 130, text="Choose one option for now. You can", font=('Arial 8'))
canvas.create_text(
    138, 155, text="explore others later", font=('Arial 8'))

r = IntVar()
# r.set(0)
# test = ['test1', 'test2', 'test3', 'test4']

# Create Buttons
button1 = Radiobutton(
    root, text="Managing everday anxiety \n and stress", variable=r, value=1, padx=5, pady=5, activebackground="grey")
button2 = Radiobutton(root, text="Sleeping better", value=2, variable=r,
                      padx=37, pady=5, activebackground="grey")
button3 = Radiobutton(root, text="Being more active", variable=r,
                      value=3, padx=29.5, pady=5, activebackground="grey")
button4 = Radiobutton(root, text="Trying something new", variable=r,
                      value=4, padx=18.5, pady=5, activebackground="grey")
button5 = Radiobutton(root, text="Staying focused",
                      variable=r, value=5, padx=36.4, pady=5, activebackground="grey")

# Display Buttons
button1_canvas = canvas.create_window(50, 180,
                                      anchor="nw",
                                      window=button1)
button2_canvas = canvas.create_window(49, 240,
                                      anchor="nw",
                                      window=button2)

button3_canvas = canvas.create_window(48, 285, anchor="nw",
                                      window=button3)

button4_canvas = canvas.create_window(47, 330, anchor="nw",
                                      window=button4)

button5_canvas = canvas.create_window(46, 375, anchor="nw",
                                      window=button5)


def Continue1():
    global bg1, img_1, new_image_1, img_2, new_image_2
    # Toplevel object which will be treated as next page
    newWindow = Toplevel(root)

    # sets the title of the Toplevel widget
    newWindow.title("MINDSPACE")
    newWindow.iconbitmap('F:/ANUSHKA/TE/HCI/Tkinter/Images/icon.ico')
    # sets the geometry of toplevel
    newWindow.geometry("282x490")

    # Add image file
    bg1 = PhotoImage(file="Images/background.png")
    # Show image using label
    label = Label(newWindow, image=bg1)
    label.place(x=0, y=0)

    # Frame
    frame_1 = tk.Frame(newWindow, width="308", height="128", bg='white')
    frame_1.place(x=1, y=115)

    label_1 = tk.Label(
        newWindow, text="Let's create your meditation", bg='white', font=('Calibri 16 bold'), fg='darkblue')
    label_1.place(x=12, y=90)
    label_2 = tk.Label(
        newWindow, text="practice.", bg='white', font=('Calibri 16 bold'), fg='darkblue')
    label_2.place(x=12, y=125)
    label_3 = tk.Label(
        newWindow, text="Relax your mind with meditations you can", bg='white', font=('Calibri 9'))
    label_3.place(x=12, y=165)
    label_4 = tk.Label(
        newWindow, text="listen to anytime.", bg='white', font=('Calibri 9'))
    label_4.place(x=12, y=189)

    img_1 = Image.open("Images/bulletpoints.jpg")
    resized_image_1 = img_1.resize((35, 35))
    new_image_1 = ImageTk.PhotoImage(resized_image_1)
    label_5 = Label(newWindow, image=new_image_1)
    label_5.place(x=15, y=240)

    label_6 = tk.Label(
        newWindow, text="Life-long skills", bg='white', font=('Calibri 10 bold'))
    label_6.place(x=50, y=230)

    label_7 = tk.Label(
        newWindow, text="Learn simple techniques to help you", bg='white', font=('Calibri 9'))
    label_7.place(x=50, y=250)

    label_8 = tk.Label(
        newWindow, text="on your mindfulness journey.", bg='white', font=('Calibri 9'))
    label_8.place(x=50, y=268)

    img_2 = Image.open("Images/bulletpoints1.jpg")
    resized_image_2 = img_2.resize((35, 35))
    new_image_2 = ImageTk.PhotoImage(resized_image_2)
    label_9 = Label(newWindow, image=new_image_2)
    label_9.place(x=15, y=312)

    label_10 = tk.Label(
        newWindow, text="Singles and Courses", bg='white', font=('Calibri 10 bold'))
    label_10.place(x=50, y=303)

    label_11 = tk.Label(
        newWindow, text="Search meditations from stress to", bg='white', font=('Calibri 9'))
    label_11.place(x=50, y=323)

    label_12 = tk.Label(
        newWindow, text="everyday anxiety and more.", bg='white', font=('Calibri 9'))
    label_12.place(x=50, y=341)

    button7 = tk.Button(newWindow, text="Continue",
                        padx=36.4, pady=5, bg='#4472C4', fg='white', command=Continue2).place(x=72, y=400)
    # button7_canvas = canvas.create_window(72, 428, anchor="nw",
    #                                       window=button7)


def Continue2():
    global bg2, new_image_3, new_image_4, new_image_5, new_image_6, new_image_7, new_image_9
    newWindow = Toplevel(root)

    # sets the title of the Toplevel widget
    newWindow.title("MINDSPACE")
    newWindow.iconbitmap('F:/ANUSHKA/TE/HCI/Tkinter/Images/icon.ico')
    # sets the geometry of toplevel
    newWindow.geometry("282x490")

    # Add image file
    bg2 = PhotoImage(file="Images/background.png")
    # Show image using label
    label = Label(newWindow, image=bg2)
    label.place(x=0, y=0)

    img_3 = Image.open("Images/profile.png")
    resized_image_3 = img_3.resize((28, 34))
    new_image_3 = ImageTk.PhotoImage(resized_image_3)
    label1 = Label(newWindow, image=new_image_3, bg='white')
    label1.place(x=40, y=65)

    img_4 = Image.open("Images/search.png")
    resized_image_4 = img_4.resize((28, 34))
    new_image_4 = ImageTk.PhotoImage(resized_image_4)
    label2 = Label(newWindow, image=new_image_4, bg='white')
    label2.place(x=213, y=65)

    label3 = tk.Label(
        newWindow, text="Focus Light", bg='white', font=('Calibri 15'))
    label3.place(x=90, y=90)
    label4 = tk.Label(
        newWindow, text="Focus music: 60 min", bg='white', font=('Calibri 7'))
    label4.place(x=97, y=116)

    button8 = tk.Button(newWindow, text="Play", font='Calibri 9 bold',
                        padx=15, pady=5, bg='#4472C4', fg='white', command=Play).place(x=107, y=140)

    label5 = tk.Label(
        newWindow, text="Featured", bg='white', font=('Calibri 15 bold'))
    label5.place(x=18, y=182)

    img_5 = Image.open("Images/img_5.png")
    resized_image_5 = img_5.resize((55, 35))
    new_image_5 = ImageTk.PhotoImage(resized_image_5)
    label6 = Label(newWindow, image=new_image_5)
    label6.place(x=18, y=230)

    label7 = tk.Label(
        newWindow, text="Organizing thoughts", bg='white', font=('Calibri 12 bold'), fg='#283F69')
    label7.place(x=80, y=227)

    label8 = tk.Label(
        newWindow, text="Meditation 7 min", bg='white', font=('Calibri 8'))
    label8.place(x=80, y=250)

    img_6 = Image.open("Images/img_6.png")
    resized_image_6 = img_6.resize((58, 35))
    new_image_6 = ImageTk.PhotoImage(resized_image_6)
    label10 = Label(newWindow, image=new_image_6)
    label10.place(x=16, y=292)

    label11 = tk.Label(
        newWindow, text="Study beats", bg='white', font=('Calibri 12 bold'), fg='#283F69')
    label11.place(x=80, y=289)

    label12 = tk.Label(
        newWindow, text="Focus music 54 min", bg='white', font=('Calibri 8'))
    label12.place(x=80, y=312)

    img_7 = Image.open("Images/img_7.png")
    resized_image_7 = img_7.resize((58, 38))
    new_image_7 = ImageTk.PhotoImage(resized_image_7)
    label10 = Label(newWindow, image=new_image_7)
    label10.place(x=16, y=354)

    label11 = tk.Label(
        newWindow, text="Breathing through exams", bg='white', font=('Calibri 12 bold'), fg='#283F69')
    label11.place(x=80, y=351)

    label12 = tk.Label(
        newWindow, text="Meditation 10 min", bg='white', font=('Calibri 8'))
    label12.place(x=80, y=374)

    #--------------------------------------------------------Footer------------------------------------------------------------------#
    img_9 = Image.open("Images/footer.png")
    resized_image9 = img_9.resize((282, 48))
    new_image_9 = ImageTk.PhotoImage(resized_image9)
    label = Label(newWindow, image=new_image_9)
    label.place(x=0, y=442)


def Play():
    global img_8
    newWindow = Toplevel(root)

    # sets the title of the Toplevel widget
    newWindow.title("MINDSPACE")
    newWindow.iconbitmap('F:/ANUSHKA/TE/HCI/Tkinter/Images/icon.ico')
    # sets the geometry of toplevel
    newWindow.geometry("304x429")

    # Add image file
    img_8 = ImageTk.PhotoImage(Image.open("Images/Music.png"))
    # Create Canvas
    canvas = Canvas(newWindow, width=304, height=429)
    canvas.grid(row=0, column=0)
    # Display image
    canvas.create_image(0, 0, image=img_8, anchor="nw")


button6 = Button(root, text="Continue",
                 padx=36.4, pady=5, bg='#4472C4', fg='white', command=Continue1)
button6_canvas = canvas.create_window(72, 420, anchor="nw",
                                      window=button6)
root.mainloop()
