import os
import webbrowser
from html_generator_mobs_bodys import generate_html_report

# Configurações
SCREENSHOT_DIR = "public/UO_BodyValues"
OUTPUT_HTML = "public/index.html"

os.makedirs(SCREENSHOT_DIR, exist_ok=True)

print("=== UO BodyValue HTML Generator ===")
print(f"Gerando relatório a partir das imagens em: {os.path.abspath(SCREENSHOT_DIR)}")

try:
    # Gera o relatório
    html_report = generate_html_report(SCREENSHOT_DIR)
    if html_report != OUTPUT_HTML:
        os.replace(html_report, OUTPUT_HTML)
        
    print(f"\nRelatório gerado com sucesso: {os.path.abspath(html_report)}")
    
    # Abre no navegador
    webbrowser.open(f'file://{os.path.abspath(html_report)}')

except Exception as e:
    print(f"\nErro durante execução: {str(e)}")

finally:
    print("Operação finalizada.")
