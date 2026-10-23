# R166SEF

## Descrição

Seguros - Faixas p/ competência

---

## Resumo

- Campos: 5
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodSeg | Number(003,0) | Não | Código do seguro |
| PerRef | Date | Não | Competência |
| CodFai | Number(002,0) | Não | Faixa de Desconto do Seguro |
| ValLim | Number(011,2) | Sim | Valor limite da faixa |
| RefFai | Number(013,5) | Sim | Referência da faixa |

---

## Chave Primária

- CodSeg
- PerRef
- CodFai

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R166SEF_001

**Tabela:** R166SED

| Origem | Destino |
|--------|---------|
| CodSeg | CodSeg |
| PerRef | PerRef |

