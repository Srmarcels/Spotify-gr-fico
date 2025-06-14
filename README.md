# Spotify-grafico
Este projeto Python conecta-se à API do Spotify para analisar e visualizar o perfil musical do usuário. Ele apresenta três gráficos interativos:

Um gráfico de barras com as músicas mais tocadas de uma playlist,
Um gráfico de árvore hierárquica mostrando a organização das músicas salvas por artista e álbum,
E um gráfico de pizza que revela a diversidade de gêneros musicais presentes na biblioteca do usuário.
A solução oferece uma visão clara e visual dos hábitos musicais, facilitando o entendimento do gosto musical e das tendências do usuário no Spotify.

O código utiliza as bibliotecas Spotipy, Matplotlib, Plotly e Pandas para acessar dados do Spotify e gerar três tipos de gráficos:

Gráfico de barras: Mostra as 5 músicas mais tocadas de uma playlist específica, usando autenticação por client credentials.
Gráfico de árvore hierárquica (treemap): Exibe a relação entre artista, álbum e música das 50 primeiras músicas salvas do usuário, usando autenticação OAuth.
Gráfico de pizza: Mostra a distribuição dos gêneros musicais das músicas salvas, buscando os gêneros dos artistas e exibindo as proporções em um gráfico de pizza.
Cada gráfico está implementado em uma função separada, com tratamento de exceções e verificação de dados. O código pode ser executado para mostrar qualquer um dos gráficos, conforme a necessidade.
