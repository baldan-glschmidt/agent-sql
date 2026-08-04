# E095BAN

## Descrição

Cadastros - Fornecedores - Contas Bancárias

---

## Resumo

- Campos: 10
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodFor | Number(009,0) | Não | Código do fornecedor |
| SeqBan | Number(004,0) | Não | Sequência da Conta bancária |
| CodBan | String(003) | Sim | Código do banco da conta corrente do fornecedor |
| CodAge | String(007) | Sim | Código da agência do banco da conta corrente do fornecedor |
| CcbFor | String(014) | Sim | Número da conta corrente do fornecedor no banco |
| SisGer | String(016) | Sim | Sistema gerador do registro |
| TipTcc | Number(002,0) | Sim | Tipo de conta |
| UsuGer | Number(010,0) | Sim | Usuário responsável pela geração do registro |
| DatGer | Date | Sim | Data da geração do registro |
| HorGer | Number(005,0) | Sim | Hora da geração do registro |

---

## Chave Primária

- CodFor
- SeqBan

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
