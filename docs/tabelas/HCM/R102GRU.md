# R102GRU

## Descrição

Grupo da Brigada

---

## Resumo

- Campos: 10
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 3

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodBri | Number(003,0) | Não | Código da Brigada |
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do Colaborador |
| DatEng | Date | Não | Data do Engajamento |
| CodFnb | Number(003,0) | Sim | Função do Grupo |
| GruSan | String(003) | Sim | Grupo Sanguíneo |
| DatSai | Date | Sim | Data da Saída |
| ObsGru | String(100) | Sim | Observação do Grupo |
| MotSai | Number(003,0) | Sim | Código do  motivo da saída |

---

## Chave Primária

- CodBri
- NumEmp
- TipCol
- NumCad
- DatEng

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R102GRU_000

**Tabela:** R102BRI

| Origem | Destino |
|--------|---------|
| CodBri | CodBri |

### IR_R102GRU_003

**Tabela:** R034FUN

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |

### IR_R102GRU_005

**Tabela:** R102FNB

| Origem | Destino |
|--------|---------|
| CodFnb | CodFnb |

