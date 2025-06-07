# Spotify-grafico
Este projeto tem como objetivo visualizar o ranking das músicas de uma playlist do Spotify utilizando Python. A proposta é automatizar a obtenção dos dados diretamente da API do Spotify, processar as informações das faixas e apresentar os resultados em um gráfico de barras, facilitando a análise visual do ranking das músicas mais tocadas em uma playlist específica.
Funcionalidades e etapas do projeto:

Autenticação na API do Spotify:
Utiliza credenciais de desenvolvedor para acessar os dados das playlists de forma segura.

Busca automática das músicas:
O código acessa uma playlist definida pelo usuário (pessoal ou pública, desde que acessível via API) e recupera os nomes das 5 primeiras músicas.

Processamento dos dados:
Os nomes das músicas são organizados em uma lista e recebem um ranking conforme a ordem em que aparecem na playlist.

Visualização gráfica:
Utiliza a biblioteca Matplotlib para criar um gráfico de barras, onde cada barra representa uma música e sua posição no ranking.

Facilidade de adaptação:
Basta trocar o ID da playlist para analisar diferentes listas do Spotify, desde que sejam acessíveis pela API.

Tecnologias utilizadas
Python
Spotipy (cliente Python para a API do Spotify)
Matplotlib (visualização de dados)
NumPy (manipulação de arrays)
