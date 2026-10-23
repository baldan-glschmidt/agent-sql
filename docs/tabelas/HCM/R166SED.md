# R166SED

## Descrição

Seguros - Definições das Faixas

---

## Resumo

- Campos: 6
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodSeg | Number(003,0) | Não | Código do Seguro |
| PerRef | Date | Não | Competência de Definição das Faixas |
| ForFai | String(001) | Sim | Formação da Faixa |
| ForRef | String(001) | Sim | Formação da Referência |
| TetMax | Number(011,2) | Sim | Teto Máximo do Seguro |
| TetMin | Number(011,2) | Sim | Teto Mínimo do Seguro |

---

## Chave Primária

- CodSeg
- PerRef

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R166SED_000

**Tabela:** R166SEG

| Origem | Destino |
|--------|---------|
| CodSeg | CodSeg |

