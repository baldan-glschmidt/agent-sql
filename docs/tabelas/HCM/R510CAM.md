# R510CAM

## Descrição

Currículo Web - Campos

---

## Resumo

- Campos: 24
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 3

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodPer | Number(003,0) | Não | Código do perfil |
| IdiLay | Number(001,0) | Não | Idioma do layout - define o idioma de apresentação |
| CodPag | Number(003,0) | Não | Código da Página do Layout |
| CodGru | Number(003,0) | Não | Código do Grupo |
| CodCam | Number(004,0) | Não | Código do campo |
| TipCam | Number(001,0) | Sim | Tipo do campo |
| SeqCam | Number(003,0) | Sim | Sequência do campo |
| NomCam | String(040) | Sim | Nome do campo |
| RotCam | String(050) | Sim | Rótulo do campo |
| DicPre | String(250) | Sim | Dica de preenchimento |
| LarExi | Number(004,0) | Sim | Largura de exibição do campo |
| CamObr | String(001) | Sim | Obrigatoriedade do campo |
| CamEdt | String(001) | Sim | Editabilidade do campo |
| FilCha | String(2000) | Sim | comando SQL aplicado para filtrar os registros da tabela referenciada pelo campo |
| FilEnu | String(200) | Sim | abrangência dos valores exibidos na lista |
| RegVal | Number(003,0) | Sim | Regra de validação |
| NumLin | Number(003,0) | Sim | Número da linha |
| MosGri | String(001) | Sim | Mostrar na grid |
| TabLkp | String(020) | Sim | Tabela lookup do campo |
| NomLis | String(020) | Sim | Nome da lista ligada ao campo |
| CamRes | String(040) | Sim | Nome do campo resultante do lookup |
| ValPad | String(8001) | Sim | Valor padrão |
| MosFor | String(001) | Sim | Mostrar no formulário |
| OpcExi | Number(001,0) | Sim | Opção de exibição para campo estrangeiro |

---

## Chave Primária

- CodPer
- IdiLay
- CodPag
- CodGru
- CodCam

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R510CAM_000

**Tabela:** R510PER

| Origem | Destino |
|--------|---------|
| CodPer | CodPer |

### IR_R510CAM_002

**Tabela:** R510PAG

| Origem | Destino |
|--------|---------|
| CodPer | CodPer |
| IdiLay | IdiLay |
| CodPag | CodPag |

### IR_R510CAM_003

**Tabela:** R510GRU

| Origem | Destino |
|--------|---------|
| CodPer | CodPer |
| IdiLay | IdiLay |
| CodPag | CodPag |
| CodGru | CodGru |

