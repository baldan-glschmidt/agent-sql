# R008HOM

## Descrição

Eventos - Código HomologNet

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
| CodTab | Number(003,0) | Não | Código da Tabela Eventos |
| CodEve | Number(004,0) | Não | Código do Evento |
| CodHom | Number(003,0) | Sim | Código HomologNet |

---

## Chave Primária

- CodTab
- CodEve

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R008HOM_001

**Tabela:** R008EVC

| Origem | Destino |
|--------|---------|
| CodTab | CodTab |
| CodEve | CodEve |

