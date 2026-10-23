# R046IDE

## Descrição

Informações demonstrativo pagamento - Eventos

---

## Resumo

- Campos: 8
- Chave Primária: 6 campo(s)
- Índices: 2
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do colaborador |
| CodCal | Number(005,0) | Não | Código do Cálculo |
| TabEve | Number(003,0) | Não | Código da Tabela de Eventos |
| CodEve | Number(004,0) | Não | Código do Evento |
| RefEve | Number(011,2) | Sim | Referência Evento |
| ValEve | Number(011,2) | Sim | Valor do Evento |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- CodCal
- TabEve
- CodEve

---

## Índices

### R046IDEIndice2

**Tipo:** Não unico

Campos:
- CodCal
- CodEve

### R046IDEIndice3

**Tipo:** Não unico

Campos:
- CodCal
- TipCol
- NumCad
- NumEmp
- CodEve
- RefEve
- ValEve

---

## Relacionamentos

### IR_R046IDE_003

**Tabela:** R044CAL

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodCal | CodCal |

### IR_R046IDE_005

**Tabela:** R008EVC

| Origem | Destino |
|--------|---------|
| TabEve | CodTab |
| CodEve | CodEve |

