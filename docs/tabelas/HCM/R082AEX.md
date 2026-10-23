# R082AEX

## Descrição

Exames por  Agente - Sugestão

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
| CodAgt | Number(006,0) | Não | Código do Perigo/Fator de Risco |
| CodExa | Number(004,0) | Não | Código Exame |

---

## Chave Primária

- CodAgt
- CodExa

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R082AEX_000

**Tabela:** R082AGT

| Origem | Destino |
|--------|---------|
| CodAgt | CodAgt |

### IR_R082AEX_001

**Tabela:** R108EXA

| Origem | Destino |
|--------|---------|
| CodExa | CodExa |

