# E035OCV

## Descrição

Tabelas - Ocorrências Internas de Retorno - Empresa

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
| CodOct | String(003) | Não | Código interno da ocorrência bancária de retorno |
| CodEmp | Number(004,0) | Não | Código da empresa |
| TpgOct | String(005) | Sim | Código da transação de baixa por pagamento |
| TcbOct | String(005) | Sim | Código da transação para caixa e bancos |

---

## Chave Primária

- CodOct
- CodEmp

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E035OCV_000

**Tabela:** E035OCT

| Origem | Destino |
|--------|---------|
| CodOct | CodOct |

