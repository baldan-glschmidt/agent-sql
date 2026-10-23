# R583RSP

## Descrição

GHE - Cadastro de PGR - Responsáveis LTCAT

---

## Resumo

- Campos: 4
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodPRA | Number(009,0) | Não | Código do Cadastro do PGR |
| DatIni | Date | Não | Data em que assumiu a responsabilidade |
| CodPes | Number(009,0) | Não | Código da Pessoa responsável pelo LTCAT |
| DatTer | Date | Sim | Data em que encerrou a responsabilidade |

---

## Chave Primária

- CodPRA
- DatIni
- CodPes

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R583RSP_000

**Tabela:** R583CAD

| Origem | Destino |
|--------|---------|
| CodPRA | CodPRA |

### IR_R583RSP_002

**Tabela:** R033PES

| Origem | Destino |
|--------|---------|
| CodPes | CodPes |

