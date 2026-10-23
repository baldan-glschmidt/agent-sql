# R101CPT

## Descrição

Avaliação de Resultado - Objetivos - Competências

---

## Resumo

- Campos: 8
- Chave Primária: 8 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Código do Colaborador |
| CodCic | Number(003,0) | Não | Código do ciclo de avaliação |
| TipAva | Number(002,0) | Não | Sequência do tipo de avaliação |
| SeqAva | Number(002,0) | Não | Sequência da avaliação |
| IdeObj | Number(006,0) | Não | Identificação dos objetivos |
| CodCpt | Number(009,0) | Não | Competência relacionada ao objetivo traçado |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- CodCic
- TipAva
- SeqAva
- IdeObj
- CodCpt

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R101CPT_006

**Tabela:** R101RES

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |
| CodCic | CodCic |
| TipAva | TipAva |
| SeqAva | SeqAva |
| IdeObj | IdeObj |

### IR_R101CPT_007

**Tabela:** R577CPT

| Origem | Destino |
|--------|---------|
| CodCpt | CodCpt |

