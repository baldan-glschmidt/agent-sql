# R122CSE

## Descrição

Candidatos Externos - Parecer Selecionador

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
| NumCan | Number(007,0) | Não | Cadastro Candidato |
| DatCpa | Date | Não | Data Parecer Candidato |
| EmpCse | Number(004,0) | Sim | Empresa Selecionador |
| OriCse | Number(001,0) | Sim | Tipo de Selecionador |
| NumCse | Number(009,0) | Sim | Cadastro Selecionador |
| CodPse | Number(003,0) | Sim | Código Parecer Selecionador |
| ComPse | String(2000) | Sim | Comentário Parecer Selecionador |

---

## Chave Primária

- NumCan
- DatCpa

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R122CSE_000

**Tabela:** R122CEX

| Origem | Destino |
|--------|---------|
| NumCan | NumCan |

