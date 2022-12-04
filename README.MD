 <h1 align="center"> Northwest Real Estate Agency </h1>

![Getting Started](/images/img_readme.jpg)

# Sejam bem-vindos ao meu projeto de portfólio de negócio da empresa fictícia Northwest Real Estate Agency.
###### [Visualizar projeto](https://ricardoffdev-nrea-project-dashboard-muvf30.streamlit.app/)

## 1. O Problema do Negócio

Nesse projeto de negócio irei analisar um banco de dados real. Este banco de dados público, foi  disponibilizado pelo website de competições de Data Science, o Kaggle.
A empresa Northwest Real Estate Agency tem como objetivo realizar a compra e venda de imóveis na cidade de Seattle. Para isso a empresa necessita de uma análise precisa de todas as informações e assim poder obter o lucro desejado na compra e venda de imóveis.

## 1.1 Contexto de negócio

Nesse banco de dados iremos encontrar 21.613 entradas que datam de 02/05/2014 até 27/05/2015. Todas as entradas são de imóveis únicos da cidade de Seattle, situada na costa do pacífico nos EUA.

## 1.2 Questões do time de negócios

#### -> Estimar quais são as melhores opções de compra e em qual valor?

#### -> Após adquirido o imóvel, qual é a margem de lucro que será inserida para a venda?

## 2. Planejamento prévio

## 2.1 Ferramentas

* Python 3.10
* Visual Studio Code
* Jupyter Notebook
* PyCharm Community Ed.
* Seaborn
* Plotly
* Plotly Express
* Pandas
* Numpy
* Folium
* Geopandas
* Streamlit-Folium
* Streamlit Web Apps 


## 2.2 Produto final

Página Web com as seguintes informações:
As sugestões de compra dos imóveis e o valor recomendado.
O valor recomendado para a venda dos imóveis adquiridos.
Os seis principais insights.

## 3. Estudo do negócio

O mercado de imóveis de Seattle é muito competitivo. As casas em Seattle recebem, na média, duas ofertas de venda a cada 14 dias.  Em Seattle por mês são comercializados U$843.000,00 na média, só no mercado imobiliário. Esse valor cresce na média de 7,3% ao ano. O preço médio de venda do square foot em Seattle é de U$555,00, valores estes do último ano. [fonte](fonte: https://www.redfin.com/city/16163/WA/Seattle/housing-market)


## 4.0 Dados

##### Estes são dados públicos que foram coletados na página web do [Kaggle](https://www.kaggle.com/datasets/harlfoxem/housesalesprediction).

## 4.1 Atributos de origem


|     COLUNA    | DESCRIÇÃO                                                              |
|:-------------:|------------------------------------------------------------------------|
| id            | Identificador único de cada imóvel                                     |
| date          | Data da venda                                                          |
| price         | Preço que foi vendido                                                  |
| bedrooms      | Quantidade de quartos                                                  |
| bathrooms     | Quantidade de banheiros                                                |
| sqft_living   | Área da sala de estar em metros quadrados                              |
| sqft_lot      | Área do lote em metros quadrados                                       |
| floors        | Quantidade de pisos/andares                                            |
| waterfront    | Identificador que informa se o imóvel tem ou não vista para água       |
| view          | Vista do imóvel medida em índice                                       |
| condition     | Condição do imóvel medida em índice                                    |
| grade         | Nota dada ao imóvel baseada no sistema de classificação de King County |
| sqft_above    | Área além do porão medida em metros quadrados                          |
| sqft_basement | Área do porão medida em metros quadrados                               |
| yr_built      | Ano de construção                                                      |
| yr_renovated  | Ano da última reforma feita                                            |
| zipcode       | Código postal                                                          |
| lat           | Latitude                                                               |
| long          | Longitude                                                              |
| sqft_living15 | Área da sala de estar para os quinze vizinhos mais próximos            |
| sqft_lot15    | Área da sala de estar para os quinze vizinhos mais próximos            |

## 4.2 Detalhamento dos atributos de origem

* waterfront: 0 = não, 1 = sim
* view: 0 = Sem vista, 1 = Razoável, 2 = Média, 3 = Boa, 4 = Excelente
* yr_renovated: ano de reforma ou ‘0’ se nunca renovado.
* bathrooms: Nos EUA existem banheiros completos que obrigatóriamente possuem quatro acessórios de encanamento. Um banheiro completo contém pelo menos um lavatório, um sanitário, um chuveiro e uma banheira. O banheiro que aparece com 0.5, representa um banheiro com sanitário e pia, já o banheiro 0.75 é um banheiro que contém um lavatório, um sanitário e um chuveiro ou banheira.
* condition: 1 = Desgastado. Reparação e revisão necessária em superfícies pintadas, coberturas, canalizações, aquecimento e numerosas insuficiências funcionais. 
* 2 = Bastante desgastado. É necessária muita reparação.
* 3 = Média. Algumas provas de manutenção diferida e obsolescência normal com a idade, na medida em que algumas pequenas reparações são necessárias, juntamente com alguns retoques.
* 4 = Bom. Não é necessária manutenção óbvia, mas também não é tudo novo.
* 5= Muito Bom. Todos os artigos bem conservados, muitos dos quais foram renovados e reparados à medida que mostraram sinais de desgaste, aumentando a esperança de vida e diminuindo a idade efetiva com pouca deterioração ou obsolescência evidente com um elevado grau de utilidade.
* grade: (1-3): abaixo dos padrões mínimos de construção.
* 4: Geralmente mais antiga, construção de baixa qualidade.
* 5: Baixos custos de construção e mão-de-obra. Projeto pequeno e simples.
* 6: A avaliação mais baixa que cumpre atualmente o código de construção. Materiais de baixa qualidade e projeto arquitetônico simples.
* 7: tem um nível médio de construção e concepção.
* 8: Um pouco acima da média em construção e concepção. Normalmente melhores materiais tanto no trabalho de acabamento exterior como interior.
* 9: Melhor design arquitetônico com design e qualidade extra no interior e exterior.
* 10: Casas com esta qualidade têm geralmente características de alta qualidade. Os trabalhos de acabamento são melhores e mais qualidade de design é vista nas plantas dos pisos. Geralmente têm um tamanho maior.
* 11: Desenho personalizado e trabalhos de acabamento de maior qualidade com comodidades acrescidas de madeiras maciças, instalações sanitárias e opções mais luxuosas.
* 12: Desenho à medida e excelentes construtores. Todos os materiais são da mais alta qualidade e todas as conveniências estão presentes.
* 13: Geralmente concebidos e construídos à medida. Nível de mansão. Grande quantidade de trabalho de armário da mais alta qualidade, acabamentos em madeira, mármore, formas de entrada, etc.

## 4.3 Atributos criados

|     COLUNA      | DESCRIÇÃO                                                                |
|:---------------:|--------------------------------------------------------------------------|
| date_str        | Data de venda no formato Dia/Mês/Ano                                   |
| year            | Ano da venda do imóvel                                                 |
| month           | Mês da venda do imóvel                                                 |
| seasons         | Estação do ano que imóvel foi vendido                                  |    
| living_m2       | Tamanho (m²) do espaço interior (área construída) dos imóveis          |
| lot_m2          | Tamanho (m²) do terreno onde o imóvel está situado                     |
| above_m2        | Tamanho (m²) do espaço interior que se encontra acima do nível do solo |
| age             | Idade do imóvel. (Ano atual - Ano Construção)                          |
| renovated       | Se foi reformado                                                       |
| living_price_m2 | Preço do imóvel pela área da sala de estar em m²                       |
| lot_price_m2    | Preço do imóvel pela área do lote em m²                                |
| price_m2_total  | Preço do imóvel pela área total em m²                                  |

## 4.4 Detalhamento atributos criados

Estações do ano (seasons):
Verão = de junho a agosto.
Outono = de setembro a novembro.
Inverno = de dezembro a fevereiro.
Primavera = de março a maio.

m2_living, m2_lot e m2_above:
Converteu a unidade de medida de área dividindo o valor em pé quadrado por 10,764.

m2_outside:
Para calcular a área externa dos imóveis, subtraiu-se do tamanho de seus terrenos o valor da divisão entre a área construída acima do nível do solo sob os andares.

price_per_m2_living:
Analisar o preço do imóvel tirando o impacto do tamanho de área construída dele. Preço/área construída(m2)

price_per_m2_living_outside:
Analisar o preço do imóvel tirando o impacto do tamanho de área construída e a área externa. Preço/ (área construída(m2) + área externa(m2) ).

## 5. Premissas

Dados Faltantes: nenhum dos atributos do dataset possui dados faltantes
Imóveis Duplicados: existem 177 imóveis que estão duplicados no dataset, ou seja, significa que foram vendidos mais de uma vez em períodos distintos ao longo do tempo que abrange a coleta de dados dos imóveis. 
Valor ‘outlier’ para número de quartos: há um único imóvel que possui 33 quartos, porém ao se realizar um cruzamento de dados, como por exemplo o tamanho total do terreno deste imóvel, foi possível afirmar que este dado é inverídico. Além disso, analisou-se outros imóveis com faixa de preço, faixa de tamanho interno do imóvel, quantidade de banheiros e andares semelhante a esse imóvel e a quantidade média de quartos nos imóveis analisados foi de 2,98.
Imóveis com zero quartos ou zero banheiros: existem 16 imóveis com zero quartos ou zero banheiros na base de dados, assumiremos que estão corretos e não serão excluídos dado que os imóveis podem não ser para uso residencial, de moradia.

## 6. Seis Principais Insights

#### H1: Imóveis com nível de condição maior ou igual a 3 são 20% mais caras, na média.
X Falsa:
Os imóveis da categoria 3, 4 e 5 custam 153.22% a mais na média geral

#### H2: Imóveis com até 50 anos que foram reformados são 20% mais caros do que os não reformados, na média?
X Falsa:
Considerando o preço médio, ao invés de 20% mais caros, os imóveis com até 50 de idade reformados são 69.33% mais caros.

#### H3: Imóveis que possuem vista para água, são 30% mais caros, na média.
X Falsa:
Considerando o preço médio, ao invés de 30%, os imóveis com vista para a água custam 212.63% a mais na média

#### H4: Imóveis com data de construção menor que 1955, são 50% mais baratos, na média.
X Falsa:
Considerando o preço médio, imóveis com data de construção menor que 1955, possuem preços 1,09% mais baratos.

#### H5: Os imóveis das últimas décadas são mais valiosos?
✔️ Verdadeira:
A avaliação dos imóveis construídos nas últimas três décadas encontra-se em média cerca de 19% acima da avaliação dos imóveis
construídos entre 1900 e 1959, enquanto que há um crescimento médio de 4,7% por década entre as décadas de 1940 e 1990.

#### H6: O valor mediano do imóveis variam 20% de acordo com a estação do ano?
X Falsa:
Considerando a maior variação no preço mediano, o maio percentual de aumento encontrado foi do inverno para a primavera, onde a mediana foi 8.13% maior.

## 7. Questões de Negócio

As questões de negócio foram solucionadas com embasamento analítico e, também, com a análise exploratória dos dados.
Quais são os imóveis que a Northwest Real Estate Agency deveria comprar e por qual preço ?
Os imóveis foram agrupados por região ( zipcode ) e dentro de cada região, encontrei a mediana dos preços por área construída.
Irei sugerir a compra dos imóveis que possuem preço abaixo da mediana da região, estejam em boas condições de conservação maior ou igual a 3, que tenham um ou mais banheiros e quartos e, também, devem ter uma grade de classificação maior ou igual a 7.
Todos os imóveis que estão dentro destes filtros de compra serão separados em uma lista.
Dentro desta lista separei os dois imóveis prioritários para aquisição, já que os mesmos possuem 'Vista para a Água'.
Uma vez que o imóvel foi comprado, por qual preço vendê-los e qual é a melhor época para concretizar a venda?
Agruparei os imóveis por região ( zipcode ) e por estação do ano. Dentro de cada região e estação, irei calcular a mediana do preço. Em seguida calcularemos o percentual de lucro base sobre os imóveis comprados. Assim poderemos ter uma clara noção do preço de venda e também do lucro resultado. 

## 8.0 Conclusão

Os objetivos almejados inicialmente foram cumpridos no que tange a lista de recomendações de imóveis para compra, bem como, a projeção do valor de venda desses imóveis. Além disso, conseguiu-se obter 5 principais insights da base de dados estudada e por fim, tudo isso foi colocado em uma aplicação na nuvem o que facilita o acesso a todas as análises realizadas.
Sobre os resultados encontrados, pode-se perceber bastante influência do atributo área construída (área interna) do imóvel no preço, dessa forma, buscou-se retirar seu impacto ao comparar outros atributos com o preço para que assim, a análise não ficasse enviesada.
Aferimos então que o presente projeto se torna mais um exemplo da importância do uso de dados para auxiliar os times de negócio nas suas tomadas de decisões dentro da empresa. Também podemos apontar, que além das ferramentas usuais de tecnologia e estatística, o conhecimento vindo das mais diversas áreas pode impactar na qualidade da análise dos dados.
Além disso, a geração de insights pode nos trazer novas perguntas ou até mesmo novas análises sob todos os dados diferentes unindo assim o negócio no seu âmago e a análise exploratória de dados.

## 9.0 Próximos Passos

Usar algoritmos de Machine Learning para recomendar o preço estimado de venda e compra. Usar clusterização para fazer análise de comparação de imóveis.
Compartilhar todos os Insights gerados com os outros times da empresa ,e assim alcançar novos horizontes. Toda nova idéia que gere discussões e contradições no projetos, serão sempre muito bem-vindas. Afinal quanto mais compartilhado for o conhecimento, melhores serão os resultados produzidos.



