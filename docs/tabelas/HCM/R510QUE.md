# R510QUE

## Descrição

Currículo Web - Questionários

---

## Resumo

- Campos: 4
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 3

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodPer | Number(003,0) | Não | Código do perfil |
| IdiLay | Number(001,0) | Não | Idioma do layout - define o idioma de apresentação |
| EstCar | Number(004,0) | Não | Código da Estrutura de Cargos |
| CodGrq | Number(003,0) | Não | Código Grupo Questionário |

---

## Chave Primária

- CodPer
- IdiLay
- EstCar
- CodGrq

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R510QUE_000

**Tabela:** R510PER

| Origem | Destino |
|--------|---------|
| CodPer | CodPer |

### IR_R510QUE_002

**Tabela:** R024EST

| Origem | Destino |
|--------|---------|
| EstCar | EstCar |

### IR_R510QUE_003

**Tabela:** R118GRQ

| Origem | Destino |
|--------|---------|
| EstCar | EstCar |
| CodGrq | CodGrq |

