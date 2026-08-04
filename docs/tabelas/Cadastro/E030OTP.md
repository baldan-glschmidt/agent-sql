# E030OTP

## Descrição

Tabelas - Bancos - Tipos de Pagamentos

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
| TipPgt | String(002) | Não | Tipo de Pagamento do título |
| PgtBan | String(003) | Não | Tipo de pagamento no banco |
| DesPgt | String(040) | Sim | Descrição do tipo de pagamento no banco |
| UtiCba | String(001) | Sim | Tipo de pagamento utiliza código de barras para pagamento eletrônico |

---

## Chave Primária

- CodBan
- TipPgt
- PgtBan

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E030OTP_000

**Tabela:** E030BAN

| Origem | Destino |
|--------|---------|
| CodBan | CodBan |

