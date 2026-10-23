# R583FGL

## Descrição

GHE - Revisão do GHE - Fonte Geradora

---

## Resumo

- Campos: 7
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
| CodFgl | Number(006,0) | Não | Código da Fonte Geradora de Lesão |
| LocFgl | String(500) | Sim | Localização da Fonte Geradora |
| SitFgl | String(001) | Sim | Situação de Controle da Fonte Geradora |

---

## Chave Primária

- CodPRA
- CodGHE
- RevGHE
- CodAgt
- CodFgl

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R583FGL_003

**Tabela:** R583LAU

| Origem | Destino |
|--------|---------|
| CodPRA | CodPRA |
| CodGHE | CodGHE |
| RevGHE | RevGHE |
| CodAgt | CodAgt |

### IR_R583FGL_004

**Tabela:** R086FGL

| Origem | Destino |
|--------|---------|
| CodFgl | CodFgl |

