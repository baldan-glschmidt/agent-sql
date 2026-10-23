# R079EDE

## Descrição

Avaliação de Excelência - Notas - Detalhamento

---

## Resumo

- Campos: 9
- Chave Primária: 8 campo(s)
- Índices: 0
- Relacionamentos: 3

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Código do Colaborador |
| CmpAva | Date | Não | Competência da Avaliação |
| TipAva | Number(004,0) | Não | Sequência da Avaliação |
| CodHpe | String(004) | Não | Código da Habilidade Pessoal |
| CodAva | Number(004,0) | Não | Código da avaliação detalhada |
| CodIte | Number(003,0) | Não | Código do item de avaliação |
| NotAva | Number(005,2) | Sim | Nota da Avaliação da Habilidade |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- CmpAva
- TipAva
- CodHpe
- CodAva
- CodIte

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R079EDE_004

**Tabela:** R079AEA

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |
| CmpAva | CmpAva |
| TipAva | TipAva |

### IR_R079EDE_005

**Tabela:** R079HPE

| Origem | Destino |
|--------|---------|
| CodHpe | CodHpe |

### IR_R079EDE_007

**Tabela:** R077IAD

| Origem | Destino |
|--------|---------|
| CodAva | CodAva |
| CodIte | CodIte |

