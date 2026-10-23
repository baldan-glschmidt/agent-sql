# R070MNO

## Descrição

Marcações Não Obrigatórias da Apuração

---

## Resumo

- Campos: 8
- Chave Primária: 5 campo(s)
- Índices: 1
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo de Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do Colaborador |
| DatAcc | Date | Não | Data do Acesso |
| HorAcc | Number(005,0) | Não | Hora do Acesso |
| DatApu | Date | Sim | Data de Apuração da Marcação |
| UsoBat | Number(002,0) | Sim | Uso da Marcação |
| TipMar | Number(001,0) | Sim | Tipo de Marcação |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- DatAcc
- HorAcc

---

## Índices

### R070MNOIndice2

**Tipo:** Não unico

Campos:
- NumEmp
- TipCol
- NumCad
- DatApu

---

## Relacionamentos

Nenhum relacionamento cadastrado.
