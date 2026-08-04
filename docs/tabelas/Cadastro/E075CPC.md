# E075CPC

## Descrição

Cadastros - Produtos - Correlação entre códigos de produtos comercializados

---

## Resumo

- Campos: 6
- Chave Primária: 5 campo(s)
- Índices: 1
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| ProCom | String(014) | Não | Código do produto comercializado |
| DerCom | String(007) | Não | Código da derivação do produto comercializado |
| CodPro | String(014) | Não | Código do produto |
| CodDer | String(007) | Não | Código da derivação |
| QtdPro | Number(014,6) | Não | Quantidade |

---

## Chave Primária

- CodEmp
- ProCom
- DerCom
- CodPro
- CodDer

---

## Índices

### E075CPCIndice1

**Tipo:** Não unico

Campos:
- CodEmp
- ProCom
- DerCom

---

## Relacionamentos

Nenhum relacionamento cadastrado.
