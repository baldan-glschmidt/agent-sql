# R126RSV

## Descrição

Solicitação de abertura de vaga - Roteiro de aprovação

---

## Resumo

- Campos: 8
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodSVa | Number(009,0) | Não | Código da solicitação de vaga |
| SeqRSV | Number(003,0) | Não | Sequência de aprovação |
| NumEmp | Number(004,0) | Sim | Empresa Requisitante |
| TipCol | Number(001,0) | Sim | Tipo de Colaborador |
| NumCad | Number(009,0) | Sim | Cadastro Colaborador |
| EstPos | Number(003,0) | Sim | Código da estrutura de postos de trabalho |
| PosTra | String(024) | Sim | Posto de Trabalho em que o Colaborador atua |
| SitRSV | Number(001,0) | Sim | Situação do passo do roteiro de aprovação |

---

## Chave Primária

- CodSVa
- SeqRSV

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R126RSV_000

**Tabela:** R126SVA

| Origem | Destino |
|--------|---------|
| CodSVa | CodSVa |

