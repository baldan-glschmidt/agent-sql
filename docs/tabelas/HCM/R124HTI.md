# R124HTI

## Descrição

Colaborador - Times Pretendidos

---

## Resumo

- Campos: 6
- Chave Primária: 6 campo(s)
- Índices: 0
- Relacionamentos: 3

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo de Colaborador Candidato |
| NumCad | Number(009,0) | Não | Cadastro do Candidato |
| DatSol | Date | Não | Data da Solicitação |
| CodSol | Number(003,0) | Não | Tipo da Solicitação |
| CodTim | String(008) | Não | Código do Time |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- DatSol
- CodSol
- CodTim

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R124HTI_002

**Tabela:** R034FUN

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |

### IR_R124HTI_004

**Tabela:** R114SLC

| Origem | Destino |
|--------|---------|
| CodSol | CodSlc |

### IR_R124HTI_005

**Tabela:** R078TIM

| Origem | Destino |
|--------|---------|
| CodTim | CodTim |

