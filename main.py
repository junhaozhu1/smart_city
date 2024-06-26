import tkinter as tk
from tkinter import filedialog, messagebox
import createMap
import csv
import os
import subprocess

def run_creat_map(file_path):
    open_distance_window()
    createMap.drawMap(file_path)

def run_sample():
    open_distance_window()
    createMap.drawMap()
    

def open_distance_window():
    # Create a new top-level window
    distance_window = tk.Toplevel()
    distance_window.title("Operation")
    distance_window.geometry("200x150")
    distance_window.resizable(0, 0)

    # Button to calculate and show the shortest distance
    calc_button = tk.Button(distance_window, text="    Show Report    ",
                            command=calculate_and_show_shortest_distance)
    calc_button.pack(pady=20)

    sugg_button = tk.Button(distance_window, text="Show Suggestions",
                            command=calculate_and_show_shortest_distance)
    sugg_button.config(state="disabled")
    sugg_button.pack(pady=20)

def calculate_and_show_shortest_distance():
    # Replace 'shortest.py' with the appropriate script and function call
    script_path = os.path.abspath('shortest.py')
    process = subprocess.Popen(['python', script_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()

    if process.returncode == 0:
        messagebox.showinfo("Shortest Distance", output.decode())
    else:
        messagebox.showerror("Error", error.decode())

def open_file_dialog():
    # 打开文件对话框，让用户选择txt文件
    file_path = tk.filedialog.askopenfilename(filetypes=[("map", "*.csv")])
    if file_path:
        # 如果用户选择了文件，就调用绘制地图的函数
        run_creat_map(file_path)

def create_new_map():
    return 0


def main():
    root = tk.Tk()
    root.title("City Planning Support")
    root.geometry("300x225")
    root.resizable(0, 0)
    root.iconphoto(True, tk.PhotoImage(file='pictures/city_skyline.jpg'))

    openfile = tk.Button(root, text="Open a map", command=open_file_dialog, height=2, width=20)
    openfile.place(x=75, y=20)

    draw = tk.Button(root, text="Create a new map", command=create_new_map, height=2, width=20)
    draw.config(state="disabled")
    draw.place(x=75, y=80)

    draw = tk.Button(root, text="Draw sample map", command=run_sample, height=2, width=20)
    draw.place(x=75, y=140)

    root.mainloop()

if __name__ == "__main__":
    main()