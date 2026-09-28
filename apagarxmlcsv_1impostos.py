import os
from dotenv import load_dotenv
load_dotenv()  # lê o .env local (não vai para o GitHub)

# --- CONFIGURAÇÕES ---
# SIMULACAO=true no .env só mostra o que seria apagado; false APAGA DE VERDADE
SIMULACAO = os.getenv("SIMULACAO", "true").strip().lower() == "true"

pasta_base = os.getenv("PASTA_IMPOSTOS")

# Lista exata dos arquivos que devem ser apagados
arquivos_alvo = [
    "nfse_pdf_prestado_1.pdf",
    "nfse_xml_prestado.xml",
    "nfse_csv_prestado_052026.csv",
    "nfse_csv_prestado.csv",
    "nfse_csv_tomado.csv",
    "nfse_xml_tomado.xml",
    "nfse_pdf_tomado_1.pdf",
    "nfse_pdf_tomado.pdf"
]

def limpar_arquivos():
    if not os.path.exists(pasta_base):
        print(f"Erro: A pasta base não foi encontrada:\n{pasta_base}")
        return

    arquivos_apagados = 0
    erros = 0

    print("--- INICIANDO VARREDURA DE LIMPEZA ---\n")
    if SIMULACAO:
        print("MODO SIMULAÇÃO ATIVADO: Nenhum arquivo será realmente apagado.\n")

    # os.walk percorre a pasta base e TODAS as subpastas dentro dela
    for raiz, subpastas, arquivos in os.walk(pasta_base):
        for nome_arquivo in arquivos:
            # Verifica se o nome do arquivo atual está na nossa lista de exclusão
            # (Usamos .lower() para garantir que não vai falhar caso tenha alguma letra maiúscula no nome)
            if nome_arquivo.lower() in [alvo.lower() for alvo in arquivos_alvo]:
                caminho_completo = os.path.join(raiz, nome_arquivo)
                
                if SIMULACAO:
                    print(f"[SIMULAÇÃO] Apagaria: {caminho_completo}")
                    arquivos_apagados += 1
                else:
                    try:
                        os.remove(caminho_completo)
                        print(f"[SUCESSO] Apagado: {caminho_completo}")
                        arquivos_apagados += 1
                    except Exception as e:
                        print(f"[ERRO] Falha ao apagar {caminho_completo}: {e}")
                        erros += 1

    print("\n--- RESUMO DA LIMPEZA ---")
    status = "Arquivos que SERIAM apagados" if SIMULACAO else "Arquivos APAGADOS com sucesso"
    print(f"{status}: {arquivos_apagados}")
    
    if erros > 0:
        print(f"Erros encontrados: {erros}")

if __name__ == "__main__":
    limpar_arquivos()