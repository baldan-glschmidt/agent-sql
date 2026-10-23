# R010AAC

## Descrição

Abrangências de Ação de Acerto

---

## Resumo

- Campos: 3
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodAce | Number(003,0) | Não | Código da Ação de Acerto |
| CamRef | String(006) | Não | Campo de Referência para Abrangência |
| AbrCam | String(1000) | Sim | Abrangência do Campo |

---

## Chave Primária

- CodAce
- CamRef

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R010AAC_000

**Tabela:** R010ACE

| Origem | Destino |
|--------|---------|
| CodAce | CodAce |

