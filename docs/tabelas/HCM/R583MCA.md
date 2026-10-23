# R583MCA

## Descrição

GHE - Revisão do GHE - Laudo - Medidas de Controle

---

## Resumo

- Campos: 5
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodPRA | Number(009,0) | Não | Código do Cadastro do PGR |
| CodGHE | Number(009,0) | Não | Código do GHE - Grupo Homogêneo de Exposição |
| RevGHE | String(010) | Não | Código da Revisão do GHE |
| CodMed | Number(007,0) | Não | Código da Medida de Controle |
| CodAgt | Number(006,0) | Não | Código do Perigo/Fator de Risco |

---

## Chave Primária

- CodPRA
- CodGHE
- RevGHE
- CodAgt
- CodMed

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R583MCA_003

**Tabela:** R583MCR

| Origem | Destino |
|--------|---------|
| CodMed | CodMed |

