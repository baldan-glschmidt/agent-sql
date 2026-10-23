# R038AVA

## Descrição

Anotações para Avaliação

---

## Resumo

- Campos: 11
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da empresa do avaliado |
| TipCol | Number(001,0) | Não | Tipo do colaborador avaliado |
| NumCad | Number(009,0) | Não | Cadastro empregado avaliado |
| DatAno | Date | Não | Data da anotação |
| SeqAno | Number(002,0) | Não | Sequência da anotação |
| EmpAvl | Number(004,0) | Sim | Empresa do avaliador |
| TipAvl | Number(001,0) | Sim | Tipo do colaborador avaliador |
| CadAvl | Number(009,0) | Sim | Cadastro do avaliador |
| DefPer | Number(001,0) | Sim | Define permissão de acesso ao registro |
| DesAno | String(10000) | Sim | Descrição da anotação |
| TipAno | Number(001,0) | Sim | Tipo de anotação |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- DatAno
- SeqAno

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
