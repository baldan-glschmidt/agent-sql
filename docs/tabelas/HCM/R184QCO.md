# R184QCO

## Descrição

PLR - Questionário do Colaborador

---

## Resumo

- Campos: 10
- Chave Primária: 8 campo(s)
- Índices: 0
- Relacionamentos: 3

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Número da Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Número do Colaborador |
| TipAva | Number(001,0) | Não | Tipo Avaliador |
| CadAva | Number(009,0) | Não | Código do Colaborador Avaliador |
| CmpPpr | Date | Não | Competência de Cálculo de PPR |
| CodGrp | Number(006,0) | Não | Código do Grupo |
| CodIte | Number(003,0) | Não | Código do Item |
| RspPpr | Number(011,2) | Sim | Resposta (Nota) |
| ComQco | String(255) | Sim | Comentário do Questionário |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- TipAva
- CadAva
- CmpPpr
- CodGrp
- CodIte

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R184QCO_002

**Tabela:** R034FUN

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |

### IR_R184QCO_006

**Tabela:** R182GRP

| Origem | Destino |
|--------|---------|
| CodGrp | CodGrp |

### IR_R184QCO_007

**Tabela:** R182GRI

| Origem | Destino |
|--------|---------|
| CodGrp | CodGrp |
| CodIte | CodIte |

