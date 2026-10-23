# R512LAY

## Descrição

Consulta Web - Layout

---

## Resumo

- Campos: 40
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodPer | Number(004,0) | Não | Perfil de Consulta Web |
| IdeECW | Number(009,0) | Não | Identificador do elemento |
| NomECW | String(140) | Sim | Nome do elemento |
| TipECW | Number(001,0) | Sim | Define o tipo de elemento que compõe o layout do formulário |
| TitECW | String(200) | Sim | Define o título do elemento no formulário |
| ForSCW | Number(001,0) | Sim | Define o formato de apresentação da seção no formulário |
| MinGru | Number(001,0) | Sim | Define se um grupo de elementos do formulário pode ser minimizado |
| EstIni | Number(001,0) | Sim | Define o estado inicial de um grupo ao apresentar o formulário |
| SQLSec | String(2000) | Sim | Define o comando SQL utilizado pelos elementos filhos da seção |
| TctECW | Number(001,0) | Sim | Define o tipo de controle que representa o elemento no formulário |
| CamECW | String(040) | Sim | Campo apresentado no formulário através deste controle |
| RotECW | String(050) | Sim | Rótulo do elemento no formulário |
| LnkECW | Number(001,0) | Sim | Define se o controle é exibido como Link |
| ValPad | String(800) | Sim | Valor padrão do elemento |
| RegCcl | Number(003,0) | Sim | Regra para campo calculado |
| MskCam | String(050) | Sim | Máscara do campo |
| ActECW | Number(001,0) | Sim | Ação executada pelo botão/link |
| ActReg | Number(003,0) | Sim | Regra executada pela ação do botão/link |
| ActMod | String(011) | Sim | Define o modelo de relatório executado pela ação do botão/link |
| ForECW | Number(001,0) | Sim | Define a forma de exibição do controle no formulário |
| TxtDic | String(800) | Sim | Texto apresentado como dica (hint) |
| NovLin | Number(001,0) | Sim | Define se deve apresentar o elemento em uma nova linha |
| BtnIco | Image | Sim | Define o ícone apresentado no botão |
| ArqIco | String(100) | Sim | Nome do arquivo usado como ícone do botão |
| PagGrd | Number(001,0) | Sim | Permite apresentar os registros da grid em diversas páginas |
| PsqGrd | Number(001,0) | Sim | Permite pesquisar registros apresentados na grid |
| RegGrd | Number(001,0) | Sim | Define a quantidade de registros exibida na grid |
| MosGrd | Number(001,0) | Sim | Define se o campo deve ser exibido na grid |
| MosDet | Number(001,0) | Sim | Mostrar no formulário |
| ColOrd | Number(001,0) | Sim | Define se o usuário pode ordenar os registros da grid através desta coluna |
| ColAgr | Number(001,0) | Sim | Indica se a coluna será usada para agrupar os registros da grid |
| SeqECW | Number(003,0) | Sim | Sequência do elemento no grupo |
| ECWPai | Number(009,0) | Sim | Identificador do elemento (seção/grid) que contém o elemento atual |
| DesLis | Number(001,0) | Sim | Define se o sistema deve usar a descrição da lista |
| NomLis | String(050) | Sim | Nome da lista ligada ao campo |
| LarExi | Number(004,0) | Sim | Largura de exibição do campo (pixels) |
| AtrECW | String(200) | Sim | Atributos adicionais do elemento |
| TitTBS | Number(001,0) | Sim | Utilizar descrição do TBS |
| RotTBS | Number(001,0) | Sim | Utilizar descrição do TBS |
| ActPer | Number(004,0) | Sim | Perfil executado pela ação do botão |

---

## Chave Primária

- CodPer
- IdeECW

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R512LAY_000

**Tabela:** R512PER

| Origem | Destino |
|--------|---------|
| CodPer | CodPer |

