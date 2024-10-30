import speech_recognition as sr
import time
from pynput import keyboard as pynput_keyboard
from tkinter import Tk, Label
import threading

# Variáveis globais
current_command = ""
recognizer_active = True  # Controle de reconhecimento de voz

def recognize_speech():
    """Função que reconhece comandos de voz continuamente."""
    global current_command, recognizer_active
    recognizer = sr.Recognizer()
    
    with sr.Microphone() as source:
        while True:  # Loop infinito para escutar continuamente
            if recognizer_active:  # Apenas escuta se o reconhecimento estiver ativo
                try:
                    print("Diga um comando...")
                    audio = recognizer.listen(source)
                    command = recognizer.recognize_google(audio, language='pt-BR')
                    current_command = command.lower()  # Armazena o comando atual
                    print(f"Você disse: {current_command}")
                    execute_command(current_command)  # Executa o comando
                except sr.UnknownValueError:
                    current_command = "Não entendi o que você disse."
                except sr.RequestError:
                    current_command = "Erro ao se conectar ao serviço de reconhecimento de fala."

def execute_command(command):
    """Função para executar comandos específicos."""
    kb = pynput_keyboard.Controller()  # Controlador de teclado
    if 'andar' in command or 'w' in command:
        print("Pressionando W por 5 segundos...")
        kb.press('w')
        time.sleep(5)
        kb.release('w')

    elif 'trás' in command or 's' in command:
        print("Pressionando S por 5 segundos...")
        kb.press('s')
        time.sleep(5)
        kb.release('s')

    elif 'esquerda' in command or 'a' in command:
        print("Pressionando A por 5 segundos...")
        kb.press('a')
        time.sleep(5)
        kb.release('a')

    elif 'direita' in command or 'd' in command:
        print("Pressionando D por 5 segundos...")
        kb.press('d')
        time.sleep(5)
        kb.release('d')

    elif 'girar pra cima' in command or 'm' in command:
        print("Pressionando M por 0,2 segundos...")
        kb.press('m')
        time.sleep(0.2)
        kb.release('m')

    elif 'girar pra baixo' in command or 'n' in command:
        print("Pressionando N por 0,2 segundos...")
        kb.press('n')
        time.sleep(0.2)
        kb.release('n')

    elif 'girar pra direita' in command or 'v' in command:
        print("Pressionando V por 0,2 segundos...")
        kb.press('v')
        time.sleep(0.2)
        kb.release('v')

    elif 'girar pra esquerda' in command or 'b' in command:
        print("Pressionando B por 0,2 segundos...")
        kb.press('b')
        time.sleep(0.2)
        kb.release('b')

    elif 'mirar' in command or 'l' in command:
        print("Pressionando L...")
        kb.press('l')
        time.sleep(0.1)
        kb.release('l')

    elif 'trocar arma' in command or 'p' in command:
        print("Pressionando P...")
        kb.press('p')
        time.sleep(0.1)
        kb.release('p')

    elif 'trocar escudo' in command or 'o' in command:
        print("Pressionando O...")
        kb.press('o')
        time.sleep(0.1)
        kb.release('o')

    elif 'trocar item' in command or 'f' in command:
        print("Pressionando F...")
        kb.press('f')
        time.sleep(0.1)
        kb.release('f')

    elif 'trocar magia' in command or 'r' in command:
        print("Pressionando R...")
        kb.press('r')
        time.sleep(0.1)
        kb.release('r')

    elif 'ataque' in command or 'x' in command:
        print("Pressionando X...")
        kb.press('x')
        time.sleep(0.1)
        kb.release('x')

    elif 'ataque forte' in command or 'z' in command:
        print("Pressionando Z...")
        kb.press('z')
        time.sleep(0.1)
        kb.release('z')

    elif 'defender' in command or 'c' in command:
        print("Pressionando C...")
        kb.press('c')
        time.sleep(0.1)
        kb.release('c')

    elif 'aparrar' in command or 'g' in command:
        print("Pressionando G...")
        kb.press('g')
        time.sleep(0.1)
        kb.release('g')

    elif 'usar' in command or 'jogar' in command or 'curar' in command or 'h' in command:
        print("Pressionando H...")
        kb.press('h')
        time.sleep(0.1)
        kb.release('h')

    elif 'desviar' in command or 'j' in command:
        print("Pressionando J...")
        kb.press('j')
        time.sleep(0.1)
        kb.release('j')

    elif 'duas mãos' in command or 'uma mão' in command or 't' in command:
        print("Pressionando T...")
        kb.press('t')
        time.sleep(0.1)
        kb.release('t')

    elif 'confirmar' in command or 'e' in command:
        print("Pressionando E...")
        kb.press('e')
        time.sleep(0.1)
        kb.release('e')

    elif 'cancelar' in command or 'q' in command:
        print("Pressionando Q...")
        kb.press('q')
        time.sleep(0.1)
        kb.release('q')

def update_command_display(command_label):
    """Atualiza a label na GUI com o comando atual."""
    def refresh():
        command_label.config(text=current_command)  # Atualiza o texto da label
        command_label.after(500, refresh)  # Chama a função novamente após 500ms
    refresh()

def on_press(key):
    """Função que escuta eventos de tecla pressionada."""
    global recognizer_active
    if key == pynput_keyboard.Key.space:
        recognizer_active = not recognizer_active  # Alterna o estado de reconhecimento
        print("Programa pausado." if not recognizer_active else "Programa retomado.")

def start_listener():
    """Inicia o listener do teclado."""
    listener = pynput_keyboard.Listener(on_press=on_press)
    listener.start()  # Inicia o listener em uma thread separada

def run_gui():
    """Cria e executa a GUI usando Tkinter."""
    root = Tk()
    root.title("Comandos de Voz")
    root.geometry("400x200")
    root.attributes("-topmost", True)  # Mantém a janela acima das outras
    root.attributes("-alpha", 0.8)  # Configura transparência da janela

    command_label = Label(root, text="Aguardando comando...", font=("Arial", 16), fg="black")
    command_label.pack(expand=True)  # Expande a label na janela

    update_command_display(command_label)  # Inicia a atualização da label
    root.mainloop()  # Mantém a janela aberta

if __name__ == "__main__":
    print("Certifique-se de que o jogo está em modo janela.")

    gui_thread = threading.Thread(target=run_gui)  # Cria uma thread para a GUI
    gui_thread.daemon = True  # Permite que a thread seja encerrada quando o programa principal terminar
    gui_thread.start()  # Inicia a thread da GUI

    start_listener()  # Inicia o listener de teclado
    recognize_speech()  # Inicia o reconhecimento de fala

