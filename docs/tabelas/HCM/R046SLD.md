# R046SLD

## Descrição

Saldos Provisões - Transferência

---

## Resumo

- Campos: 19
- Chave Primária: 8 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do colaborador |
| MesAno | Date | Não | Competência Provisões |
| FilCtb | Number(006,0) | Não | Filial Contábil |
| TabOrg | Number(003,0) | Não | Código da Tabela de Organograma |
| NumLoc | Number(009,0) | Não | Local do Organograma |
| CodCcu | String(018) | Não | Código Centro Custo Contábil |
| SldTrf | Number(011,2) | Sim | Saldo Prv Férias - Transferência |
| AdiTrf | Number(011,2) | Sim | Saldo Prv Adicional 1/3 Férias - Transferência |
| InsTrf | Number(011,2) | Sim | Saldo Prv Inss Férias - Transferência |
| FgtTrf | Number(011,2) | Sim | Saldo Prv FGTS Prv Férias - Transferência |
| PisTrf | Number(011,2) | Sim | Saldo Prv Pis Férias - Transferência |
| Sld13T | Number(011,2) | Sim | Saldo Prv 13° Salário - Transferência |
| Ins13T | Number(011,2) | Sim | Saldo Prv INSS 13° Salário - Transferência |
| Fgt13T | Number(011,2) | Sim | Saldo Prv FGTS 13° Salário - Transferência |
| Pis13T | Number(011,2) | Sim | Saldo Prv Pis 13° Salário - Transferência |
| TipTrf | Number(001,0) | Sim | Tipo da transferência |
| Adt13s | Number(011,2) | Sim | 13° Salário Adto. do Mês |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- MesAno
- FilCtb
- NumLoc
- CodCcu
- TabOrg

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
