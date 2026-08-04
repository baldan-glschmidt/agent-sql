# E030TBE

## Descrição

Tabelas - Tarifas Bancárias - Empresa

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
| CodTrb | String(003) | Não | Código interno da tarifa bancária |
| CodEmp | Number(004,0) | Não | Código da empresa |
| TcbTrb | String(005) | Sim | Código da transação de débito para caixa e bancos |

---

## Chave Primária

- CodTrb
- CodEmp

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E030TBE_000

**Tabela:** E030TRB

| Origem | Destino |
|--------|---------|
| CodTrb | CodTrb |

