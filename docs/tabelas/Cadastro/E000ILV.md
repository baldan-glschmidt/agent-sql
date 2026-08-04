# E000ILV

## Descrição

Tabelas - Lista de Presentes - Itens Vendidos

---

## Resumo

- Campos: 11
- Chave Primária: 1 campo(s)
- Índices: 2
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| IdeIlv | Number(009,0) | Não | Número de sequência do item |
| IdeIlp | Number(009,0) | Não | Número de sequência do item solicitado |
| QtdVen | Number(014,5) | Sim | Quantidade vendida do item |
| DocVen | String(250) | Sim | Dados referentes ao documento de venda |
| DatVen | Date | Sim | Data da venda do item |
| HorVen | Number(005,0) | Sim | Hora da venda do item |
| FilVen | Number(005,0) | Não | Código da filial responsável venda do item |
| CodPro | String(014) | Sim | Código do produto vendido |
| CodDer | String(007) | Sim | Código da derivação do produto vendido |
| CodRep | Number(009,0) | Não | Código do representante responsável pela venda |
| NomCli | String(100) | Sim | Nome do cliente que realizou a compra |

---

## Chave Primária

- IdeIlv

---

## Índices

### E000ILVIndice1

**Tipo:** Não unico

Campos:
- IdeIlp

### E000ILVIndice2

**Tipo:** Não unico

Campos:
- CodRep

---

## Relacionamentos

### IR_E000ILV_001

**Tabela:** E000ILP

| Origem | Destino |
|--------|---------|
| IdeIlp | IdeIlp |

### IR_E000ILV_009

**Tabela:** E090REP

| Origem | Destino |
|--------|---------|
| CodRep | CodRep |

