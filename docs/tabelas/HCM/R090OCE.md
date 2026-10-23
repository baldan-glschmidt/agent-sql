# R090OCE

## Descrição

Colaboradores Envolvidos nas Ocorrências da Portaria

---

## Resumo

- Campos: 8
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodPlt | Number(005,0) | Não | Planta da Ocorrência |
| DatOcP | Date | Não | Data da Ocorrência na Portaria |
| HorOcP | Number(005,0) | Não | Hora da Ocorrência na Portaria |
| SeqOcP | Number(002,0) | Não | Sequência da Ocorrência na Portaria |
| SeqEnv | Number(002,0) | Não | Sequência do Envolvido na Ocorrência na Portaria |
| NumEmp | Number(004,0) | Sim | Código da Empresa do Responsável pela Ocorrência |
| TipCol | Number(001,0) | Sim | Tipo do Colaborador Responsável pela Ocorrência |
| NumCad | Number(009,0) | Sim | Cadastro do Colaborador Responsável pela Ocorrência |

---

## Chave Primária

- CodPlt
- DatOcP
- HorOcP
- SeqOcP
- SeqEnv

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R090OCE_000

**Tabela:** R058PLT

| Origem | Destino |
|--------|---------|
| CodPlt | CodPlt |

