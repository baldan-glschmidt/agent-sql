# R999GUI

## Descrição

Itens de grupos de modelos

---

## Resumo

- Campos: 6
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| SysGrp | String(002) | Não | Sist. grupo |
| CodGrp | Number(003,0) | Não | Código do grupo |
| NomMod | String(015) | Não | Nome do modelo |
| DesMod | String(150) | Sim | Descrição do modelo |
| OrdGrp | Number(002,0) | Sim | Ordem do item |
| QtdVia | Number(003,0) | Sim | Quantidade de vias |

---

## Chave Primária

- SysGrp
- CodGrp
- NomMod

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R999GUI_001

**Tabela:** R999GUC

| Origem | Destino |
|--------|---------|
| SysGrp | SysGrp |
| CodGrp | CodGrp |

