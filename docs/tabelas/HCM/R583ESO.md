# R583ESO

## Descrição

GHE - Cadastro de PGR - eSocial

---

## Resumo

- Campos: 4
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodPRA | Number(009,0) | Não | Código do Cadastro do PGR |
| DatAlt | Date | Não | Data de Alteração |
| MetErg | String(999) | Sim | Descrição da metodologia utilizada para o levantamento dos riscos ergonômicos. |
| ObsCom | String(999) | Sim | Observação(ões) complementar(es) referente(s) a registros ambientais. |

---

## Chave Primária

- CodPRA
- DatAlt

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R583ESO_000

**Tabela:** R583CAD

| Origem | Destino |
|--------|---------|
| CodPRA | CodPRA |

