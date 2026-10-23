# R122CLA

## Descrição

Candidatos Externos - Laudos Psicólogo

---

## Resumo

- Campos: 7
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumCan | Number(007,0) | Não | Cadastro do Candidato |
| DatCla | Date | Não | Data do Laudo |
| NumEmp | Number(004,0) | Sim | Empresa |
| TipCol | Number(001,0) | Sim | Tipo do Psicólogo |
| NumCad | Number(009,0) | Sim | Cadastro do Psicólogo |
| ComCla | String(7000) | Sim | Laudo |
| NomArq | String(250) | Sim | Arquivo |

---

## Chave Primária

- NumCan
- DatCla

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R122CLA_000

**Tabela:** R122CEX

| Origem | Destino |
|--------|---------|
| NumCan | NumCan |

