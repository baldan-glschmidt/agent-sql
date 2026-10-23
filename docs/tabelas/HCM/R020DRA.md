# R020DRA

## Descrição

Definições do Rateio

---

## Resumo

- Campos: 5
- Chave Primária: 1 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| RatDsl | String(001) | Sim | Rateio no Deslocamento |
| DslTra | String(001) | Sim | Deslocamento no Trabalho |
| DslExt | String(001) | Sim | Deslocamento nas Extras |
| SitDsl | Number(003,0) | Sim | Código Situação Deslocamento |

---

## Chave Primária

- NumEmp

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R020DRA_000

**Tabela:** R030EMP

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |

