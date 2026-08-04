# E084DFX

## Descrição

Cadastros - Derivações da Faixa

---

## Resumo

- Campos: 4
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFxa | String(015) | Não | Código da faixa da grade |
| CodDer | String(007) | Não | Código da derivação da faixa |
| SeqCmd | Number(007,0) | Não | Ordenação seqüencial da derivação |

---

## Chave Primária

- CodEmp
- CodFxa
- CodDer

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E084DFX_001

**Tabela:** E084FXA

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodFxa | CodFxa |

