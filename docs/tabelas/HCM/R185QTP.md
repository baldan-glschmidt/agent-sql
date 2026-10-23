# R185QTP

## Descrição

Orçamento Individual - Qtde de Colaboradores - Posto

---

## Resumo

- Campos: 12
- Chave Primária: 7 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da empresa |
| CmpOrc | Date | Não | Competência do orçamento |
| EstPos | Number(003,0) | Não | Código da estrutura de postos de trabalho |
| PosTra | String(024) | Não | Código do posto de trabalho |
| AnoBas | Number(004,0) | Não | Ano base de cálculo do orçamento |
| VerOrc | Number(004,0) | Não | Versão do orçamento |
| RevOrc | Number(004,0) | Não | Revisão da versão do orçamento |
| CodCen | Number(004,0) | Sim | Código do cenário |
| IndCal | Number(001,0) | Sim | Tipo de cálculo (1-Base/2-Valor Mensal) |
| QtdCol | Number(004,0) | Sim | Quantidade total de colaboradores |
| QtdEfe | Number(004,0) | Sim | Quantidade de colaboradores efetivos |
| QtdVar | Number(004,0) | Sim | Quantidade de variação do quadro |

---

## Chave Primária

- NumEmp
- CmpOrc
- EstPos
- PosTra
- AnoBas
- VerOrc
- RevOrc

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R185QTP_003

**Tabela:** R017POS

| Origem | Destino |
|--------|---------|
| EstPos | EstPos |
| PosTra | PosTra |

### IR_R185QTP_006

**Tabela:** R185REV

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| AnoBas | AnoBas |
| VerOrc | VerOrc |
| RevOrc | RevOrc |

