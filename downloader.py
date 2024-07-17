import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# URL do site com as imagens de gatos
url = 'https://www.pexels.com/pt-br/procurar/cat/'

# Faz a requisição HTTP para obter o conteúdo da página
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Encontra todas as tags <img> na página
img_tags = soup.find_all('img')

# Cria uma pasta para salvar as imagens
if not os.path.exists('imagens_gatos'):
    os.makedirs('imagens_gatos')

# Contador para limitar o número de imagens
contador = 0

# Itera sobre as URLs das imagens e faz o download
for img in img_tags:
    img_url = img.get('src')
    if img_url and 'cat' in img_url:  # Filtra apenas as imagens de gatos
        img_url = urljoin(url, img_url)  # Transforma a URL relativa em absoluta
        img_name = f"imagem{contador + 1}.jpg"
        img_path = os.path.join('imagens_gatos', img_name)
        try:
            img_data = requests.get(img_url).content
            with open(img_path, 'wb') as f:
                f.write(img_data)
            print(f"Imagem '{img_name}' salva com sucesso!")
            contador += 1
            if contador >= 10:
                break  # Para quando tiver 10 imagens
        except Exception as e:
            print(f"Erro ao baixar a imagem '{img_name}': {e}")

print("Download concluído!")
