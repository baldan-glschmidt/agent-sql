# R108AUD

## Descrição

Histórico de situação do Exame

---

## Resumo

- Campos: 8
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 4

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Número da Empresa |
| CodFic | Number(009,0) | Não | Código Ficha Médica |
| CodExa | Number(004,0) | Não | Código do Exame |
| DatSol | Date | Não | Data Solicitação do Exame |
| DhrAlt | Number(014,6) | Não | Data/Hora da alteração da situação do exame |
| CodUsu | Number(010,0) | Sim | Código do Usuário |
| SitAnt | String(001) | Sim | Define a situação anterior do Exame |
| SitAtu | String(001) | Sim | Define a situação atual do Exame |

---

## Chave Primária

- NumEmp
- CodFic
- CodExa
- DatSol
- DhrAlt

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R108AUD_000

**Tabela:** R030EMP

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |

### IR_R108AUD_001

**Tabela:** R110FIC

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodFic | CodFic |

### IR_R108AUD_002

**Tabela:** R108EXA

| Origem | Destino |
|--------|---------|
| CodExa | CodExa |

### IR_R108AUD_003

**Tabela:** R108RES

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodFic | CodFic |
| CodExa | CodExa |
| DatSol | DatSol |

