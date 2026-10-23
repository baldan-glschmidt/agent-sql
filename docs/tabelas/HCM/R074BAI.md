# R074BAI

## Descrição

Bairros

---

## Resumo

- Campos: 5
- Chave Primária: 2 campo(s)
- Índices: 1
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodCid | Number(007,0) | Não | Código da Cidade |
| CodBai | Number(004,0) | Não | Código do Bairro |
| NomBai | String(040) | Sim | Nome do Bairro |
| CepBai | Number(008,0) | Sim | Cep do Bairro |
| CodRad | Number(002,0) | Sim | Código da Região Administrativa |

---

## Chave Primária

- CodCid
- CodBai

---

## Índices

### R074BAIIndice2

**Tipo:** Unico

Campos:
- CodCid
- NomBai
- CodBai

---

## Relacionamentos

### IR_R074BAI_000

**Tabela:** R074CID

| Origem | Destino |
|--------|---------|
| CodCid | CodCid |

