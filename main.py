import tkinter as tk
from tkinter import filedialog
import createMap


def run_creat_map(file_path):
    createMap.drawMap(file_path)

def run_sample():
    createMap.drawMap()

def open_file_dialog():
    # 打开文件对话框，让用户选择txt文件
    file_path = tk.filedialog.askopenfilename(filetypes=[("map", "*.csv")])
    if file_path:
        # 如果用户选择了文件，就调用绘制地图的函数
        run_creat_map(file_path)

def main():
    root = tk.Tk()
    root.title("City planning support")
    root.geometry("300x175")
    root.resizable(0, 0)
    root.iconphoto(True, tk.PhotoImage(file='pictures/city_skyline.jpg'))

    openfile = tk.Button(root, text="Open a map", command=open_file_dialog, height=2, width=20)
    openfile.place(x=75, y=20)

    draw = tk.Button(root, text="Draw sample map", command=run_sample, height=2, width=20)
    draw.place(x=75, y=80)

    root.mainloop()

if __name__ == "__main__":
    main()