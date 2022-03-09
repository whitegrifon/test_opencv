import tkinter as tk
import time
from tkinter import ttk
import cv2
import numpy as np
a=0
b=0
c=0
a_1=0
b_1=0
c_1=0
a1_1=0
b1_1=0
c1_1=0
a1_2=0
b1_2=0
c1_2=0
a2_1=0
b2_1=0
c2_1=0
a2_2=0
b2_2=0
c2_2=0
root = tk.Tk()
root.geometry('1000x480')
root.resizable(False, False)
root.title('Fucking slider')

value_1 = tk.DoubleVar()
value_2 = tk.DoubleVar()
value_3 = tk.DoubleVar()
value_4 = tk.DoubleVar()
value_5 = tk.DoubleVar()
value_6 = tk.DoubleVar()
value_7 = tk.DoubleVar()
value_8 = tk.DoubleVar()
value_9 = tk.DoubleVar()
value_10 = tk.DoubleVar()
value_11 = tk.DoubleVar()
value_12 = tk.DoubleVar()
value_13 = tk.DoubleVar()
value_14 = tk.DoubleVar()
value_15 = tk.DoubleVar()
value_16 = tk.DoubleVar()
value_17 = tk.DoubleVar()
value_18 = tk.DoubleVar()


label1=ttk.Label(text='h_min', foreground="#00FF00")
label2=ttk.Label(text='s_min', foreground="#00FF00")
label3=ttk.Label(text='v_min', foreground="#00FF00")
label4=ttk.Label(text='h_max', foreground="#00FF00")
label5=ttk.Label(text='s_max', foreground="#00FF00")
label6=ttk.Label(text='v_max', foreground="#00FF00")

label7=ttk.Label(text='h_min_master', foreground="#CC0033")
label8=ttk.Label(text='s_min_master', foreground="#CC0033")
label9=ttk.Label(text='v_min_master', foreground="#CC0033")
label10=ttk.Label(text='h_max_master', foreground="#CC0033")
label11=ttk.Label(text='s_max_master', foreground="#CC0033")
label12=ttk.Label(text='v_max_master', foreground="#CC0033")

label13=ttk.Label(text='h_min_slave', foreground="#CC0033")
label14=ttk.Label(text='s_min_slave', foreground="#CC0033")
label15=ttk.Label(text='v_min_slave', foreground="#CC0033")
label16=ttk.Label(text='h_max_slave', foreground="#CC0033")
label17=ttk.Label(text='s_max_slave', foreground="#CC0033")
label18=ttk.Label(text='v_max_slave', foreground="#CC0033")

label1.grid(column=1, row=0)
label2.grid(column=1, row=1)
label3.grid(column=1, row=2)
label4.grid(column=1, row=3)
label5.grid(column=1, row=4)
label6.grid(column=1, row=5)

label7.grid(column=1, row=6)
label8.grid(column=1, row=7)
label9.grid(column=1, row=8)
label10.grid(column=1, row=9)
label11.grid(column=1, row=10)
label12.grid(column=1, row=11)

label13.grid(column=1, row=12)
label14.grid(column=1, row=13)
label15.grid(column=1, row=14)
label16.grid(column=1, row=15)
label17.grid(column=1, row=16)
label18.grid(column=1, row=17)

#count

label1=ttk.Label(text='h_min', foreground="#00FF00")
label2=ttk.Label(text='s_min', foreground="#00FF00")
label3=ttk.Label(text='v_min', foreground="#00FF00")
label4=ttk.Label(text='h_max', foreground="#00FF00")
label5=ttk.Label(text='s_max', foreground="#00FF00")
label6=ttk.Label(text='v_max', foreground="#00FF00")

label7=ttk.Label(text='h_min_master', foreground="#CC0033")
label8=ttk.Label(text='s_min_master', foreground="#CC0033")
label9=ttk.Label(text='v_min_master', foreground="#CC0033")
label10=ttk.Label(text='h_max_master', foreground="#CC0033")
label11=ttk.Label(text='s_max_master', foreground="#CC0033")
label12=ttk.Label(text='v_max_master', foreground="#CC0033")

label13=ttk.Label(text='h_min_slave', foreground="#CC0033")
label14=ttk.Label(text='s_min_slave', foreground="#CC0033")
label15=ttk.Label(text='v_min_slave', foreground="#CC0033")
label16=ttk.Label(text='h_max_slave', foreground="#CC0033")
label17=ttk.Label(text='s_max_slave', foreground="#CC0033")
label18=ttk.Label(text='v_max_slave', foreground="#CC0033")

label1.grid(column=1, row=0)
label2.grid(column=1, row=1)
label3.grid(column=1, row=2)
label4.grid(column=1, row=3)
label5.grid(column=1, row=4)
label6.grid(column=1, row=5)

label7.grid(column=1, row=6)
label8.grid(column=1, row=7)
label9.grid(column=1, row=8)
label10.grid(column=1, row=9)
label11.grid(column=1, row=10)
label12.grid(column=1, row=11)

label13.grid(column=1, row=12)
label14.grid(column=1, row=13)
label15.grid(column=1, row=14)
label16.grid(column=1, row=15)
label17.grid(column=1, row=16)
label18.grid(column=1, row=17)

slider_1 = ttk.Scale(
    root, from_=0,
    to=360,
    orient='horizontal',
    variable=value_1
)
slider_2 = ttk.Scale(
    root, from_=0,
    to=360,
    orient='horizontal',
    variable=value_2
)
slider_3 = ttk.Scale(
    root, from_=0,
    to=360,
    orient='horizontal',
    variable=value_3
)
slider_4 = ttk.Scale(
    root, from_=0,
    to=360,
    orient='horizontal',
    variable=value_4
)
slider_5 = ttk.Scale(
    root, from_=0,
    to=360,
    orient='horizontal',
    variable=value_5
)
slider_6 = ttk.Scale(
    root, from_=0,
    to=360,
    orient='horizontal',
    variable=value_6
)
slider_7 = ttk.Scale(
    root, from_=0,
    to=360,
    orient='horizontal',
    variable=value_7
)
slider_8 = ttk.Scale(
    root, from_=0,
    to=360,
    orient='horizontal',
    variable=value_8
)
slider_9 = ttk.Scale(
    root, from_=0,
    to=360,
    orient='horizontal',
    variable=value_9
)
slider_10 = ttk.Scale(
    root, from_=0,
    to=360,
    orient='horizontal',
    variable=value_10
)
slider_11 = ttk.Scale(
    root, from_=0,
    to=360,
    orient='horizontal',
    variable=value_11
)
slider_12 = ttk.Scale(
    root, from_=0,
    to=360,
    orient='horizontal',
    variable=value_12
)
slider_13 = ttk.Scale(
    root, from_=0,
    to=360,
    orient='horizontal',
    variable=value_13
)
slider_14 = ttk.Scale(
    root, from_=0,
    to=360,
    orient='horizontal',
    variable=value_14
)
slider_15 = ttk.Scale(
    root, from_=0,
    to=360,
    orient='horizontal',
    variable=value_15
)
slider_16 = ttk.Scale(
    root, from_=0,
    to=360,
    orient='horizontal',
    variable=value_16
)
slider_17 = ttk.Scale(
    root, from_=0,
    to=360,
    orient='horizontal',
    variable=value_17
)
slider_18 = ttk.Scale(
    root, from_=0,
    to=360,
    orient='horizontal',
    variable=value_18
)
slider_1.grid(column=0, row=0, sticky='w')
slider_2.grid(column=0, row=1, sticky='w')
slider_3.grid(column=0, row=2, sticky='w')
slider_4.grid(column=0, row=3, sticky='w')
slider_5.grid(column=0, row=4, sticky='w')
slider_6.grid(column=0, row=5, sticky='w')
slider_7.grid(column=0, row=6, sticky='w')
slider_8.grid(column=0, row=7, sticky='w')
slider_9.grid(column=0, row=8, sticky='w')
slider_10.grid(column=0, row=9, sticky='w')
slider_11.grid(column=0, row=10, sticky='w')
slider_12.grid(column=0, row=11, sticky='w')
slider_13.grid(column=0, row=12, sticky='w')
slider_14.grid(column=0, row=13, sticky='w')
slider_15.grid(column=0, row=14, sticky='w')
slider_16.grid(column=0, row=15, sticky='w')
slider_17.grid(column=0, row=16, sticky='w')
slider_18.grid(column=0, row=17, sticky='w')

text_values = []
labels = []
start_row = 0
for i in range(18):
    text_values.append(tk.StringVar())
    labels.append(ttk.Label(textvariable=text_values[i], foreground="#000000"))
    labels[i].grid(column=2, row=start_row + i)

# label1_1 = ttk.Label(textvariable=text_values[0], foreground="#00FF00")
# label2_1 = ttk.Label(textvariable=text_values[1], foreground="#00FF00")
# label3_1 = ttk.Label(text=c, foreground="#00FF00")
# label4_1 = ttk.Label(text=a_1, foreground="#00FF00")
# label5_1 = ttk.Label(text=b_1, foreground="#00FF00")
# label6_1 = ttk.Label(text=c_1, foreground="#00FF00")
#
# label7_1 = ttk.Label(text=a1_1, foreground="#CC0033")
# label8_1 = ttk.Label(text=b1_1, foreground="#CC0033")
# label9_1 = ttk.Label(text=c1_1, foreground="#CC0033")
# label10_1 = ttk.Label(text=a1_2, foreground="#CC0033")
# label11_1 = ttk.Label(text=b1_2, foreground="#CC0033")
# label12_1 = ttk.Label(text=c1_2, foreground="#CC0033")
#
# label13_1 = ttk.Label(text=a2_1, foreground="#CC0033")
# label14_1 = ttk.Label(text=b2_1, foreground="#CC0033")
# label15_1 = ttk.Label(text=c2_1, foreground="#CC0033")
# label16_1 = ttk.Label(text=a2_2, foreground="#CC0033")
# label17_1 = ttk.Label(text=b2_2, foreground="#CC0033")
# label18_1 = ttk.Label(text=c2_2, foreground="#CC0033")

# label1_1.grid(column=2, row=0)
# label2_1.grid(column=2, row=1)
# label3_1.grid(column=2, row=2)
# label4_1.grid(column=2, row=3)
# label5_1.grid(column=2, row=4)
# label6_1.grid(column=2, row=5)
#
# label7_1.grid(column=2, row=6)
# label8_1.grid(column=2, row=7)
# label9_1.grid(column=2, row=8)
# label10_1.grid(column=2, row=9)
# label11_1.grid(column=2, row=10)
# label12_1.grid(column=2, row=11)
#
# label13_1.grid(column=2, row=12)
# label14_1.grid(column=2, row=13)
# label15_1.grid(column=2, row=14)
# label16_1.grid(column=2, row=15)
# label17_1.grid(column=2, row=16)
# label18_1.grid(column=2, row=17)

cap = cv2.VideoCapture(0)

while True:
    root.update_idletasks()
    root.update()
    a=int(value_1.get())
    text_values[0].set(str(a))
    b=int(value_2.get())
    text_values[1].set(str(b))
    c=int(value_3.get())
    text_values[2].set(str(c))
    a_1=int(value_4.get())
    text_values[3].set(str(a_1))
    b_1=int(value_5.get())
    text_values[4].set(str(b_1))
    c_1=int(value_6.get())
    text_values[5].set(str(c_1))

    a1_1=int(value_7.get())
    text_values[6].set(str(a1_1))
    b1_1=int(value_8.get())
    text_values[7].set(str(b1_1))
    c1_1=int(value_9.get())
    text_values[8].set(str(c1_1))

    a1_2=int(value_10.get())
    text_values[9].set(str(a1_2))
    b1_2=int(value_11.get())
    text_values[10].set(str(b1_2))
    c1_2=int(value_12.get())
    text_values[11].set(str(c1_2))

    a2_1=int(value_13.get())
    text_values[12].set(str(a2_1))
    b2_1=int(value_14.get())
    text_values[13].set(str(b2_1))
    c2_1=int(value_15.get())
    text_values[14].set(str(c2_1))

    a2_2=int(value_16.get())
    text_values[15].set(str(a2_2))
    b2_2=int(value_17.get())
    text_values[16].set(str(b2_2))
    c2_2=int(value_18.get())
    text_values[17].set(str(c2_2))
    print(a,b,c)
    # time.sleep(0.4)
    # video_processing_callibrate(a,b,c)



    ret, frame = cap.read()
    if (ret == True):
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        hsv_min = (a, b, c)
        hsv_max = (a_1, b_1, c_1)

        hsv_min_r = (a1_1, b1_1, c1_1)
        hsv_max_r = (a1_2, b1_2, c1_2)

        hsv_min_r1 = (a2_1, b2_1, c2_1)
        hsv_max_r1 = (a2_2, b2_2, c2_2)

        ir = cv2.inRange(hsv, hsv_min, hsv_max)
        er = cv2.erode(ir, (7, 7), iterations=5)
        dil = cv2.dilate(er, (7, 7), iterations=7)
        ir_r = cv2.inRange(hsv, hsv_min_r, hsv_max_r)
        ir_r1 = cv2.inRange(hsv, hsv_min_r1, hsv_max_r1)
        ir_r2 = ir_r + ir_r1
        er_r = cv2.erode(ir_r2, (100, 100), iterations=5)
        dil_r = cv2.dilate(er_r, (100, 100), iterations=7)
        contours, hierarchy = cv2.findContours(dil.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        contours1, hierarchy1 = cv2.findContours(dil_r.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        for cnt in contours:
            rect = cv2.minAreaRect(cnt)
            box = cv2.boxPoints(rect)
            box = np.int0(box)
            area = cv2.contourArea(cnt)
            if area > 1000:
                cv2.drawContours(frame, [box], 0, (0, 255, 0), 2)
            x, y, w, h = cv2.boundingRect(cnt)
        for cnt in contours1:
            rect = cv2.minAreaRect(cnt)
            box = cv2.boxPoints(rect)
            box = np.int0(box)
            area_red = cv2.contourArea(cnt)
            if area_red > 1000:
                cv2.drawContours(frame, [box], 0, (0, 0, 255), 2)
            x1, y1, w1, h1 = cv2.boundingRect(cnt)

            # print('x,y,w,h for red', x1, y1, w1, h1, 'area for red', area_red, 'center for red', x1 + w1, y1 + h1)
            # print('x,y,w,h', x, y, w, h, 'area', area, 'center', x + w, y + h)
        cv2.imshow('red', dil_r)
        cv2.imshow('v-f', dil)
        cv2.imshow('w-f', frame)
        if cv2.waitKey(100) & 0xFF == ord('q'):
            break
    if not (ret):
        break

cap.release()

cv2.destroyAllWindows()