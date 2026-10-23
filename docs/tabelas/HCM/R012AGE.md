# R012AGE

## Descrição

Agências Bancárias

---

## Resumo

- Campos: 7
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodBan | Number(004,0) | Não | Código do Banco |
| CodAge | Number(005,0) | Não | Código da Agência |
| NomAge | String(030) | Sim | Nome da Agência |
| CodPai | Number(004,0) | Sim | Código do País |
| CodEst | String(004) | Sim | Estado |
| CodCid | Number(007,0) | Sim | Código Cidade da Agência |
| DigAge | String(002) | Sim | Dígito da agência bancária |

---

## Chave Primária

- CodBan
- CodAge

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R012AGE_000

**Tabela:** R012BAN

| Origem | Destino |
|--------|---------|
| CodBan | CodBan |

### IR_R012AGE_005

**Tabela:** R074CID

| Origem | Destino |
|--------|---------|
| CodCid | CodCid |

