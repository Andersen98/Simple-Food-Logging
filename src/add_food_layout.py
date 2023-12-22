import PySimpleGUI as sg
sg.theme('Dark Blue 3')
layout = [[sg.Text(size=(12,1),key='-OUTPUT-')],
          [sg.Text('Food Name:'), sg.Input(key='-NAME-')],
          [sg.Text('Amount Per Serving:'), sg.Input(key='-SERVING-'), sg.Text('units'),sg.Input(key='-UNITS-')],
          [sg.Text('Calories Per Serving'), sg.Input(key='-CALORIES-')],
          [sg.Button('Show'), sg.Button('Exit')]]

window = sg.Window('Window Title', layout)

while True:  # Event Loop
    event, values = window.read()
    print(event, values)
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    if event == 'Show':
        # change the "output" element to be the value of "input" element
        window['-OUTPUT-'].update(values['-NAME-'] + values['-SERVING-'] + values['-UNITS-'] + values['-CALORIES-'])

window.close()

