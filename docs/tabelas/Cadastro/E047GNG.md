# E047GNG

## Descrição

Tabelas - Naturezas de Gasto - Grupos

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
| CodEmp | Number(004,0) | Não | Código da Empresa |
| CodGng | Number(002,0) | Não | Cód. Grupo Naturezas de Gasto de Custos ou Despesas |
| DesGng | String(040) | Não | Descrição do Grupo de Naturezas de Gasto |
| ClaGng | String(001) | Não | Classificação do Grupo de Naturezas de Gasto |
| TaxCus | String(001) | Não | Indicativo se Compõe Taxa de Custos |
| NcpMax | Number(002,0) | Sim | Nível Máximo de Capacidade |

---

## Chave Primária

- CodEmp
- CodGng

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E047GNG_000

**Tabela:** E070EMP

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |

