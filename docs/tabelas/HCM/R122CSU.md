# R122CSU

## Descrição

Candidatos Externos - Parecer Superior

---

## Resumo

- Campos: 8
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumCan | Number(007,0) | Não | Cadastro Candidato |
| DatCpa | Date | Não | Data Parecer Candidato |
| SeqCsu | Number(002,0) | Não | Sequência de entrevistas |
| EmpCsu | Number(004,0) | Sim | Empresa Superior |
| OriCsu | Number(001,0) | Sim | Tipo de Superior |
| NumCsu | Number(009,0) | Sim | Cadastro de Superior |
| CodPsu | Number(003,0) | Sim | Código Parecer Superior |
| ComPsu | String(2000) | Sim | Comentário Parecer Superior |

---

## Chave Primária

- NumCan
- DatCpa
- SeqCsu

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R122CSU_000

**Tabela:** R122CEX

| Origem | Destino |
|--------|---------|
| NumCan | NumCan |

