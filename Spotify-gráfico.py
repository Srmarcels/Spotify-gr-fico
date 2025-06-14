# Este código cria um gráfico de barras que exibe as 5 músicas mais tocadas de uma playlist específica do Spotify.
# Ele utiliza a biblioteca Spotipy para acessar a API do Spotify e matplotlib para criar o gráfico.
# Importa as bibliotecas necessárias para gráficos e manipulação de arrays
import matplotlib.pyplot as plt
import numpy as np
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth
import plotly.express as px
import pandas as pd
from collections import Counter

# Credenciais do Spotify
client_id = "a21cb06323be464b960f64609cb860aa"
client_secret = "20c05001b3aa4c0da1cff6324118af9b"
redirect_uri = "http://127.0.0.1:8888/callback"

# Gráfico 1: Barras - Top 5 músicas da playlist
def grafico_barras():
    sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=client_id, client_secret=client_secret))
    playlist_id = "22R0Iz9WLovMhLN2eLyELP"
    try:
        results = sp.playlist_tracks(playlist_id, limit=5)
        musicas = []
        if results and "items" in results:
            for item in results["items"]:
                musicas.append(item["track"]["name"])
            print("Autenticação bem-sucedida!")
        else:
            print("Nenhuma música encontrada na playlist.")
            return

        indice = np.arange(len(musicas))
        acessos = list(range(len(musicas), 0, -1))
        plt.bar(indice, acessos)
        plt.xticks(indice, musicas, rotation=30)
        plt.ylabel("Ranking (5 = mais tocada)")
        plt.title("Top 5 músicas da playlist")
        plt.show()
    except Exception as e:
        print("Erro ao acessar a playlist:", e)
        return

# Gráfico 2: Árvore hierárquica das músicas salvas
def grafico_arvore():
    sp_user = spotipy.Spotify(auth_manager=SpotifyOAuth(
        client_id=client_id,
        client_secret=client_secret,
        redirect_uri=redirect_uri,
        scope="user-library-read"))
    results = sp_user.current_user_saved_tracks(limit=50)
    dados = []
    if results and "items" in results and results["items"]:
        for item in results["items"]:
            track = item["track"]
            dados.append({
                'Artista': track['artists'][0]['name'],
                'Album': track['album']['name'],
                'Música': track['name'],
            })
    else:
        print("Nenhuma música salva encontrada para o usuário.")
        return

    df = pd.DataFrame(dados)
    fig = px.treemap(df, path=['Artista', 'Album', 'Música'], title='Árvore Hierárquica de Músicas Salvas')
    fig.show()

# Gráfico 3: Pizza dos gêneros das músicas salvas
def grafico_pizza():
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
        client_id=client_id,
        client_secret=client_secret,
        redirect_uri=redirect_uri,
        scope="user-library-read"))
    results = sp.current_user_saved_tracks(limit=50)
    dados = []
    if results and "items" in results and results["items"]:
        for item in results["items"]:
            track = item["track"]
            dados.append({
                'Artista': track['artists'][0]['name'],
                'Album': track['album']['name'],
                'Música': track['name'],
            })
    else:
        print("Nenhuma música salva encontrada para o usuário.")
        return

    df = pd.DataFrame(dados)
    generos = []
    for index, row in df.iterrows():
        artista_nome = row['Artista']
        resultado = sp.search(q='artist:' + artista_nome, type='artist', limit=1)
        if resultado and 'artists' in resultado and 'items' in resultado['artists'] and resultado['artists']['items']:
            artista = resultado['artists']['items'][0]
            if 'genres' in artista and artista['genres']:
                generos.extend(artista['genres'])

    contagem_generos = Counter(generos)
    if not contagem_generos:
        print("Nenhum gênero encontrado nas músicas salvas.")
        return

    mais_comuns = contagem_generos.most_common(8)
    labels, valores = zip(*mais_comuns)

    plt.figure(figsize=(10, 6))
    plt.pie(valores, labels=labels, autopct='%1.1f%%')
    plt.title('Distribuição de Gêneros das Músicas Salvas')
    print("Gêneros encontrados:", generos)
    print("Contagem:", contagem_generos)
    plt.show()

# --- CHAME APENAS O GRÁFICO QUE DESEJA VISUALIZAR ---
print("Bem-vindo ao visualizador de gráficos do Spotify!")
print("Escolha o gráfico:")
print("1 - Barras (Top 5 músicas da playlist)")
print("2 - Árvore hierárquica (músicas salvas)")
print("3 - Pizza (gêneros das músicas salvas)")
opcao = input("Digite o número do gráfico desejado: ")

if opcao == "1":
    grafico_barras()
elif opcao == "2":
    grafico_arvore()
elif opcao == "3":
    grafico_pizza()
else:
    print("Opção inválida.")