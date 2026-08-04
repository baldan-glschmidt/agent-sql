# E027LSF

## Descrição

Ligação entre situação/classificação tributária do CBS/IBS e NCM

---

## Resumo

- Campos: 12
- Chave Primária: 1 campo(s)
- Índices: 4
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| IdeUni | Number(009,0) | Não | Identificador de ligacão do cClassTrib |
| IdeScr | Number(009,0) | Não | Identificador do cClassTrib |
| CodEmp | Number(004,0) | Sim | Código da empresa |
| CodFil | Number(005,0) | Sim | Código da filial |
| FinCib | String(003) | Sim | Aplicação da CBS/IBS |
| CodClf | String(003) | Sim | Código interno da classificação fiscal |
| NopOpe | String(005) | Sim | Natureza de operação |
| IdeNbs | Number(009,0) | Sim | Identificador NBS |
| IdeStr | Number(009,0) | Sim | Código da cClassTrib Tributado quando operação for desonerada |
| VigIni | Date | Não | Vigência inicial |
| VigFin | Date | Sim | Vigência final |
| OriMer | String(001) | Sim | Origem fiscal da mercadoria |

---

## Chave Primária

- IdeUni

---

## Índices

### E027LSF_UK

**Tipo:** Unico

Campos:
- CodEmp
- CodFil
- CodClf
- IdeNbs
- NopOpe
- FinCib
- VigIni
- VigFin
- OriMer

### E027LSFIndice1

**Tipo:** Não unico

Campos:
- IdeScr

### E027LSFIndice2

**Tipo:** Não unico

Campos:
- CodClf

### E027LSFIndice3

**Tipo:** Não unico

Campos:
- IdeNbs

---

## Relacionamentos

### IR_E027LSF_001

**Tabela:** E027SCR

| Origem | Destino |
|--------|---------|
| IdeScr | IdeUni |

