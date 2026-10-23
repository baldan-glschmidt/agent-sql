# R028PRM

## Descrição

Precos Linhas Vale Transporte - Múltiplos

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
| CodLin | Number(005,0) | Não | Código da Linha |
| DatPre | Date | Não | Data Competência dos Preços Vtr |
| SeqMul | Number(002,0) | Não | Sequência do Múltiplo |
| ValPas | Number(012,3) | Sim | Valor Passe Múltiplo |
| OriPrm | String(001) | Sim | Origem Preço Linha VT |

---

## Chave Primária

- CodLin
- DatPre
- SeqMul

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R028PRM_001

**Tabela:** R028PRT

| Origem | Destino |
|--------|---------|
| CodLin | CodLin |
| DatPre | DatPre |

