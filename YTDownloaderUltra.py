from tkinter import *
from tkinter.filedialog import *
import requests, time
from pytube import YouTube
from bs4 import BeautifulSoup
headersget = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:76.0) Gecko/20100101 Firefox/76.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate',
        'DNT': '1',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1'
    }
box = Tk()
box.title('Youtube Downloader Ultra V1.0')
box.iconbitmap(r'C:\Windows\System32\wscript.exe')
url1 = Entry(box, width=38, borderwidth=7)
randomlabel = Label(box, text='').grid(row=7,column=0)
randomlabel = Label(box, text='').grid(row=7,column=6)
url1.grid(row=7, column=1, columnspan=5)
def specify():
    global folder_path
    folder_path = askdirectory()
def getvid():
    url = url1.get()
    if url == '':
        randomlabel1 = Label(box, text='          ERROR: The Link/URL cannot be empty!          ')
        randomlabel1.grid(row=10,column=3)
    else:
        try: YouTube(url).streams.first().download(folder_path)
        except:
            randomlabel1 = Label(box, text='ERROR: Cannot get video! Perhaps the URL is wrong!')
            randomlabel1.grid(row=10,column=3)
    return
randomlabel = Label(box, text='YouTube High Quality Downloader by Arcana').grid(row=3,column=3)
specpath = Button(box, text='Save As',padx=44, pady=10, command = specify).grid(row=4, column=3)
randomlabel = Label(box, text='').grid(row=5,column=3)
randomlabel = Label(box, text='Paste Link/URL: ').grid(row=6,column=3)
randomlabel = Label(box, text='').grid(row=8,column=3)
randomlabel = Label(box, text='').grid(row=9,column=3)
randomlabel1 = Label(box, text='')
randomlabel1.grid(row=10,column=3)
getvideo = Button(box, text='Get Video!', padx=37, pady=10, command = getvid).grid(row=11, column=3)
randomlabel = Label(box, text='').grid(row=12,column=3)
box.mainloop()
