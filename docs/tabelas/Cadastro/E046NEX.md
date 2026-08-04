# E046NEX

## Descrição

Notas Explicativas - Notas

---

## Resumo

- Campos: 8
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| GruNex | String(030) | Não | Grupo de notas explicativas |
| SeqNex | Number(007,0) | Não | Sequência do grupo de notas explicativas |
| CodNex | String(025) | Não | Código da nota explicativa |
| ClaNex | String(025) | Sim | Classificação da nota explicativa |
| NivNex | Number(002,0) | Sim | Nível da nota explicativa |
| TitNex | String(250) | Sim | Título da nota explicativa |
| TxtNex | String(9998) | Sim | Texto contendo os detalhes da nota explicativa |

---

## Chave Primária

- CodEmp
- GruNex
- SeqNex

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E046NEX_000

**Tabela:** E070EMP

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |

### IR_E046NEX_001

**Tabela:** E046GNE

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| GruNex | GruNex |

