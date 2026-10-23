# R178DTO

## Descrição

Def. Contas p/ Totais

---

## Resumo

- Campos: 5
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| FilCtb | Number(006,0) | Não | Código da Filial Matriz |
| TipCta | String(001) | Sim | Tipos de Contas (P,O) |
| OutEmp | Number(004,0) | Sim | Código da Outra Empresa |
| OutFil | Number(006,0) | Sim | Código da Outra Filial |

---

## Chave Primária

- NumEmp
- FilCtb

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R178DTO_000

**Tabela:** R030EMP

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |

