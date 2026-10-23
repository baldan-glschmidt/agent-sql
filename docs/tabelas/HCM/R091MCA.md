# R091MCA

## Descrição

Movimento Entrada/Saída de Candidatos

---

## Resumo

- Campos: 12
- Chave Primária: 3 campo(s)
- Índices: 1
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| DatEnt | Date | Não | Data de Entrada |
| HorEnt | Number(005,0) | Não | Hora de Entrada |
| NumCan | Number(007,0) | Não | Cadastro do Candidato |
| CodAce | Number(003,0) | Sim | Código do Acesso do Candidato |
| DatAut | Date | Sim | Data da Autorização do Acesso |
| HorAut | Number(005,0) | Sim | Hora da Autorização de Acesso |
| NumCra | Number(012,0) | Sim | Código do Crachá |
| CodPrm | Number(005,0) | Sim | Código Permissão de Acesso |
| DatVal | Date | Sim | Data de Validade de Acesso |
| HorVal | Number(005,0) | Sim | Hora de Validade de Acesso |
| DatSai | Date | Sim | Data da Saída da Empresa |
| HorSai | Number(005,0) | Sim | Hora da Saída da Empresa |

---

## Chave Primária

- DatEnt
- HorEnt
- NumCan

---

## Índices

### R091MCAIndice2

**Tipo:** Não unico

Campos:
- NumCra
- DatEnt
- HorEnt

---

## Relacionamentos

### IR_R091MCA_002

**Tabela:** R122CEX

| Origem | Destino |
|--------|---------|
| NumCan | NumCan |

### IR_R091MCA_003

**Tabela:** R091MAC

| Origem | Destino |
|--------|---------|
| CodAce | CodAce |

