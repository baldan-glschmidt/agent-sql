# R008TCL

## Descrição

Eventos - Tipos de Colaborador Inválidos

---

## Resumo

- Campos: 3
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodTab | Number(003,0) | Não | Código da Tabela de Eventos |
| CodEve | Number(004,0) | Não | Código do Evento |
| TipCol | Number(001,0) | Não | Tipo Colaborador Inválido p/ o Evento |

---

## Chave Primária

- CodTab
- CodEve
- TipCol

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R008TCL_001

**Tabela:** R008EVC

| Origem | Destino |
|--------|---------|
| CodTab | CodTab |
| CodEve | CodEve |

