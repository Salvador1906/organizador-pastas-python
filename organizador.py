import os
import shutil
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# Definimos o caminho para a pasta que queremos vigiar. Podes alterar para a tua pasta de downloads ou outra qualquer.
CAMINHO_PASTA = CAMINHO_PASTA = os.path.dirname(os.path.abspath(__file__))

REGRAS_PASTAS = {
    '.pdf': 'Documentos_PDF',
    '.docx': 'Documentos_Word',
    '.csv': 'Dados_CSV',
    '.jpg': 'Imagens',
    '.png': 'Imagens'
}

def mover_e_organizar(caminho_completo, item):
    # Ignora ficheiros ocultos do Mac (.DS_Store, etc)
    if item.startswith('.'):
        return

    nome, extensao = os.path.splitext(item)
    extensao = extensao.lower()
    
    if extensao in REGRAS_PASTAS:
        nome_pasta_destino = REGRAS_PASTAS[extensao]
        caminho_pasta_destino = os.path.join(CAMINHO_PASTA, nome_pasta_destino)
        
        if not os.path.exists(caminho_pasta_destino):
            os.makedirs(caminho_pasta_destino)
            print(f"Pasta criada: {nome_pasta_destino}")
            
        caminho_final_ficheiro = os.path.join(caminho_pasta_destino, item)
        
        contador = 1
        novo_nome = item
        while os.path.exists(caminho_final_ficheiro):
            novo_nome = f"{nome}_{contador}{extensao}"
            caminho_final_ficheiro = os.path.join(caminho_pasta_destino, novo_nome)
            contador += 1
            
        if novo_nome != item:
            print(f"Conflito resolvido: {item} renomeado para -> {novo_nome}")
            
        shutil.move(caminho_completo, caminho_final_ficheiro)
        print(f"Movido com sucesso: {novo_nome} -> {nome_pasta_destino}\n")

# A classe que vai "reagir" aos eventos da pasta
class ManipuladorPasta(FileSystemEventHandler):
    # O evento 'on_created' dispara automaticamente sempre que um ficheiro surge na pasta
    def on_created(self, event):
        # Garantir que não estamos a tentar mover uma pasta inteira, apenas ficheiros
        if not event.is_directory:
            # event.src_path dá-nos o caminho completo do ficheiro detetado
            item = os.path.basename(event.src_path)
            # Damos um mini delay de 100ms para garantir que o Mac acabou de escrever o ficheiro no disco
            time.sleep(0.1) 
            mover_e_organizar(event.src_path, item)
    
    def on_modified(self, event):
        if not event.is_directory:
            item = os.path.basename(event.src_path)
            # Verificar se o ficheiro ainda existe na raiz antes de tentar mover
            # (evita que o programa tente mover um ficheiro que já foi movido no on_created)
            if os.path.exists(event.src_path):
                time.sleep(0.2)
                mover_e_organizar(event.src_path, item)

# Configuração do Cão de Guarda (Watchdog)
if __name__ == "__main__":
    handler = ManipuladorPasta()
    observer = Observer()
    observer.schedule(handler, path=CAMINHO_PASTA, recursive=False)
    
    observer.start()
    print(f"O teu Cão de Guarda está ativo e a vigiar a pasta:\n{CAMINHO_PASTA}\n(Pressiona Ctrl+C no terminal para parar)\n")
    
    try:
        while True:
            time.sleep(1) # Mantém o programa vivo sem gastar processador
    except KeyboardInterrupt:
        observer.stop()
        print("\nPrograma terminado com sucesso.")
    observer.join()