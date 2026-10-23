# R126GHR

## Descrição

GHEs Requisição

---

## Resumo

- Campos: 3
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 3

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodRqu | Number(009,0) | Não | Código Requisição |
| CodPRA | Number(009,0) | Não | Código do Cadastro do PGR |
| CodGHE | Number(009,0) | Não | Código do GHE - Grupo Homogêneo de Exposição |

---

## Chave Primária

- CodRqu
- CodPRA
- CodGHE

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R126GHR_000

**Tabela:** R126RQU

| Origem | Destino |
|--------|---------|
| CodRqu | CodRqu |

### IR_R126GHR_001

**Tabela:** R583CAD

| Origem | Destino |
|--------|---------|
| CodPRA | CodPRA |

### IR_R126GHR_002

**Tabela:** R583GHE

| Origem | Destino |
|--------|---------|
| CodPRA | CodPRA |
| CodGHE | CodGHE |

