from tkinter import *
from tkinter import messagebox
from pytube import YouTube
import tkinter.ttk as ttk

def download():
    save_file = "G:/youtube download"
    link = link_entry.get()
    resolution = resolution_var.get()
    if link:
        try:
            yt = YouTube(link)
            videos = yt.streams.filter(progressive=True)
            video = None
            if resolution == "All":
                video = yt.streams.first()
            else:
                video = yt.streams.filter(resolution=resolution).first()
            video.download(save_file)
            messagebox.showinfo("Info", "Download compleat")
        except:
            messagebox.showerror("Error", "An error occurred")
    else:
        messagebox.showerror("Error", "Enter a link")

root = Tk()
root.title("YouTube Downloader")
root.geometry("500x200")
root.resizable(False, False)

style = ttk.Style()
style.theme_use("vista")
style.configure("TFrame", background="white", foreground="white")

frame = ttk.Frame(root, style="TFrame")
frame.place(relx=0.5, rely=0.5, anchor=CENTER)

link_label = ttk.Label(frame, text="Enter YouTube link:")
link_label.grid(row=0, column=0, padx=10, pady=10)

link_entry = ttk.Entry(frame)
link_entry.grid(row=0, column=1, padx=10, pady=10)

resolution_var = StringVar(root)
resolution_var.set("All")
resolution_options = ["All", "360p", "480p", "720p", "1080p"]
resolution_dropdown = ttk.OptionMenu(frame, resolution_var, *resolution_options)
resolution_dropdown.grid(row=1, column=0, padx=10, pady=10)

download_button = ttk.Button(frame, text="Download", command=download)
download_button.grid(row=1, column=1, padx=10, pady=10)

root.mainloop()




