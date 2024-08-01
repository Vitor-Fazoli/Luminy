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

Qualificação do TCC - Análise

- Luiz:
  - apresentou muito bem
  - ficou confuso se iria usar uma ferramenta ou desenvolver
  - a ideia é boa
  - não apresentou a unity e nem a justificativa
  - não explicou: funciona, problema, restrição, objetos, pessoas, ambientes (ver tabela comparativa)
  - avaliar o uso do Godot (problema quando usa 2D e 3D, resposta do Vitor)
  - Anotações do whatsapp:
    Página 06: Objetivos Específicos
Seprar em 2 objetivos (Criar um Protótipo, Desenvolver a Ferrameta)

Página 15: Metodologia
Reescrever o ínicio do primeiro parágrafo. Ficou parecendo uma nota
mental sua

Sugestão para itens da metodologia
3.1, 3.2 3.3 - Achei os itens um pouco confusos, talvez reescrever eles
Exemplo
No item 3.1 você chama o tópico de levantamento de requisitos. Então
poderia conter um paragráfo inicial descrevendo a sua ideia central
e justificando a aplicação de uma ferramenta Relight para essa parte.
No item 3.2 você poderia colocar o tópico mais genérico por exemplo:
"Iluminição em Engine para games" e deixar para falar mais do Unit no seu
item 3.5 que é o item que você justifica quais ferramentas serão
utilizadas

Voltando ao seu objetivo:
O objetivo do trabalho é simular a iluminação em imagens digitais de média e
baixa resolução por meio do desenvolvimento de uma ferramenta.
Oque você definiu no sua metodologia que vai possibilitar alcançar
seu objetivo.

- Arthur:
  - boa apresentação
  - texto precisa ser melhor trabalhado
  - enfatizar o problema
  - foco! o que você vai fazer?
  - não falou do relight
  - motivação precisa melhorar
  - o que diferencia o seu trabalho dos demais? Resolução
  - falar do pixelart (motivação)
  - não ficou claro a questão da marcação manual e uso de IA?
  - lista de requisitos (engenharia de software)
  - vender melhor o peixe