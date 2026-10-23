# R077CDE

## Descrição

Avaliação de Conhecimentos - Notas - Detalhamento

---

## Resumo

- Campos: 10
- Chave Primária: 9 campo(s)
- Índices: 0
- Relacionamentos: 3

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Código do Colaborador |
| CmpAva | Date | Não | Competência de Geração da Avaliação |
| TipAva | Number(004,0) | Não | Sequência da Avaliação |
| FamCnc | String(004) | Não | Família do Conhecimento |
| CodCnc | String(005) | Não | Código do Conhecimento |
| CodAva | Number(004,0) | Não | Código da avaliação detalhada |
| CodIte | Number(003,0) | Não | Código do item de avaliação |
| NotAva | Number(005,2) | Sim | Nota da Avaliação do Conhecimento |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- CmpAva
- TipAva
- FamCnc
- CodCnc
- CodAva
- CodIte

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R077CDE_004

**Tabela:** R077ACT

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |
| CmpAva | CmpAva |
| TipAva | TipAva |

### IR_R077CDE_006

**Tabela:** R125CNC

| Origem | Destino |
|--------|---------|
| FamCnc | FamCnc |
| CodCnc | CodCnc |

### IR_R077CDE_008

**Tabela:** R077IAD

| Origem | Destino |
|--------|---------|
| CodAva | CodAva |
| CodIte | CodIte |

