# R057DEV

## Descrição

Tabela de Devedores de Benefícios

---

## Resumo

- Campos: 14
- Chave Primária: 6 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro Colaborador |
| DatMar | Date | Não | Data da Marcação |
| HorMar | Number(005,0) | Não | Hora da Marcação |
| SeqMar | Number(002,0) | Não | Sequência do Registro |
| NumCra | Number(012,0) | Sim | Número do Crachá |
| CodPlt | Number(005,0) | Sim | Código do Site |
| CodRlg | Number(005,0) | Sim | Código do Coletor no Acesso |
| CodBnf | Number(002,0) | Sim | Código do Benefício |
| NomLis | String(008) | Sim | Nome da Lista de Benefícios |
| MotDeb | Number(001,0) | Sim | Motivo do Crachá na Lista de Devedores |
| DatCon | Date | Sim | Data do Consumo do Benefício |
| HorCon | Number(005,0) | Sim | Hora do Consumo do Benefício |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- DatMar
- HorMar
- SeqMar

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
