# R010SAC

## Descrição

Situações para Ações de Acerto

---

## Resumo

- Campos: 3
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodAce | Number(003,0) | Não | Código da Ação de Acerto |
| CodSit | Number(003,0) | Não | Código da Situação |
| SitAlt | Number(003,0) | Sim | Código da Situação Alterada |

---

## Chave Primária

- CodAce
- CodSit

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R010SAC_000

**Tabela:** R010ACE

| Origem | Destino |
|--------|---------|
| CodAce | CodAce |

### IR_R010SAC_001

**Tabela:** R010SIT

| Origem | Destino |
|--------|---------|
| CodSit | CodSit |

