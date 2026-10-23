# R082RIS

## Descrição

Agente - Riscos Ocupacionais

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
| CodAgt | Number(006,0) | Não | Código do Perigo/Fator de Risco |
| SeqRis | Number(002,0) | Não | Sequência do risco |
| DesRis | String(080) | Sim | Descrição do Risco Ocupacional |

---

## Chave Primária

- CodAgt
- SeqRis

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R082RIS_000

**Tabela:** R082AGT

| Origem | Destino |
|--------|---------|
| CodAgt | CodAgt |

