# R126GHS

## Descrição

GHEs Solicitação de vagas

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
| CodSVa | Number(009,0) | Não | Código da solicitação de vaga |
| CodPRA | Number(009,0) | Não | Código do Cadastro do PGR |
| CodGHE | Number(009,0) | Não | Código do GHE - Grupo Homogêneo de Exposição |

---

## Chave Primária

- CodSVa
- CodPRA
- CodGHE

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R126GHS_000

**Tabela:** R126SVA

| Origem | Destino |
|--------|---------|
| CodSVa | CodSVa |

### IR_R126GHS_001

**Tabela:** R583CAD

| Origem | Destino |
|--------|---------|
| CodPRA | CodPRA |

### IR_R126GHS_002

**Tabela:** R583GHE

| Origem | Destino |
|--------|---------|
| CodPRA | CodPRA |
| CodGHE | CodGHE |

