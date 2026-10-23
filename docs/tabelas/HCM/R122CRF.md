# R122CRF

## Descrição

Candidatos Externos - Referências

---

## Resumo

- Campos: 7
- Chave Primária: 2 campo(s)
- Índices: 1
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumCan | Number(007,0) | Não | Cadastro Candidato |
| SeqRef | Number(002,0) | Não | Sequência do Registro |
| NomRef | String(030) | Sim | Nome da Referência |
| NumTel | String(020) | Sim | Número do Telefone |
| CodRlc | Number(003,0) | Sim | Tipo de Referência |
| DddTel | Number(003,0) | Sim | Código DDD do telefone |
| DdiTel | Number(003,0) | Sim | Código DDI do telefone |

---

## Chave Primária

- NumCan
- SeqRef

---

## Índices

### R122CRFIndice2

**Tipo:** Não unico

Campos:
- NumCan
- CodRlc

---

## Relacionamentos

### IR_R122CRF_000

**Tabela:** R122CEX

| Origem | Destino |
|--------|---------|
| NumCan | NumCan |

### IR_R122CRF_004

**Tabela:** R114RLC

| Origem | Destino |
|--------|---------|
| CodRlc | CodRlc |

