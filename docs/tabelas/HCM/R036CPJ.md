# R036CPJ

## Descrição

Contas Bancárias (Pensão Judicial)

---

## Resumo

- Campos: 12
- Chave Primária: 9 campo(s)
- Índices: 1
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo do Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do Empregado |
| CodDep | Number(002,0) | Não | Código do Dependente |
| DatAlt | Date | Não | Data de Alteração |
| SeqCon | Number(002,0) | Não | Sequência |
| CodBan | Number(004,0) | Não | Código do Banco |
| CodAge | Number(005,0) | Não | Código da Agência |
| TipBan | Number(001,0) | Sim | Tipo de Conta Bancária |
| ConBan | Number(012,0) | Não | Conta Bancária |
| DigBan | String(003) | Sim | Dígito Conta Banco |
| PerCon | Number(005,2) | Sim | Percentual Conta |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- CodDep
- DatAlt
- SeqCon
- CodBan
- CodAge
- ConBan

---

## Índices

### R036CPJIndice2

**Tipo:** Não unico

Campos:
- CodBan
- CodAge

---

## Relacionamentos

Nenhum relacionamento cadastrado.
