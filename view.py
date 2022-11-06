import tkinter as tk
import read_ip
import model


def start():
    buttons = {}
    def click(ip_address):
        ping_result = model.ping_ip(ip_address)
        if ping_result!='Disconnect':
            buttons[ip_address]['foreground'] = 'red'
            # buttons[ip_address]['font'] = 'bold'
            buttons[ip_address]['text'] = ping_result
        else:
            buttons[ip_address]['foreground'] = 'black'
            buttons[ip_address]['text'] = ping_result
        # print(ping_result)

    def click_all(ip_addresses):
        for ip_address in ip_addresses:
            ping_result = model.ping_ip(ip_address)
            if ping_result != 'Disconnect':
                buttons[ip_address]['foreground'] = 'red'
                # buttons[ip_address]['font'] = 'bold'
                buttons[ip_address]['text'] = ping_result
            else:
                buttons[ip_address]['foreground'] = 'black'
                buttons[ip_address]['text'] = ping_result


    # задание поля кнопок
    def make_buttons():
        ip_addresses = read_ip.read_ip()
        # print(ip_addresses)
        row = 0
        col = 0
        for ip_address in ip_addresses:
            # print(ip_address)
            button = tk.Button(text=ip_address, command=lambda ip_address=ip_address: click(ip_address))

            # button = tk.Button(text=ip_address, width=6, height=1,
            #                    font=('Arial', 20, 'bold'), background='light gray',
            #                    command=lambda ip_address=ip_address: click(ip_address))
            button.grid(row=row, column=col, padx=1, pady=1, sticky='nsew')
            buttons[ip_address] = button
            if row == 20:
                row = 0
                col += 1
            else:
                row += 1
        button = tk.Button(text='Бахнуть все IP', command=lambda ip_address=ip_addresses: click_all(ip_addresses))
        button.grid(row=row+1, column=col, padx=1, pady=1, sticky='nsew')
        button = tk.Button(text='Показать все IP', command=make_buttons)
        button.grid(row=row+2, column=col, padx=1, pady=1, sticky='nsew')



    ping_ip = tk.Tk()
    ping_ip.title("Ping IP")
    # ping_ip.geometry('350x500')

    make_buttons()

    ping_ip.mainloop()


start()
