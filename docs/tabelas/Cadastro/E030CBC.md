# E030CBC

## Descrição

Tabelas - Bancos - Cidades atendidas

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
| CodBan | String(003) | Não | Código do banco na Febraban |
| CepCid | Number(008,0) | Não | Faixa inicial do CEP da cidade |
| DesCid | String(040) | Sim | Descrição da cidade atendida |

---

## Chave Primária

- CodBan
- CepCid

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E030CBC_000

**Tabela:** E030BAN

| Origem | Destino |
|--------|---------|
| CodBan | CodBan |

