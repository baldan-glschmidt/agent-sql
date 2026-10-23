# R122CTI

## Descrição

Candidatos Externos - Times Pretendidos - OBSOLETA

---

## Resumo

- Campos: 2
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumCan | Number(007,0) | Não | Cadastro Candidato |
| CodTim | String(008) | Não | Código do Time |

---

## Chave Primária

- NumCan
- CodTim

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R122CTI_000

**Tabela:** R122CEX

| Origem | Destino |
|--------|---------|
| NumCan | NumCan |

### IR_R122CTI_001

**Tabela:** R078TIM

| Origem | Destino |
|--------|---------|
| CodTim | CodTim |

