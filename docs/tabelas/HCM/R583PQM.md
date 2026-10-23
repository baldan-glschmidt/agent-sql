# R583PQM

## Descrição

GHE - Revisão do GHE - Produto Químico

---

## Resumo

- Campos: 5
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodPRA | Number(009,0) | Não | Código do Cadastro do PGR |
| CodGHE | Number(009,0) | Não | Código do GHE - Grupo Homogêneo de Exposição |
| RevGHE | String(010) | Não | Código da Revisão do GHE |
| CodAgt | Number(006,0) | Não | Código do Perigo/Fator de Risco |
| CodPro | Number(006,0) | Não | Código do Produto Químico |

---

## Chave Primária

- CodPRA
- CodGHE
- RevGHE
- CodAgt
- CodPro

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R583PQM_002

**Tabela:** R583REV

| Origem | Destino |
|--------|---------|
| CodPRA | CodPRA |
| CodGHE | CodGHE |
| RevGHE | RevGHE |

### IR_R583PQM_004

**Tabela:** R082PRO

| Origem | Destino |
|--------|---------|
| CodPro | CodPro |

