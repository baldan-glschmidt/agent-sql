# E072PES

## Descrição

Tabelas - Pesquisa de Mercado

---

## Resumo

- Campos: 18
- Chave Primária: 6 campo(s)
- Índices: 1
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodPro | String(014) | Não | Código do produto |
| CodDer | String(007) | Não | Código da derivação do Produto (tamanho, cor, etc...) |
| CodFor | Number(009,0) | Não | Código do fornecedor |
| CodCli | Number(009,0) | Não | Código do Cliente |
| SeqPes | Number(004,0) | Não | Sequência |
| VlrPro | Number(015,2) | Sim | Valor do Produto da Empresa |
| CodCon | Number(002,0) | Sim | Código do Concorrente |
| VlrCon | Number(015,2) | Sim | Valor do Produto do Concorrente |
| AreEmp | String(030) | Sim | Área ocupada pelo produto da empresa |
| AreCon | String(030) | Sim | Área ocupada pelo produto do concorrente |
| QtdPro | Number(011,2) | Sim | Quantidade Produto da empresa |
| QtdCon | Number(011,2) | Sim | Quantidade do produto do concorrente |
| CodAc1 | Number(002,0) | Sim | Código da Ação 1 |
| CodAc2 | Number(002,0) | Sim | Código da Ação 2 |
| DatPes | Date | Sim | Data da Pesquisa |
| CodRep | Number(009,0) | Não | Código do representante |
| CodPal | Number(003,0) | Sim | Código do Palmtop |

---

## Chave Primária

- CodEmp
- CodPro
- CodDer
- CodFor
- CodCli
- SeqPes

---

## Índices

### E072PESIndice1

**Tipo:** Não unico

Campos:
- CodCli

---

## Relacionamentos

### IR_E072PES_001

**Tabela:** E075PRO

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodPro | CodPro |

### IR_E072PES_004

**Tabela:** E085CLI

| Origem | Destino |
|--------|---------|
| CodCli | CodCli |

