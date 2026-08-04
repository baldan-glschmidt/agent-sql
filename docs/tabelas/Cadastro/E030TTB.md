# E030TTB

## Descrição

Tabelas - Bancos - Tipos de Tributos

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
| CodBan | String(003) | Não | Código do banco na Febraban |
| TipImp | Number(002,0) | Não | Tipo de Imposto do título |
| TipGui | Number(002,0) | Sim | Tipo de Guia para emissão do Título |
| TriBan | String(002) | Não | Tipo de Tributo no banco |
| DesTri | String(040) | Sim | Descrição do tipo de tributo no banco |

---

## Chave Primária

- CodBan
- TipImp
- TriBan

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E030TTB_000

**Tabela:** E030BAN

| Origem | Destino |
|--------|---------|
| CodBan | CodBan |

