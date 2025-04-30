import os
import time
import webbrowser
from PIL import ImageGrab
from html_generator_mobs_bodys import generate_html_report  # <-- agora vem daqui

# Configurações
START_VALUE = 0
END_VALUE = 1700
DELAY = 6  # segundos para mudar manualmente o body
SCREENSHOT_DIR = "UO_BodyValues"
CAPTURE_REGION = (912, 125, 1317, 511)  # Área de captura da tela

# Cria diretório se não existir
if not os.path.exists(SCREENSHOT_DIR):
    os.makedirs(SCREENSHOT_DIR)

print("=== UO BodyValue Screenshotter ===")
print(f"Capturando de BodyValue {START_VALUE} a {END_VALUE}")
print(f"Screenshots serão salvos em: {os.path.abspath(SCREENSHOT_DIR)}")
print("Você deverá mudar o bodyvalue manualmente no jogo entre cada captura.")
input("Pressione Enter para começar...")

try:
    for body_value in range(START_VALUE, END_VALUE + 1):
        print(f"\n[+] Prepare para BodyValue: {body_value}")
        time.sleep(DELAY)  # Dá tempo para mudar no jogo
        
        # Tira screenshot da região especificada
        filename = f"{body_value:04d}.png"
        filepath = os.path.join(SCREENSHOT_DIR, filename)
        
        screenshot = ImageGrab.grab(bbox=CAPTURE_REGION)
        screenshot.save(filepath)
        print(f"[OK] Screenshot salvo: {filename}")
        
        # Atualiza o relatório HTML após cada captura
        html_report = generate_html_report(SCREENSHOT_DIR)

    print("\nProcesso concluído com sucesso!")
    print(f"Relatório gerado: {os.path.abspath(html_report)}")
    
    webbrowser.open(f'file://{os.path.abspath(html_report)}')

except KeyboardInterrupt:
    print("\nProcesso interrompido pelo usuário.")
    html_report = generate_html_report(SCREENSHOT_DIR)
    webbrowser.open(f'file://{os.path.abspath(html_report)}')

except Exception as e:
    print(f"\nErro durante execução: {str(e)}")

finally:
    print("Operação finalizada.")
