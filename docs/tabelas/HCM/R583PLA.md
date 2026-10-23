# R583PLA

## Descrição

GHE - Revisão do GHE - Planos de Ação

---

## Resumo

- Campos: 7
- Chave Primária: 6 campo(s)
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
| NumEmp | Number(004,0) | Não | Código da Empresa do Plano de Ação |
| CodPln | Number(009,0) | Não | Código do Plano de Ação |
| CodFgl | Number(006,0) | Sim | Código da Fonte Geradora do Risco (Obsoleto) |

---

## Chave Primária

- CodPRA
- CodGHE
- RevGHE
- CodAgt
- NumEmp
- CodPln

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R583PLA_002

**Tabela:** R583REV

| Origem | Destino |
|--------|---------|
| CodPRA | CodPRA |
| CodGHE | CodGHE |
| RevGHE | RevGHE |

### IR_R583PLA_005

**Tabela:** R084PLN

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodPln | CodPln |

