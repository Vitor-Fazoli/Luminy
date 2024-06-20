<h1 align="center">Lumixy</h1>

<p>Este é um TCC focado em desenvolvimento que tem como ideal trazer o ambiente de iluminação para objetos e paisagens bidimensionais
Trabalhos Similares (Relight): https://clipdrop.co/relight</p>

 <p> O trabalho será feito em python e irá recuperar uma imagem em formato png e uma posição de luz dentro da imagem para realizar uma segmentação, detecção de profundidade de cada uma dos grupos segmentados, para por fim executar uma série de calculos sobre cada pixel, para iluminar a imagem de maneira consisa e coesa</p>

<p>30/03/2024 - Hoje realizei a criação de funções para geração de um documento xlsx e imagens para criação dos dados futuros</p>

<p>05/06/2024 - Para fazer as analíses aprimoradas das pixel arts, estou usando a biblioteca skimage -> mas encontrei um problema referente ao uso da metrica Similarity, pois não é possível fazer com imagens menores que 7x7 e em ambito das pixel artes existem várias utilizadas que em pelo menos um dos lados tem menos de 7 pixels, oque torna essa metrica impossivel de ser usada </p>
