# R583ICS

## Descrição

GHE - Revisão do GHE - Laudo - Indicativo comprometimento saúde

---

## Resumo

- Campos: 6
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 3

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodPRA | Number(009,0) | Não | Código do Cadastro do PGR |
| CodGHE | Number(009,0) | Não | Código do Cadastro do PGR |
| RevGHE | String(010) | Não | Código da Revisão do GHE |
| CodAGT | Number(006,0) | Não | Código do Perigo/Fator de Risco |
| SeqICS | Number(003,0) | Não | Sequência do indicativo de comprometimento de saúde |
| DesICS | String(500) | Sim | Descrição do indicativo de comprometimento de saúde |

---

## Chave Primária

- CodPRA
- CodGHE
- RevGHE
- CodAGT
- SeqICS

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R583ICS_000

**Tabela:** R583CAD

| Origem | Destino |
|--------|---------|
| CodPRA | CodPRA |

### IR_R583ICS_001

**Tabela:** R583GHE

| Origem | Destino |
|--------|---------|
| CodPRA | CodPRA |
| CodGHE | CodGHE |

### IR_R583ICS_002

**Tabela:** R583REV

| Origem | Destino |
|--------|---------|
| CodPRA | CodPRA |
| CodGHE | CodGHE |
| RevGHE | RevGHE |

