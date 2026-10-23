# R009ASO

## Descrição

Assinatura Espelho de Ponto - Solicitação

---

## Resumo

- Campos: 11
- Chave Primária: 1 campo(s)
- Índices: 1
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| ProSol | String(040) | Não | Protocolo Solicitação |
| NumEmp | Number(004,0) | Sim | Empresa do colaborador |
| TipCol | Number(001,0) | Sim | Tipo do colaborador |
| NumCad | Number(009,0) | Sim | Cadastro do colaborador |
| DatCmp | Date | Sim | Competência |
| DatSol | Date | Sim | Data Solicitação Assinatura Cartão Ponto |
| MilSol | Number(005,0) | Sim | Data Sol. Millisegundos |
| DatExp | Date | Sim | Data Expiração da Solicitação |
| SolAti | String(001) | Sim | Solicitação Ativa |
| StaSol | Number(003,0) | Sim | Status Solicitação |
| CodUsu | Number(009,0) | Sim | Código do Usuário Solicitante |

---

## Chave Primária

- ProSol

---

## Índices

### R009ASOindice2

**Tipo:** Não unico

Campos:
- NumEmp
- TipCol
- NumCad
- DatCmp

---

## Relacionamentos

Nenhum relacionamento cadastrado.
