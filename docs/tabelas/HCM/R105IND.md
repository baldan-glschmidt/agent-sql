# R105IND

## Descrição

Cadastro de Avaliadores - Individual

---

## Resumo

- Campos: 15
- Chave Primária: 6 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do Colaborador Avaliado |
| DatIni | Date | Não | Data de início |
| TpAval | Number(001,0) | Não | Foco da Avaliação |
| SeqAvl | Number(005,0) | Não | Sequência do avaliador |
| DatFim | Date | Sim | Data de término |
| EmpAvl | Number(004,0) | Sim | Empresa do avaliador |
| TipAvl | Number(001,0) | Sim | Tipo do Colaborador Avaliador |
| CadAvl | Number(009,0) | Sim | Cadastro do Avaliador |
| DefMut | String(001) | Sim | Na avaliação oposta o avaliador assume o papel de avaliado |
| CodUsu | Number(010,0) | Sim | Usuário responsável pela última alteração do registro |
| DthAlt | Number(014,6) | Sim | Data/Hora da última alteração do registro |
| SitCad | Number(001,0) | Sim | Define se o cadastro de avaliadores individual é válido |
| CodCic | Number(003,0) | Sim | Código do ciclo de avaliação |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- DatIni
- TpAval
- SeqAvl

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
