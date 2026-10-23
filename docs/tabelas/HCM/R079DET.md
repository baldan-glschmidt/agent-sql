# R079DET

## Descrição

Hab. Pessoais - Avaliação Detalhada

---

## Resumo

- Campos: 5
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodHpe | String(004) | Não | Código da Habilidade Pessoal |
| DatAlt | Date | Não | Data da Última Revisão da Avaliação Detalhada da Habilidade |
| CodHie | Number(003,0) | Não | Código da Hierarquia |
| TpAval | Number(001,0) | Não | Foco da Avaliação |
| CodAva | Number(004,0) | Sim | Código da avaliação detalhada |

---

## Chave Primária

- CodHpe
- DatAlt
- CodHie
- TpAval

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R079DET_000

**Tabela:** R079HPE

| Origem | Destino |
|--------|---------|
| CodHpe | CodHpe |

