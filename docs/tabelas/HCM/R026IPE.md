# R026IPE

## Descrição

Previdência - Faixas IPE

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
| PerRef | Date | Não | Competência |
| CodFai | Number(002,0) | Não | Faixa de Desconto do IPE |
| TetFai | Number(011,2) | Sim | Teto da Faixa do IPE |
| PerFai | Number(004,2) | Sim | Percentual de desconto da faixa do IPE |
| ForDes | Number(001,0) | Sim | Forma de Desconto |

---

## Chave Primária

- PerRef
- CodFai

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R026IPE_000

**Tabela:** R026INS

| Origem | Destino |
|--------|---------|
| PerRef | PerRef |

