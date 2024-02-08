# 📽 -> 🐍 -> 🎞 -> 🖼 -> 📝 -> 🤖 

# Processador de Vídeos para Geração de Datasets

Este é um script Python desenvolvido para processar vídeos e extrair frames para geração de datasets. O script utiliza a biblioteca OpenCV para manipulação de vídeos e frames.

## Funcionalidades

- **Limpeza do Diretório de Saída**: Antes de processar os vídeos, o script verifica se o diretório de saída está limpo. Se não estiver, ele remove todos os arquivos contidos no diretório para evitar conflitos.

- **Extração de Frames**: O script percorre todos os vídeos encontrados em um diretório especificado e extrai frames de cada vídeo. Os frames são salvos como imagens JPEG no diretório de saída.

## Pré-requisitos

- Python 3.x
- OpenCV (instalação via `pip install opencv-python`)

## Como Usar

1. Coloque seus vídeos na pasta `videos-to-generate-dataset`.
   
2. Execute o script `main.py`.

## Como Contribuir

Sinta-se à vontade para contribuir com melhorias, correções de bugs ou novas funcionalidades. Basta abrir uma issue ou enviar um pull request.

