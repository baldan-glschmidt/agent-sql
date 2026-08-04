# E005CEL

## Descrição

Tabelas - Células de Produção (Grupos de Trabalho)

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
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodCel | String(004) | Não | Código da Célula de Produção (Grupos de Trabalho) |
| DesCel | String(030) | Não | Descrição da Célula de Produção |
| AbrCel | String(010) | Sim | Abreviatura |
| CodOri | String(003) | Não | Código de Origem do Produto |

---

## Chave Primária

- CodEmp
- CodCel

---

## Índices

### E005CELIndice1

**Tipo:** Não unico

Campos:
- CodEmp
- CodOri

---

## Relacionamentos

### IR_E005CEL_004

**Tabela:** E083ORI

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodOri | CodOri |

