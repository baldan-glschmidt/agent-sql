# R124HSU

## Descrição

Colaborador - Parecer Superior

---

## Resumo

- Campos: 10
- Chave Primária: 5 campo(s)
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
| SeqHsu | Number(002,0) | Não | Sequência de entrevistas |
| EmpCsu | Number(004,0) | Sim | Empresa Superior |
| OriCsu | Number(001,0) | Sim | Tipo de Superior |
| NumCsu | Number(009,0) | Sim | Cadastro do Superior |
| CodPsu | Number(003,0) | Sim | Código do Parecer Superior |
| CmtPsu | String(2000) | Sim | Comentário do Superior |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- DatHpa
- SeqHsu

---

## Índices

### R124HSUIndice2

**Tipo:** Não unico

Campos:
- EmpCsu
- OriCsu
- NumCsu

---

## Relacionamentos

### IR_R124HSU_002

**Tabela:** R034FUN

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |

