import tkinter
from tkinter import messagebox
import time
from threading import Thread


def main():

    def show_info():
        messagebox.showinfo('Info','Tang')
    
    class DownloadTasHandlerk(Thread):

        def run(self):
            time.sleep(10)
            tkinter.messagebox.showinfo('提示', '下载完成!')
            button1.config(state=tkinter.NORMAL)

    def download():
        button1.config(state=tkinter.DISABLED)
        DownloadTaskHandler(daemon=True).start()

    top = tkinter.Tk()
    top.title("单线程")
    top.geometry('200x100')
    top.wm_attributes('-topmost', True)

    panel = tkinter.Frame(top)
    button1 = tkinter.Button(panel, text='Download', command=download)
    button1.pack(side='left')
    button2 = tkinter.Button(panel, text='About', command=show_info)
    button2.pack(side='right')
    panel.pack(side='bottom')

    tkinter.mainloop()



if __name__=="__main__":
    main()