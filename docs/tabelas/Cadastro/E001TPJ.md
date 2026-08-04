# E001TPJ

## Descrição

Tabelas - Transações - Projetos

---

## Resumo

- Campos: 3
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodTns | String(005) | Não | Código da transação |
| RecLct | String(001) | Sim | Indicativo se o lançamento manual reconhece receita (IFRS/POC) |

---

## Chave Primária

- CodEmp
- CodTns

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E001TPJ_001

**Tabela:** E001TNS

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodTns | CodTns |

