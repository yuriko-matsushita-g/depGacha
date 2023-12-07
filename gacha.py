import tkinter as tk
from tkinter import ttk
import tkinter.font as tkFont
from PIL import Image, ImageTk
import pandas as pd
import random

def load_data(csv_path):
    # CSVファイルの読み込み
    return pd.read_csv(csv_path)

def display_random_person(data):
    # 「配属区分」が"主務"である行だけをフィルタリング
    filtered_data = data[data['配属区分'] == "主務"]

    # フィルタリングされたデータからランダムに選択
    if not filtered_data.empty:
        person = filtered_data.sample().iloc[0]
        result_label.config(text=f"{person['名前']} - {person['組織フルパス']}")
        # GIF再生が終了したので、テキストを表示する
        result_label.place(relx=0.5, rely=0.5, anchor='center')
    else:
        result_label.config(text="該当する人はいません")
        result_label.place(relx=0.5, rely=0.5, anchor='center')

gif_frame = 0

def play_gif():
    # GIFアニメーションの再生
    global gif_label, gif_frame

    # GIF再生開始時にテキストを非表示にする
    result_label.place_forget()

    gif_frame += 1
    try:
        gif_label.config(image=gif_frames[gif_frame])
        window.after(100, play_gif)  # 100ミリ秒ごとにフレーム更新
    except IndexError:
        gif_frame = 0
        display_random_person(data)  # GIF再生終了時にテキストを表示

csv_path = "members.csv"
gif_path = "gacha.gif"

data = load_data(csv_path)

# Tkinterウィンドウの初期化
window = tk.Tk()
window.title("ガチャガチャアプリケーション")

# GIFの読み込みとフレームの準備
gif = Image.open(gif_path)
gif_frames = []
for i in range(gif.n_frames):
    gif.seek(i)
    frame = ImageTk.PhotoImage(image=gif.copy())
    gif_frames.append(frame)

gif_label = ttk.Label(window, image=gif_frames[0])
gif_label.pack()

start_button = ttk.Button(window, text="ガチャを回す", command=play_gif)
start_button.pack()

fontStyle = tkFont.Font(family="Lucida Grande", size=20)

# tk.Labelを使用して背景色を白に設定
result_label = tk.Label(window, text="", font=fontStyle, bg="white")
# result_label.place(relx=0.5, rely=0.5, anchor='center')  # 初期状態では表示しない

window.mainloop()
