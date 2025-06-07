# Este código cria um gráfico de barras que exibe as 5 músicas mais tocadas de uma playlist específica do Spotify.
# Ele utiliza a biblioteca Spotipy para acessar a API do Spotify e matplotlib para criar o gráfico.
# Importa as bibliotecas necessárias para gráficos e manipulação de arrays
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np 
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# Configura as credenciais do Spotify

client_id = "a21cb06323be464b960f64609cb860aa"
client_secret = "a0635a8cbf484d0ea3d11e819ddd3ca7"

# Autentica no Spotify usando as credenciais
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=client_id, client_secret=client_secret))

# ID da playlist "ARENA 19/10 - Playlist Pessoal"

playlist_id = "22R0Iz9WLovMhLN2eLyELP"

# Busca as faixas da playlist (limitando para 5)
try:
    # Obtém as faixas da playlist
    results = sp.playlist_tracks(playlist_id, limit=5)
    musicas = []
    if results and "items" in results:
        for item in results["items"]:
            musicas.append(item["track"]["name"])
        print("Autenticação bem-sucedida!")
    else:
        print("Nenhuma música encontrada na playlist.")
        exit()
except Exception as e:
    print("Erro ao acessar a playlist:", e)
    exit()
# Fim da configuração das credenciais e obtenção das músicas

indice = np.arange(len(musicas))
acessos = list(range(len(musicas),0, -1))
plt.bar(indice, acessos)
plt.xticks(indice, musicas, rotation=30)
plt.ylabel("Ranking (5 = mais tocada)")
plt.title("Top 5 músicas da playlist")
plt.show()
# Fim do código