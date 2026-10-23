# R008CSA

## Descrição

Saldos de Eventos

---

## Resumo

- Campos: 4
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodTab | Number(003,0) | Não | Código da Tabela Eventos |
| CodSal | Number(004,0) | Não | Código do Saldo |
| DesSal | String(020) | Sim | Descrição do Saldo |
| MesFec | Number(002,0) | Sim | Mês de Fechamento do Saldo |

---

## Chave Primária

- CodTab
- CodSal

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R008CSA_000

**Tabela:** R008EVM

| Origem | Destino |
|--------|---------|
| CodTab | CodTab |

