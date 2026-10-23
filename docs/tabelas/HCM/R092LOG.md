# R092LOG

## Descrição

Log de Rastreabilidade do Efetivo

---

## Resumo

- Campos: 11
- Chave Primária: 0 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Sim | Código da Empresa |
| CodPlv | Number(004,0) | Sim | Código do Plano de Vagas |
| EstPos | Number(003,0) | Sim | Código da Estrutura de Postos de Trabalho |
| PosTra | String(024) | Sim | Código do Posto de Trabalho |
| DatOpe | Date | Sim | Data que foi realizada a operação |
| DthAlt | Number(014,6) | Sim | Data e Hora do log |
| QtdLog | Number(004,0) | Sim | Quantidade Registrada no Log  do Efetivo |
| TipAlt | String(001) | Sim | Tipo da Alteração do Efetivo |
| TabAlt | Number(001,0) | Sim | Tabela de Alteração do Efetivo |
| TipOpe | Number(001,0) | Sim | Tipo da Operação do Efetivo |
| ObsLog | String(999) | Sim | Observação Registrada no Log do Efetivo |

---

## Chave Primária

Não possui.

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
