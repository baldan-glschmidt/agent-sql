# R074RUA

## Descrição

Logradouros

---

## Resumo

- Campos: 6
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodCid | Number(007,0) | Não | Código da Cidade |
| CodBai | Number(004,0) | Não | Código do Bairro da Empresa Responsável |
| CepRua | Number(008,0) | Não | Cep do Bairro |
| SeqRua | Number(009,0) | Não | Sequência |
| NomRua | String(040) | Sim | Endereço Residencial |
| TipLgr | String(005) | Sim | Tipo do Logradouro |

---

## Chave Primária

- CodCid
- CodBai
- CepRua
- SeqRua

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R074RUA_000

**Tabela:** R074CID

| Origem | Destino |
|--------|---------|
| CodCid | CodCid |

### IR_R074RUA_001

**Tabela:** R074BAI

| Origem | Destino |
|--------|---------|
| CodCid | CodCid |
| CodBai | CodBai |

