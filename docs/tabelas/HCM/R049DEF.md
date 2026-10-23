# R049DEF

## Descrição

Empréstimo Consignado - Definições

---

## Resumo

- Campos: 6
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| CodBan | Number(004,0) | Não | Código do Banco |
| PerEmp | Number(004,2) | Sim | Percentual Margem Consignado para Empréstimo |
| TetEmp | Number(011,2) | Sim | Teto da parcela para concessão do empréstimo |
| PerRes | Number(004,2) | Sim | Percentual de desconto do empréstimo sobre a Rescisão |
| RegCri | Number(003,0) | Sim | Regra para critérios do empréstimo |

---

## Chave Primária

- NumEmp
- CodBan

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R049DEF_001

**Tabela:** R012BAN

| Origem | Destino |
|--------|---------|
| CodBan | CodBan |

