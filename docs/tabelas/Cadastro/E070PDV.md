# E070PDV

## Descrição

Tabelas - Varejo - PDVS

---

## Resumo

- Campos: 10
- Chave Primária: 3 campo(s)
- Índices: 2
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| NumPdv | Number(003,0) | Não | Número sequencial do PDV |
| DesPdv | String(050) | Não | Descrição que identifica o pdv |
| NumCco | String(014) | Sim | Número da conta do PDV para receber as movimentações financeiras |
| CodEqu | Number(003,0) | Sim | Código do equipamento fiscal |
| CodDep | String(010) | Não | Código do depósito |
| SitReg | String(001) | Não | Situação do registro |
| SnfNfc | String(003) | Sim | Série para nota fiscal de consumidor eletrônica |
| IdeUni | Number(009,0) | Não | Identificador único do PDV |

---

## Chave Primária

- CodEmp
- CodFil
- NumPdv

---

## Índices

### E070PDVIndice1

**Tipo:** Unico

Campos:
- IdeUni

### E070PDVIndice2

**Tipo:** Não unico

Campos:
- CodEmp
- CodDep

---

## Relacionamentos

### IR_E070PDV_006

**Tabela:** E205DEP

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodDep | CodDep |

