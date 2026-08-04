# E000LPD

## Descrição

Tabelas - Integrações - Ligação Produto X Depósitos

---

## Resumo

- Campos: 6
- Chave Primária: 1 campo(s)
- Índices: 3
- Relacionamentos: 5

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| SeqInt | Number(009,0) | Não | Número sequencial dos registros de integração |
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| CodPro | String(014) | Não | Código do produto |
| CodDer | String(007) | Não | Código da derivação |
| CodDep | String(010) | Não | Código do depósito |

---

## Chave Primária

- SeqInt

---

## Índices

### E000LPDIndice1

**Tipo:** Unico

Campos:
- CodEmp
- CodFil
- CodDep
- CodPro
- CodDer

### E000LPDIndice2

**Tipo:** Não unico

Campos:
- CodEmp
- CodPro
- CodDer

### E000LPDIndice3

**Tipo:** Não unico

Campos:
- CodEmp
- CodDep

---

## Relacionamentos

### IR_E000LPD_001

**Tabela:** E070EMP

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |

### IR_E000LPD_002

**Tabela:** E070FIL

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodFil | CodFil |

### IR_E000LPD_003

**Tabela:** E075PRO

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodPro | CodPro |

### IR_E000LPD_004

**Tabela:** E075DER

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodPro | CodPro |
| CodDer | CodDer |

### IR_E000LPD_005

**Tabela:** E205DEP

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodDep | CodDep |

