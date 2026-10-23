# R583PDS

## Descrição

GHE - Revisão do GHE - Laudo - Possíveis Danos (Natureza lesões)

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
| CodNle | Number(003,0) | Não | Possível Dano à Saúde |

---

## Chave Primária

- CodPRA
- CodGHE
- RevGHE
- CodAgt
- CodNle

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R583PDS_003

**Tabela:** R583LAU

| Origem | Destino |
|--------|---------|
| CodPRA | CodPRA |
| CodGHE | CodGHE |
| RevGHE | RevGHE |
| CodAgt | CodAgt |

### IR_R583PDS_004

**Tabela:** R086NLE

| Origem | Destino |
|--------|---------|
| CodNle | CodNle |

