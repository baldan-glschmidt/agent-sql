# R091AGC

## Descrição

Agendamento de Candidatos

---

## Resumo

- Campos: 5
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| DatAgc | Date | Não | Data de Agendamento de Candidato |
| HorAgc | Number(005,0) | Não | Hora de Agendamento de Candidato |
| NumCan | Number(007,0) | Não | Cadastro do Candidato |
| CanEli | String(001) | Sim | Candidato Eliminado |
| EmiCag | String(001) | Sim | Emitir Carta de Agradecimento |

---

## Chave Primária

- DatAgc
- HorAgc
- NumCan

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R091AGC_002

**Tabela:** R122CEX

| Origem | Destino |
|--------|---------|
| NumCan | NumCan |

