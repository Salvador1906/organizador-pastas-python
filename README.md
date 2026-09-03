

https://github.com/user-attachments/assets/245a7655-f27f-4508-86a2-bfb5d38a79de

# Organizador de Pastas Inteligente em Tempo Real 🚀

Este é um script em Python desenvolvido para automatizar a organização de ficheiros em qualquer diretório. O programa funciona em segundo plano (como um "Cão de Guarda") e move os ficheiros automaticamente para pastas específicas com base na sua extensão (PDFs, Imagens, Documentos, etc.) assim que eles são criados ou modificados.

## ✨ Funcionalidades
- **Monitorização em Tempo Real:** Utiliza a biblioteca `watchdog` ligada ao sistema operativo para deteção instantânea.
- **Compatibilidade com Nuvem:** Otimizado com lógica de dupla fase (`on_created` e `on_modified`) para funcionar perfeitamente em pastas sincronizadas como o iCloud Drive.
- **Prevenção de Conflitos:** Ciclo inteligente que renomeia ficheiros duplicados automaticamente (ex: `foto(1).png`) para evitar perdas de dados.
- **Multiplataforma:** Utiliza o módulo `os` para garantir portabilidade entre macOS e Windows.

## 📦 Como Instalar
1. Transfere o ficheiro `organizador.py` para a pasta que pretendes manter organizada.
2. Instala as dependências necessárias através do terminal:
   ```bash
   pip install -r requirements.txt
