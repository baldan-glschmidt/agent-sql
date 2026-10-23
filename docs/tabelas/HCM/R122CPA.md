# R122CPA

## Descrição

Candidatos Externos - Parecer Psicólogo

---

## Resumo

- Campos: 17
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumCan | Number(007,0) | Não | Cadastro Candidato |
| DatCpa | Date | Não | Data Parecer Candidato |
| EmpCsi | Number(004,0) | Sim | Empresa Psicólogo |
| OriCsi | Number(001,0) | Sim | Tipo de Psicólogo |
| NumCsi | Number(009,0) | Sim | Cadastro do Psicólogo |
| CodPsi | Number(003,0) | Sim | Código Parecer Psicólogo |
| ComPsi | String(7000) | Sim | Comentário Psicólogo |
| EmpCse | Number(004,0) | Sim | Empresa Selecionador |
| OriCse | Number(001,0) | Sim | Tipo de Selecionador |
| NumCse | Number(009,0) | Sim | Cadastro Selecionador |
| CodPse | Number(003,0) | Sim | Código Parecer Selecionador |
| ComPse | String(2000) | Sim | Comentário Parecer Selecionador |
| EmpCsu | Number(004,0) | Sim | Empresa Superior |
| OriCsu | Number(001,0) | Sim | Tipo de Superior |
| NumCsu | Number(009,0) | Sim | Cadastro de Superior |
| CodPsu | Number(003,0) | Sim | Código Parecer Superior |
| ComPsu | String(2000) | Sim | Comentário Parecer Superior |

---

## Chave Primária

- NumCan
- DatCpa

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R122CPA_000

**Tabela:** R122CEX

| Origem | Destino |
|--------|---------|
| NumCan | NumCan |

