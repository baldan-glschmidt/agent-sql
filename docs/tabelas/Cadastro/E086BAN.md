# E086BAN

## Descrição

Cadastros - Sacados - Contas Bancárias

---

## Resumo

- Campos: 10
- Chave Primária: 2 campo(s)
- Índices: 1
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodSac | Number(014,0) | Não | Número do CNPJ ou CPF do sacado |
| DocIdeSac | String(014) | Sim | Número do CNPJ ou CPF do sacado |
| SeqBan | Number(004,0) | Não | Sequência da Conta bancária |
| CodBan | String(003) | Sim | Código do banco da conta corrente do sacado |
| CodAge | String(007) | Sim | Código da agência do banco da conta corrente do sacado |
| CcbSac | String(014) | Sim | Número da conta corrente do sacado no banco |
| UsuGer | Number(010,0) | Sim | Usuário responsável pela geração do registro |
| DatGer | Date | Sim | Data da geração do registro |
| HorGer | Number(005,0) | Sim | Hora da geração do registro |
| IdeSac | String(050) | Não | Identificador único alfanumérico |

---

## Chave Primária

- IdeSac
- SeqBan

---

## Índices

### E086BANIndice2

**Tipo:** Não unico

Campos:
- CodBan
- CodAge
- CcbSac

---

## Relacionamentos

Nenhum relacionamento cadastrado.
