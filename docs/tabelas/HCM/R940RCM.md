# R940RCM

## Descrição

Cadastro de Máscaras para configurações Regionais

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
| CodCfg | Number(005,0) | Não | Código da configuração |
| OriMsk | String(255) | Não | Máscara original |
| NewMsk | String(255) | Não | Máscara configurada |

---

## Chave Primária

- CodCfg
- OriMsk

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R940RCM_000

**Tabela:** R940RCF

| Origem | Destino |
|--------|---------|
| CodCfg | CodCfg |

