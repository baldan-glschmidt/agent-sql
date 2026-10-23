# R583ATV

## Descrição

GHE - Revisão do GHE - Atividade de Risco

---

## Resumo

- Campos: 4
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodPRA | Number(009,0) | Não | Código do Cadastro do PGR |
| CodGHE | Number(009,0) | Não | Código do GHE - Grupo Homogêneo de Exposição |
| RevGHE | String(010) | Não | Código da Revisão do GHE |
| CodApi | Number(005,0) | Não | Código da atividade perigosa, insalubre e/ou especial do eSocial |

---

## Chave Primária

- CodPRA
- CodGHE
- RevGHE
- CodApi

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R583ATV_002

**Tabela:** R583REV

| Origem | Destino |
|--------|---------|
| CodPRA | CodPRA |
| CodGHE | CodGHE |
| RevGHE | RevGHE |

