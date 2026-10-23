# R049INT

## Descrição

Empréstimo Consignado - Integração

---

## Resumo

- Campos: 23
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| CodBan | Number(004,0) | Não | Código do Banco |
| SeqEmp | Number(002,0) | Não | Sequência do Empréstimo |
| TabEve | Number(003,0) | Sim | Código da Tabela de Eventos |
| EvePar | Number(004,0) | Sim | Evento para Integração da Parcela |
| EveBa1 | Number(004,0) | Sim | Evento para Valores do Banco |
| EveBa2 | Number(004,0) | Sim | Evento para Valores do Banco |
| EveBa3 | Number(004,0) | Sim | Evento para Valores do Banco |
| EveBa4 | Number(004,0) | Sim | Evento para Valores do Banco |
| EveBa5 | Number(004,0) | Sim | Evento para Valores do Banco |
| DesBa1 | String(001) | Sim | Forma de Desconto do Evento |
| DesBa2 | String(001) | Sim | Forma de Desconto do Evento |
| DesBa3 | String(001) | Sim | Forma de Desconto do Evento |
| DesBa4 | String(001) | Sim | Forma de Desconto do Evento |
| DesBa5 | String(001) | Sim | Forma de Desconto do Evento |
| EveEm1 | Number(004,0) | Sim | Evento para Valores da Empresa |
| EveEm2 | Number(004,0) | Sim | Evento para Valores da Empresa |
| DesEm1 | String(001) | Sim | Forma de Desconto do Evento |
| DesEm2 | String(001) | Sim | Forma de Desconto do Evento |
| TipEm1 | String(001) | Sim | Tipo do desconto sobre o evento da empresa |
| TipEm2 | String(001) | Sim | Tipo do desconto sobre o evento da empresa |
| ValEm1 | Number(011,2) | Sim | Valor do Desconto |
| ValEm2 | Number(011,2) | Sim | Valor do Desconto |

---

## Chave Primária

- NumEmp
- CodBan
- SeqEmp

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
