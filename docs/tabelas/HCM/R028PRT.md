# R028PRT

## Descrição

Precos Linhas Vale Transporte

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
| CodLin | Number(005,0) | Não | Código da Linha |
| DatPre | Date | Não | Data Competência dos Preços Vtr |
| ValKlm | Number(011,2) | Sim | Custo do Quilômetro |

---

## Chave Primária

- CodLin
- DatPre

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R028PRT_000

**Tabela:** R028LVT

| Origem | Destino |
|--------|---------|
| CodLin | CodLin |

