# R038NOT

## Descrição

Anotações da Ficha Registro

---

## Resumo

- Campos: 13
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro Empregado |
| DatNot | Date | Não | Data Anotação Registro |
| SeqNot | Number(002,0) | Não | Sequência |
| TipNot | Number(003,0) | Sim | Tipo da anotação |
| NroDoc | String(020) | Sim | Número do documento |
| NotFic | String(2500) | Sim | Descrição da Anotação da Ficha |
| EmpDig | Number(004,0) | Sim | Código da Empresa Responsável |
| TipDig | Number(001,0) | Sim | Tipo Responsável |
| CadDig | Number(009,0) | Sim | Responsável Anotação |
| OriInf | String(001) | Sim | Origem da informação |
| CodTce | Number(004,0) | Sim | Código do treinamento na tabela do eSocial |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- DatNot
- SeqNot

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R038NOT_002

**Tabela:** R034FUN

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |

