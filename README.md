<h1 align="center">Lumixy</h1>

<p>Este é um TCC focado em desenvolvimento que tem como ideal trazer o ambiente de iluminação para objetos e paisagens bidimensionais
Trabalhos Similares (Relight): https://clipdrop.co/relight</p>

<p> O trabalho será feito em python e irá recuperar uma imagem em formato png e uma posição de luz dentro da imagem para realizar uma segmentação, detecção de profundidade de cada uma dos grupos segmentados, para por fim executar uma série de calculos sobre cada pixel, para iluminar a imagem de maneira consisa e coesa</p>

<p>30/03/2024 - Hoje realizei a criação de funções para geração de um documento xlsx e imagens para criação dos dados futuros</p>

<p>05/06/2024 - Para fazer as analíses aprimoradas das pixel arts, estou usando a biblioteca skimage -> mas encontrei um problema referente ao uso da metrica Similarity, pois não é possível fazer com imagens menores que 7x7 e em ambito das pixel artes existem várias utilizadas que em pelo menos um dos lados tem menos de 7 pixels, oque torna essa metrica impossivel de ser usada </p>

<p>26/06/2024 - Com a análise pronta em mãoes com 50 pixel artes, iniciei buscando uma forma de segmentar todas elas em grupos de pixel arte, entre grupo pequeno & Médio, Grande, Muito Grande e utilizei de alguns conceitos de estatísticas para isso:</p>
Você está certo, o valor da média deve ser utilizado de maneira mais eficaz na definição dos grupos. Podemos usar a média e o desvio padrão para criar intervalos mais estatisticamente informados para os grupos. Vamos seguir um método mais detalhado:

**Média:**

$\ \text{Média} = \frac{\sum x_i}{N} = \frac{258197}{50} = 5163.94 \$

$\ \text{onde } 258197 \text{ é a soma de todos os tamanhos de todas as pixel artes} \$

**Desvio padrão:**

$\ \text{Desvio padrão} = \sqrt{\frac{\sum (x_i - \text{Média})^2}{N}} \$

para fazer as margens entre os tamanhos de pixel arte vamos utilizar de um calculo como esse

- Grupo 1: Dados menores que (Média - Desvio padrão)
- Grupo 2: Dados entre (Média - Desvio padrão) e Média
- Grupo 3: Dados entre Média e (Média + Desvio padrão)
- Grupo 4: Dados maiores que (Média + Desvio padrão)

Dessa forma, os grupos criados apartir deste calculo são os seguintes:

**Grupo 2:**
63, 143, 144, 169, 192, 195, 342, 360, 567, 957, 960, 1024, 1024, 1024, 1024, 1024, 1024, 1024, 1024, 1024, 1024, 1024, 1024, 1024, 1024, 1024, 1024, 1024, 1024, 1024, 1024, 1024, 1024, 1024, 1024, 1485, 1485, 1932, 2048, 2268

**Grupo 3:**
6400, 7168, 7371, 8960, 8960, 10752, 13625

**Grupo 4:**
16616, 45056, 4505
