# R583IRO

## Descrição

GHE - Revisão do GHE - Laudo - Inventário de Riscos Ocupacionais

---

## Resumo

- Campos: 12
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
| CodAgt | Number(006,0) | Não | Código do Perigo/Fator de Risco |
| CodRis | Number(002,0) | Não | Código do risco ocupacional gerado pelo perigo/fator de risco |
| DesRis | String(080) | Sim | Descrição do risco ocupacional gerado pelo perigo/fator de risco |
| MatRis | Number(006,0) | Sim | Técnica utilizada para realizar a avaliação do risco |
| NivPro | Number(001,0) | Sim | Nível de probabilidade do risco |
| NivSev | Number(001,0) | Sim | Nível de severidade do risco |
| NivCla | Number(001,0) | Sim | Nível da classificação do risco |
| ClaRis | String(250) | Sim | Comentários sobre a classificação do risco |
| ValRes | Number(004,0) | Sim | Valor do resultado (Probabilidade x Severidade) |

---

## Chave Primária

- CodPRA
- CodGHE
- RevGHE
- CodAgt
- CodRis

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R583IRO_000

**Tabela:** R583CAD

| Origem | Destino |
|--------|---------|
| CodPRA | CodPRA |

### IR_R583IRO_001

**Tabela:** R583GHE

| Origem | Destino |
|--------|---------|
| CodPRA | CodPRA |
| CodGHE | CodGHE |

### IR_R583IRO_002

**Tabela:** R583REV

| Origem | Destino |
|--------|---------|
| CodPRA | CodPRA |
| CodGHE | CodGHE |
| RevGHE | RevGHE |

