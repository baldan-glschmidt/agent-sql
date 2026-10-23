# R026INM

## Descrição

Previdência - Faixas Salário Família

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
| PerRef | Date | Não | Competência |
| CodFai | Number(002,0) | Não | Faixa Salário Família |
| LimFai | Number(011,2) | Sim | Limite da Faixa do Salário Família |
| ValFai | Number(011,2) | Sim | Valor do Salário Família desta Faixa |

---

## Chave Primária

- PerRef
- CodFai

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R026INM_000

**Tabela:** R026INS

| Origem | Destino |
|--------|---------|
| PerRef | PerRef |

