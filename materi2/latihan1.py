import PySimpleGUI as sg
sg.theme("DarkBrown6")
sg.theme_text_color("#f0FFFF")
window = sg.Window(title="Profile",
                    layout=[[sg.Text("SELAMAT DATANG DI KELAS",
                                    font=("Arial",25,"italic","bold","underline"))],
                            [sg.Text("NPM : 2210010477 ")],
                            [sg.Text("Nama : TIARA DESMITHA OLIVIANY ")],
                            [sg.Text("Kelas : 5E Regular Banjarmasin ")]
                            ],
                    size=(510,200),
                    font=("Times", 18))
window()
window.close()