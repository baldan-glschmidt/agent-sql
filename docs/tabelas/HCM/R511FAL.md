# R511FAL

## Descrição

Avaliação - Formulário de avaliação - layout

---

## Resumo

- Campos: 54
- Chave Primária: 2 campo(s)
- Índices: 1
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodPfa | Number(004,0) | Não | Código do perfil do formulário de avaliação |
| IdeEll | Number(009,0) | Não | Identificador do elemento do formulário de avaliação |
| NomEll | String(060) | Sim | Nome do elemento do formulário de avaliação |
| TipEll | Number(001,0) | Sim | Define o tipo de elemento que compõe o layout do formulário |
| TitEll | String(200) | Sim | Define o título do elemento do layout |
| TipSec | Number(001,0) | Sim | Determina quais dados estão disponíveis para seus subelementos |
| ForSec | Number(001,0) | Sim | Define o formato de apresentação da seção no formulário da avaliação |
| AbeDia | Number(001,0) | Sim | Define como ocorrerá a abertura de uma caixa de diálogo |
| ModDia | Number(001,0) | Sim | Define se a caixa de diálogo será aberta de forma modal |
| MinGru | Number(001,0) | Sim | Define se um grupo de elementos do formulário da avaliação pode ser minimizado |
| EstIni | Number(001,0) | Sim | Define o estado inicial de um grupo ao apresentar o formulário de avaliação |
| RegSec | Number(003,0) | Sim | Define a exibição de um botão de acordo com a disponibilidade de uma ação |
| TctEll | Number(001,0) | Sim | Define o tipo de controle que representará o elemento do layout |
| CamEle | Number(002,0) | Sim | Campo apresentado no formulário através deste controle |
| RotEll | String(050) | Sim | Rótulo do elemento do layout |
| ValPad | String(800) | Sim | Valor padrão |
| RegCcl | Number(003,0) | Sim | Regra para campo calculado |
| MskCam | String(050) | Sim | Máscara do campo |
| CamObr | Number(001,0) | Sim | Obrigatoriedade do campo |
| CamEdt | Number(001,0) | Sim | Editabilidade do campo |
| TabBas | Number(001,0) | Sim | Tabela-base da grid |
| FilSql | String(2000) | Sim | Filtro avançado - comando SQL aplicado para filtrar os registros da tabela-base |
| NomCol | String(040) | Sim | Nome do campo apresentado na coluna da grid |
| ColOrd | Number(001,0) | Sim | Define se o usuário pode ordenar os registros da grid através desta coluna |
| ColAgr | Number(001,0) | Sim | Indica se a coluna será usada para agrupar os registros da grid |
| RegVal | Number(003,0) | Sim | Regra de validação executada na saída do campo |
| BtnAct | Number(002,0) | Sim | Ação executada pelo botão |
| BtnReg | Number(003,0) | Sim | Regra executada pelo elemento botão |
| BtnMod | String(011) | Sim | Define o modelo de relatório executado pelo botão |
| BtnIco | Image | Sim | Ícone apresentado ao lado do elemento |
| ArqIco | String(100) | Sim | Nome do arquivo usado como ícone do botão |
| ForExi | Number(001,0) | Sim | Define o tipo de elemento HTML usado para representar |
| OriDic | Number(001,0) | Sim | Define a origem da informação apresentada na dica de preenchimento |
| TxtDic | String(800) | Sim | Texto apresentado como dica de preenchimento do campo |
| CamDic | Number(001,0) | Sim | Campo usado como dica de preenchimento |
| RegDic | Number(003,0) | Sim | Regra usada para personalizar o texto da dica de preenchimento |
| AprDic | Number(001,0) | Sim | Define quando a dica de preenchimento será apresentada |
| PagGrd | Number(001,0) | Sim | Permite apresentar os registros da grid em diversas páginas |
| PsqGrd | Number(001,0) | Sim | Permite pesquisar registros apresentados na grid |
| NovLin | Number(001,0) | Sim | Define se deve apresentar o elemento em uma nova linha |
| SeqEll | Number(003,0) | Sim | Sequência do elemento no grupo |
| EllPai | Number(009,0) | Sim | Identificador do elemento (seção/grid) que contém o elemento atual |
| RegExi | Number(003,0) | Sim | Regra usada para definir se a seção deve ser apresentada no formulário |
| GrfLar | Number(004,0) | Sim | Define a largura do gráfico em pixels |
| GrfAlt | Number(004,0) | Sim | Define a altura do gráfico em pixels |
| GrfTem | Number(002,0) | Sim | Define qual é o nome do tema aplicado no gráfico de radar (Radar Chart) |
| GrfLeg | Number(001,0) | Sim | Define se a legenda do gráfico radar deve ser exibida |
| GrfPoL | Number(001,0) | Sim | Define a posição da legenda do gráfico radar |
| PagIni | Number(009,0) | Sim | Identificador da página inicial |
| MosDef | Number(001,0) | Sim | Define se deve apresentar o elemento na situação Definição (Av. resultados) |
| MosAva | Number(001,0) | Sim | Define se deve apresentar o elemento na situação Avaliação (Av. resultados) |
| MosCan | Number(001,0) | Sim | Define se deve apresentar o elemento na situação Cancelada (Av. resultados) |
| MosCon | Number(001,0) | Sim | Define se deve apresentar o elemento na situação Concluída (Av. resultados) |
| ExiAct | Number(002,0) | Sim | Define a exibição de um botão de acordo com a disponibilidade de uma ação |

---

## Chave Primária

- CodPfa
- IdeEll

---

## Índices

### R511FALIndice2

**Tipo:** Não unico

Campos:
- CodPfa
- EllPai

---

## Relacionamentos

### IR_R511FAL_000

**Tabela:** R511FAP

| Origem | Destino |
|--------|---------|
| CodPfa | CodPfa |

