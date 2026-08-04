# E066TOC

## Descrição

Cadastros - Taxas de Operadoras de Cartão de Débito/Crédito

---

## Resumo

- Campos: 5
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodOpe | Number(004,0) | Não | Código da operadora |
| NumPar | Number(004,0) | Não | Número Parcela |
| PerRep | Number(005,2) | Sim | Taxa de repasse (em percentual) cobrado pela administradora de cartão |
| SitReg | String(001) | Não | Situação do registro |
| BanCar | String(010) | Não | Nome da bandeira do cartão |

---

## Chave Primária

- CodOpe
- NumPar
- BanCar

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E066TOC_000

**Tabela:** E066OPE

| Origem | Destino |
|--------|---------|
| CodOpe | CodOpe |

