# R064FOL

## Descrição

Programação de Folga - TC

---

## Resumo

- Campos: 10
- Chave Primária: 4 campo(s)
- Índices: 1
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro Colaborador |
| DatIni | Date | Não | Data Inicial |
| DatFim | Date | Sim | Data Final |
| TipFol | Number(002,0) | Sim | Tipo de Folga |
| TipOco | Number(003,0) | Sim | Tipo de Ocorrência para Ficha Funcional |
| EmpSub | Number(004,0) | Sim | Código da Empresa do Substituto |
| TClSub | Number(001,0) | Sim | Tipo de Colaborador Substituto |
| CadSub | Number(009,0) | Sim | Cadastro do Substituto |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- DatIni

---

## Índices

### R064FOLIndice2

**Tipo:** Não unico

Campos:
- EmpSub
- TClSub
- CadSub

---

## Relacionamentos

Nenhum relacionamento cadastrado.
