# R201NPR

## Descrição

Tabela de Proficiência - Níveis - OBSOLETA

---

## Resumo

- Campos: 5
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodPro | Number(003,0) | Não | Código da Tabela de Proficiência |
| DatPro | Date | Não | Data da Tabela de Níveis de Proficiência |
| CodNiv | Number(004,0) | Não | Código do Nível da Proficiência |
| DesNiv | String(200) | Sim | Descrição do Nível da Proficiência |
| PerNiv | Number(007,4) | Sim | Define o percentual máximo do nível de proficiência |

---

## Chave Primária

- CodPro
- DatPro
- CodNiv

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R201NPR_000

**Tabela:** R201PRO

| Origem | Destino |
|--------|---------|
| CodPro | CodPro |

