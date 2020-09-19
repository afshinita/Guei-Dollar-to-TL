import datetime as dt
import time
import urllib.request
import ssl
from bs4 import BeautifulSoup
from tkinter import ttk
import tkinter as tk


class Data:
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.ctx = ssl.create_default_context()
        self.ctx.check_hostname = False
        self.ctx.verify_mode = ssl.CERT_NONE
        self.odata = urllib.request.urlopen("https://dolar.tlkur.com/", context=self.ctx)
        self.my_data = BeautifulSoup(self.odata, 'html.parser')
        self.dat = self.my_data.find('div')('span')
        self.lis = list()
        for line in self.dat:
            xl = line.text
            self.lis.append(xl)
        self.dollar = self.lis[3]
        self.euro = self.lis[9]
        self.bitco = self.lis[35]
        self.dollar_pe = self.lis[4]
        self.euro_pe = self.lis[10]
        self.bitcoin_pe = self.lis[34]
        self.pound = self.lis[27]
        self.pound_pe = self.lis[28]
        self.altin = self.lis[15]
        self.altin_pe = self.lis[16]
        self.bitcoin = self.bitco[-9:]

        self.root = tk.Tk()
        self.root.config(bg="white")
        self.root.title("Python for ever")
        self.window = ttk.Panedwindow(self.root, orient='horizontal')
        self.window.pack(fill='both', expand=True)
        self.frame1 = ttk.Frame(self.window, width=100, height=300, relief='sunken')
        self.frame2 = ttk.Frame(self.window, width=200, height=400, relief='sunken')
        self.window.add(self.frame1, weight=1)
        self.window.add(self.frame2, weight=4)
        self.root.resizable(height=False, width=False)

        self.lable0 = ttk.Label(self.frame2, text="Dollar:    ", background="red", font=("Courier", 18, "italic"))
        self.lable0.grid(row=0, column=0)
        self.lable1 = ttk.Label(self.frame2, text=" ", background="red", font=("Courier", 18, "italic"))
        self.lable1.grid(row=0, column=1)

        self.lable2 = ttk.Label(self.frame2, text="Euro:      ", background="orange", font=("Courier", 18, "italic"))
        self.lable2.grid(row=1, column=0)
        self.lable3 = ttk.Label(self.frame2, text=" ", background="orange", font=("Courier", 18, "italic"))
        self.lable3.grid(row=1, column=1)

        self.lable4 = ttk.Label(self.frame2, text="Pound:     ", background="magenta", font=("Courier", 18, "italic"))
        self.lable4.grid(row=2, column=0)
        self.lable5 = ttk.Label(self.frame2, text=" ", background="magenta", font=("Courier", 18, "italic"))
        self.lable5.grid(row=2, column=1)

        # self.lable6 = ttk.Label(self.frame2, text="Bitcoin:   ", background="green", font=("Courier", 18, "italic"))
        # self.lable6.grid(row=3, column=0)
        # self.lable7 = ttk.Label(self.frame2, text=" ", background="green", font=("Courier", 18, "italic"))
        # self.lable7.grid(row=3, column=1)
        #
        # self.lable8 = ttk.Label(self.frame2, text="Altin/Ons: ", background="orange", font=("Courier", 18, "italic"))
        # self.lable8.grid(row=4, column=0)
        # self.lable9 = ttk.Label(self.frame2, text=" ", background="orange", font=("Courier", 18, "italic"))
        # self.lable9.grid(row=4, column=1)

        self.text = tk.Text(self.frame2, font=("Arial", 18), height=1, width=20)
        self.text.grid(row=0, column=2)
        self.text.insert('1.0', self.dollar)
        self.text.insert('1.10', '          ')
        self.text.insert('1.16', self.dollar_pe)
        self.text.configure(bg='yellow')

        self.text1 = tk.Text(self.frame2, font=("Arial", 18), height=1, width=20)
        self.text1.grid(row=1, column=2)
        self.text1.insert('1.0', self.euro)
        self.text1.insert('1.10', '          ')
        self.text1.insert('1.16', self.euro_pe)
        self.text1.configure(bg='yellow')

        self.text2 = tk.Text(self.frame2, font=("Arial", 18), height=1, width=20)
        self.text2.grid(row=2, column=2)
        self.text2.insert('1.0', self.pound)
        self.text2.insert('1.10', '          ')
        self.text2.insert('1.16', self.pound_pe)
        self.text2.configure(bg='yellow')

        # self.text3 = tk.Text(self.frame2, font=("Arial", 18), height=1, width=20)
        # self.text3.grid(row=3, column=2)
        # self.text3.insert('1.0', self.bitcoin)
        # self.text3.insert('1.10', '     ')
        # self.text3.insert('1.14', self.bitcoin_pe)
        # self.text3.configure(bg='yellow')

        # self.text4 = tk.Text(self.frame2, font=("Arial", 18), height=1, width=20)
        # self.text4.grid(row=4, column=2)
        # self.text4.insert('1.0', self.altin)
        # self.text4.insert('1.10', '        ')
        # self.text4.insert('1.15', self.altin_pe)
        # self.text4.configure(bg='yellow')

        self.progressbar = ttk.Progressbar(self.frame1, orient='horizontal', length = 180, mode='determinate')
        self.progressbar.grid(row=2, column=0)
        self.count = 0
        # self.text5 = tk.Text(self.frame1, font=("Arial", 24), height=1, width=3,foreground='red')
        # self.text5.grid(row=3, column=0)

    def read_data(self):
        self.odata = urllib.request.urlopen("https://dolar.tlkur.com/", context=self.ctx)
        self.my_data = BeautifulSoup(self.odata, 'html.parser')
        self.dat = self.my_data.find('div')('span')
        self.lis = list()
        for line in self.dat:
            xl = line.text
            self.lis.append(xl)
        self.dollar = self.lis[3]
        self.euro = self.lis[9]
        self.bitco = self.lis[35]
        self.dollar_pe = self.lis[4]
        self.euro_pe = self.lis[10]
        self.bitcoin_pe = self.lis[34]
        self.pound = self.lis[27]
        self.pound_pe = self.lis[28]
        self.altin = self.lis[15]
        self.altin_pe = self.lis[16]
        self.bitcoin = self.bitco[-9:]

        self.text.config(state='normal')
        self.text1.config(state='normal')
        self.text2.config(state='normal')
        # self.text3.config(state='normal')
        # self.text4.config(state='normal')

        self.text.replace('1.0', '1.6', self.dollar)
        self.text.replace('1.16', '1.22 lineend', self.dollar_pe)
        self.text1.replace('1.0', '1.6', self.euro)
        self.text1.replace('1.16', '1.22 lineend', self.euro_pe)
        self.text2.replace('1.0', '1.6', self.pound)
        self.text2.replace('1.16', '1.22 lineend', self.pound_pe)
        # self.text3.replace('1.0', '1.9', self.bitcoin)
        # self.text3.replace('1.14', '1.20 lineend', self.bitcoin_pe)
        # self.text4.replace('1.0', '1.7', self.altin)
        # self.text4.replace('1.15', '1.21 lineend', self.altin_pe)

        self.text.config(state='disabled')
        self.text1.config(state='disabled')
        self.text2.config(state='disabled')
        # self.text3.config(state='disabled')
        # self.text4.config(state='disabled')

        print("Dollar: ", self.dollar, "TL ", self.dollar_pe, "\nEuro: ", self.euro, "TL ", self.euro_pe, \
              "\nPound: ", self.pound, "TL ", self.pound_pe, "\nBitcoin: ", self.bitcoin, "TL ", self.bitcoin_pe, \
              "\nAltin Ons: ", self.altin, "TL ", self.altin_pe)
        print("================================================================")
        self.count_me()
        return self.dollar, self.dollar_pe, self.euro, self.euro_pe, self.pound, self.pound_pe, self.bitcoin, self.bitcoin_pe, self.altin, self.altin_pe

    def count_me(self):
        self.count += 1
        self.progressbar.config(value=self.count * 2)
        # self.text5.config(state='normal')
        # self.text5.replace('1.0','1.3', self.count)
        # self.text5.config(state='disabled')
        print(self.count, ' S%')
        if self.count >= 180:
            self.count = 0


def main():
    data = Data()
    data.read_data()

    lable = ttk.Label(data.frame1, text="Dollar/Euro/Pound\n     Cost%", background="lightgreen",
                      font=("Courier", 14, "italic"))
    lable.grid(row=0, column=0)
    button = ttk.Button(data.frame1, command=data.read_data, text="Update Currency", width=30)
    button.grid(row=1, column=0)

    data.root.mainloop()


if __name__ == '__main__': main()
