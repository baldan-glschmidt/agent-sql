# R114CPA

## Descrição

Pastas de Candidatos - Candidatos internos e externos

---

## Resumo

- Campos: 6
- Chave Primária: 6 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodPac | Number(004,0) | Não | Código da Pastas de Candidatos |
| OriCan | Number(001,0) | Não | Origem do Candidato (I-Interno, E-Externo) |
| NumCan | Number(007,0) | Não | Cadastro do Candidato |
| NumEmp | Number(004,0) | Não | Empresa |
| TipCol | Number(001,0) | Não | Tipo do Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do Colaborador |

---

## Chave Primária

- CodPac
- OriCan
- NumCan
- NumEmp
- TipCol
- NumCad

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R114CPA_000

**Tabela:** R114PAC

| Origem | Destino |
|--------|---------|
| CodPac | CodPac |

