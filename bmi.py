import PySimpleGUI as sg 

def InterfaceMain():
    sg.theme('Dark')
    Mainlayout = [  [sg.Text('\t\tBMI Calculator'), sg.Text('\n\n')],
                    [sg.Text('  '), sg.Text('Input Weight:'), sg.Input(size=25), sg.Text('\n\n')],
                    [sg.Text('  '), sg.Text('Input Height:'), sg.Input(size=25), sg.Text('\n\n\n\n')],
                    [sg.Submit(size=25), sg.Cancel(size=25)]
                    ]
    while True:
        MainWindow = sg.Window("BMI Calculator",Mainlayout,size = (400,400))
        event, values = MainWindow.read()
        MainWindow.close()
        InterfaceResult(values)

def InterfaceResult(values):
    sg.theme('Dark')
    bmi = int(values[0])/((int(values[1])/100)*(int(values[1])/100))
    
    if bmi<18.5:
        layout = [
        [sg.Text('\n\t\t Your Body Mass Index is')],
        [sg.Text("\t\t\t {:.2f}".format(bmi))],
        [sg.Text("\n\t\t    You are classified as\n\n\t\t           UNDERWEIGHT")],
        [sg.Text("\n\n\t\t      Calculate More ?")],
        [sg.Text("\t           "),sg.Button("Yes",size=(8,2)),sg.Exit(size=(8,2))]
    ]
    elif 18.5<=bmi<25:
        layout = [
        [sg.Text('\n\t\t Your Body Mass Index is')],
        [sg.Text("\t\t\t {:.2f}".format(bmi))],
        [sg.Text("\n\t\t    You are classified as\n\n\t\t           HEALTHY")],
        [sg.Text("\n\n\t\t      Calculate More ?")],
        [sg.Text("\t           "),sg.Button("Yes",size=(8,2)),sg.Exit(size=(8,2))]
    ]

    elif 25<=bmi<40:
        layout = [
        [sg.Text('\n\t\t Your Body Mass Index is')],
        [sg.Text("\t\t\t {:.2f}".format(bmi))],
        [sg.Text("\n\t\t    You are classified as\n\n\t\t           OVERWEIGHT")],
        [sg.Text("\n\n\t\t      Calculate More ?")],
        [sg.Text("\t           "),sg.Button("Yes",size=(8,2)),sg.Exit(size=(8,2))]
        ]

    elif bmi>=40:
        layout = [
        [sg.Text('\n\t\t Your Body Mass Index is')],
        [sg.Text("\t\t\t {:.2f}".format(bmi))],
        [sg.Text("\n\t\t    You are classified as\n\n\t\t           OBESSE")],
        [sg.Text("\n\n\t\t      Calculate More ?")],
        [sg.Text("\t           "),sg.Submit("Yes",size=(8,2)),sg.Cancel('Exit', size=(8,2))]
    ]  
    while True:
        Resultwindow = sg.Window("BMI Calculator",layout,size=(400,400))
        event1, values1 = Resultwindow.read()
        values.clear()
        Resultwindow.close()
        if event1 == sg.WIN_CLOSED or event1 == 'Exit':
            break
        InterfaceMain()
        

InterfaceMain()