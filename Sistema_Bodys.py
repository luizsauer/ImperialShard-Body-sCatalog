import os
import webbrowser
from html_generator_mobs_bodys import generate_html_report

# Configurações
SCREENSHOT_DIR = "UO_BodyValues"  # Pasta onde estão as imagens

print("=== UO BodyValue HTML Generator ===")
print(f"Gerando relatório a partir das imagens em: {os.path.abspath(SCREENSHOT_DIR)}")

try:
    # Gera o relatório
    html_report = generate_html_report(SCREENSHOT_DIR)
    print(f"\nRelatório gerado com sucesso: {os.path.abspath(html_report)}")
    
    # Abre no navegador
    webbrowser.open(f'file://{os.path.abspath(html_report)}')

except Exception as e:
    print(f"\nErro durante execução: {str(e)}")

finally:
    print("Operação finalizada.")
