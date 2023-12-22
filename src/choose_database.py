import PySimpleGUI as sg
import sqlite3

sg.theme('Dark Blue 3')

layout = [[ sg.Text(size=(48,3), key='-OUTPUT-')],
          [ sg.Text('Select database file:'), sg.In(key='-INPUT-')],
          [sg.FileBrowse(target='-INPUT-'),sg.Button('Show'),sg.Button('Exit')],
          [sg.Button('Initialize Database')]]

window = sg.Window('Select Database', layout)

while True:
    event, values = window.read()
    print(event,values)
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    if event == 'Show':
        con = sqlite3.connect(values['-INPUT-'])
        cur = con.cursor()
        food_list = [ row for row in cur.execute("SELECT * FROM food LIMIT 10")]
        con.close()
        window['-OUTPUT-'].update(str(food_list))
    if event == 'Initialize Database':
        con = sqlite3.connect("foodlog.db")
        cur = con.cursor()
        cur.execute("CREATE TABLE food(name, serving, units, calories)")
        cur.execute("INSERT INTO food VALUES ('rice', 1, 'cups', 200)")
        con.commit()
        con.close()
window.close()
