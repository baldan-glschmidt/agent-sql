# R124HSE

## Descrição

Colaborador - Parecer Selecionador

---

## Resumo

- Campos: 9
- Chave Primária: 4 campo(s)
- Índices: 1
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo de Colaborador |
| NumCad | Number(009,0) | Não | Cadastro Colaborador Candidato |
| DatHpa | Date | Não | Data do Parecer |
| EmpCse | Number(004,0) | Sim | Empresa Selecionador |
| OriCse | Number(001,0) | Sim | Tipo de Selecionador |
| NumCse | Number(009,0) | Sim | Cadastro do Selecionador |
| CodPse | Number(003,0) | Sim | Código do Parecer Selecionador |
| CmtPse | String(2000) | Sim | Comentário do Selecionador |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- DatHpa

---

## Índices

### R124HSEIndice2

**Tipo:** Não unico

Campos:
- EmpCse
- OriCse
- NumCse

---

## Relacionamentos

### IR_R124HSE_002

**Tabela:** R034FUN

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |

