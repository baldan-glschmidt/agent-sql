# E077BAN

## Descrição

Cadastros - Favorecidos - Contas Bancárias

---

## Resumo

- Campos: 11
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodFav | Number(014,0) | Sim | Número do CNPJ ou CPF do favorecido |
| DocIdeFav | String(014) | Sim | Número do CNPJ ou CPF do favorecido |
| SeqBan | Number(004,0) | Não | Sequência da Conta bancária |
| CodBan | String(003) | Sim | Código do banco da conta corrente do favorecido |
| TipTcc | Number(002,0) | Sim | Tipo de conta |
| CodAge | String(007) | Sim | Código da agência do banco da conta corrente do favorecido |
| CcbFav | String(014) | Sim | Número da conta corrente do favorecido no banco |
| UsuGer | Number(010,0) | Sim | Usuário responsável pela geração do registro |
| DatGer | Date | Sim | Data da geração do registro |
| HorGer | Number(005,0) | Sim | Hora da geração do registro |
| IdeFav | String(050) | Não | Identificador único alfanumérico |

---

## Chave Primária

- IdeFav
- SeqBan

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
