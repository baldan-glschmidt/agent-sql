# R091AUT

## Descrição

Autorização de Acesso Candidatos

---

## Resumo

- Campos: 8
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| DatAut | Date | Não | Data da Autorização do Acesso |
| HorAut | Number(005,0) | Não | Hora da Autorização de Acesso |
| NumCan | Number(007,0) | Não | Cadastro do Candidato |
| CodAce | Number(003,0) | Não | Código do Acesso do Candidato |
| DatAgc | Date | Sim | Data de Agendamento de Candidato |
| HorAgc | Number(005,0) | Sim | Hora de Agendamento de Candidato |
| TabOrg | Number(004,0) | Sim | Código da Tabela de Organograma do Local |
| NumLoc | Number(009,0) | Sim | Local do Organograma |

---

## Chave Primária

- DatAut
- HorAut
- NumCan
- CodAce

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R091AUT_002

**Tabela:** R122CEX

| Origem | Destino |
|--------|---------|
| NumCan | NumCan |

### IR_R091AUT_003

**Tabela:** R091MAC

| Origem | Destino |
|--------|---------|
| CodAce | CodAce |

