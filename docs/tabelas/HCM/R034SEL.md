# R034SEL

## Descrição

Códigos de Seleção do Empregado

---

## Resumo

- Campos: 4
- Chave Primária: 4 campo(s)
- Índices: 1
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do colaborador |
| CodSel | Number(003,0) | Não | Código de Seleção |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- CodSel

---

## Índices

### R034SELIndice2

**Tipo:** Não unico

Campos:
- CodSel

---

## Relacionamentos

### IR_R034SEL_002

**Tabela:** R034FUN

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |

### IR_R034SEL_003

**Tabela:** R008SEL

| Origem | Destino |
|--------|---------|
| CodSel | CodSel |

