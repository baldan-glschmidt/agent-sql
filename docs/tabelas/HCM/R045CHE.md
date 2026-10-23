# R045CHE

## Descrição

Cheques

---

## Resumo

- Campos: 9
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Codigo da Empresa do Empregado |
| SeqChe | Number(005,0) | Não | Seq |
| NumChe | Number(007,0) | Não | Número Sequencial do Cheque |
| DatFrs | Date | Sim | Data de Férias e Rescisão |
| TipCol | Number(001,0) | Sim | Tipo do Colaborador |
| NumCad | Number(009,0) | Sim | Numero do Cadastro |
| CodDep | Number(002,0) | Sim | Código do Dependente |
| ValChe | Number(011,2) | Sim | Valor do Cheque |
| CheImp | String(001) | Sim | Cheque Impresso |

---

## Chave Primária

- NumEmp
- SeqChe
- NumChe

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R045CHE_001

**Tabela:** R045SEQ

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| SeqChe | SeqChe |

