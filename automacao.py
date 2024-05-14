from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import keyboard

# Mapeamento de atalhos para frases
atalhos_para_frases = {
    "ctrl+1": "Esta é a frase para Ctrl+1.",
    "ctrl+2": "Esta é a frase para Ctrl+2.",
    "ctrl+3": "Esta é a frase para Ctrl+3.",
    "ctrl+4": "Esta é a frase para Ctrl+4.",
    "ctrl+5": "Esta é a frase para Ctrl+5.",
    # Adicione mais atalhos e frases conforme necessário
}

def enviar_frase(frase):
    # Encontra o campo de texto ativo no navegador e digita a frase
    campo_ativo = driver.switch_to.active_element
    campo_ativo.send_keys(frase)

# Inicializa o driver do navegador / Ele vai abrir uma nova janela do navegador
driver = webdriver.Chrome()

# Adiciona os atalhos
for atalho in atalhos_para_frases:
    keyboard.add_hotkey(atalho, enviar_frase, args=(atalhos_para_frases[atalho],))

# Mantém o script em execução
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("Programa encerrado.")
    driver.quit()
