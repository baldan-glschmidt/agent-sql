# R058CPR

## Descrição

Cobrança de Provisórios

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
| TabEve | Number(003,0) | Não | Código Tabela de Eventos |
| CodEve | Number(004,0) | Não | Código do Evento |
| DatAlt | Date | Não | Data de Alteração do Valor do Provisório |
| ValPrv | Number(012,3) | Sim | Valor do Crachá Provisório |

---

## Chave Primária

- TabEve
- CodEve
- DatAlt

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R058CPR_000

**Tabela:** R008EVM

| Origem | Destino |
|--------|---------|
| TabEve | CodTab |

### IR_R058CPR_001

**Tabela:** R008EVC

| Origem | Destino |
|--------|---------|
| TabEve | CodTab |
| CodEve | CodEve |

