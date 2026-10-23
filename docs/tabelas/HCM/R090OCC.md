# R090OCC

## Descrição

Pessoas Comunicadas nas Ocorrências da Portaria

---

## Resumo

- Campos: 9
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodPlt | Number(005,0) | Não | Site da Ocorrência |
| DatOcP | Date | Não | Data da Ocorrência na Portaria |
| HorOcP | Number(005,0) | Não | Hora da Ocorrência na Portaria |
| SeqOcP | Number(002,0) | Não | Sequência da Ocorrência na Portaria |
| SeqCco | Number(002,0) | Não | Sequência do Comunicado na Ocorrência na Portaria |
| NumEmp | Number(004,0) | Sim | Código da Empresa do Responsável pela Ocorrência |
| TipCol | Number(001,0) | Sim | Tipo do Colaborador Responsável pela Ocorrência |
| NumCad | Number(009,0) | Sim | Cadastro do Colaborador Responsável pela Ocorrência |
| EccCco | String(254) | Sim | Endereço Cópia do E-mail para Comunicação à Terceiros |

---

## Chave Primária

- CodPlt
- DatOcP
- HorOcP
- SeqOcP
- SeqCco

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R090OCC_000

**Tabela:** R058PLT

| Origem | Destino |
|--------|---------|
| CodPlt | CodPlt |

