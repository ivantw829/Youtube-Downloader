from tkinter import *
from pytube import YouTube


def download():
    x.set("---下載中---")
    try:
        yt = YouTube(links.get())
        video = yt.streams.get_by_resolution("720p")
        video.download()
    except Exception as error:
        x.set(F"下載發生錯誤：{error}")
    else:
        x.set(yt.title + "下載成功")


window = Tk()
window.title("Youtube Downloader")

x = StringVar()
links = StringVar()
x.set("Youtube Downloader")

lab1 = Label(window, text="輸入要下載的影片網址 : ").grid(row=0)
lab2 = Label(window, textvariable=x,
             height=3).grid(row=2, column=0, columnspan=2)

e1 = Entry(window, textvariable=links)
e1.grid(row=0, column=1)


btn2 = Button(window, text="關閉", command=window.destroy)
btn2.grid(row=3, column=0)
btn1 = Button(window, text="下載", command=download)
btn1.grid(row=3, column=1)

window.mainloop()
