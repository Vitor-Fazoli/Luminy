# lumenin

# Inicial

- **O que é:** Algoritimo de iluminação para pinturas 2D
- Q**uando:** prazo um ano
- **Como:** a definir os processos
- **Porquê:** para auxiliar a criação de imagens com iluminações para auxiliar processos de design
- **Para quem:** será importante para artistas iniciantes ou veteranos para aprimorar o estudo e polpar tempo, aumentar a eficiência

## Estudos iniciais

###testando a funcionalidade de aplicações semelhantes
###Relight:

Gráfico de cores para diferentes estilos de arte

| Azul | Realista |
| --- | --- |
| Vermelho | Desenho |
| Verde | Pixel Arte |

Gráfico Quantitativo de funcionamento do software

| Funciona | 100% |
| --- | --- |
| Restrição | 50% |
| Problema | 0% |

| Imagem | Alta Resolução | Média Resolução | Baixa Resolução |
| --- | --- | --- | --- |
| Objetos | Funciona | Funciona | Restrição |
| Humanos  | Funciona | Funciona | Restrição |
| Paisagens | Funciona | Problema | Problema |

| Imagem | Alta Resolução | Média Resolução | Baixa Resolução |
| --- | --- | --- | --- |
| Objetos |  |  |  |
| Humanos  |  |  |  |
| Paisagens |  | Funciona |  |

| Imagem | Alta Resolução | Média Resolução | Baixa Resolução |
| --- | --- | --- | --- |
| Objetos |  |  |  |
| Humanos  |  |  |  |
| Paisagens |  |  |  |

---

sempre que vemos uma cor clara e logo depois uma escura, isso significa que há relevo muito grande ali, por exemplo 

<p align="center" >
  <img  src="/Documentation/Assets/batman.png"/>
</p>

Fonte: [https://www.boletimnerd.com.br/batman-3-quadrinhos-que-influenciaram-o-novo-filme/](https://www.boletimnerd.com.br/batman-3-quadrinhos-que-influenciaram-o-novo-filme/)

Nesse quadrinho do batman, podemos ver que em seu ombro está muito claro e logo acima onde sua capa está vem uma cor muito escura, isso nos mostra que a profundidade da capa é grande, ao ponto de não chegar nenhuma luz até ela, é claro que precisamos levar em consideração que nas HQ’s em geral os constrastes são muito maiores, porque traz esse volume nos trajes

# Tecnica para iluminação de imagens

você irá criar uma malha por cima de toda a imagem e definir um inteiro para a profundidade, assim cada pixel dá imagem deve receber uma profundidade ideal ( pode ser feito a mão ou por uma ia ) 

<p align="center" >
  <img  src="/Documentation/Assets/exemplo1.png"/>
  <img  src="/Documentation/Assets/exemplo2.png"/>
</p>

Assim ele vai numerar toda a malha de pixels na tela com numeros que podem ter uma variação maior dependendo do tamanho da imagem ( no caso de exemplo)

foi usado de 1 a 9, mas com imagens imensas em full hd podemos pensar em usar de 1 a 100 ou até mais

---

O resultado disso seria que numeros distantes próximos iriam gerar uma deformação quase que 90° na malha, enquanto que numerações próximas iriam gerar variações pequenas

---

Podemos pensar que dessa forma será possivel utilizar essa profundidade para produzir uma luz pelas laterais ou pela frente e até atrás de elementos, sem perder sua funcionalidade até mesmo em imagens pequenas

Além disso, cada um desses valores definidos em cada pixel da imagem, vão servir de referencia para criar
