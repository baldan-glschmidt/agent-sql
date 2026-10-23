# R583RCP

## Descrição

GHE - Cadastro de PGR - Revisão

---

## Resumo

- Campos: 5
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodPRA | Number(009,0) | Não | Código do Cadastro do PGR |
| RevPRA | String(010) | Não | Código da Revisão do Cadastro de PGR |
| DesRev | String(060) | Sim | Descrição de referência da revisão do Cadastro de PGR |
| DatIni | Date | Sim | Data de início da revisão do PGR |
| DatTer | Date | Sim | Data de término da revisão do PGR |

---

## Chave Primária

- CodPRA
- RevPRA

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R583RCP_000

**Tabela:** R583CAD

| Origem | Destino |
|--------|---------|
| CodPRA | CodPRA |

