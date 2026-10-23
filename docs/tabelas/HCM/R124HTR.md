# R124HTR

## Descrição

Colaborador - Turnos Pretendidos

---

## Resumo

- Campos: 6
- Chave Primária: 6 campo(s)
- Índices: 1
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo de Colaborador Candidato |
| NumCad | Number(009,0) | Não | Cadastro do Candidato |
| DatSol | Date | Não | Data da Solicitação |
| CodSol | Number(003,0) | Não | Tipo da Solicitação |
| CodTur | Number(001,0) | Não | Código do Turno |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- DatSol
- CodSol
- CodTur

---

## Índices

### R124HTRIndice2

**Tipo:** Não unico

Campos:
- NumEmp
- TipCol
- NumCad
- CodTur

---

## Relacionamentos

### IR_R124HTR_002

**Tabela:** R034FUN

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |

