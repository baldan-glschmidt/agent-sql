# E075BAR

## Descrição

Cadastros - Produtos - Códigos de Barras

---

## Resumo

- Campos: 15
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodBar | String(020) | Não | Código de barras |
| CodPro | String(014) | Não | Código do produto |
| CodDer | String(007) | Não | Código da derivação do produto |
| UniMed | String(003) | Sim | Código da unidade de medida para o código de barras |
| UsuGer | Number(010,0) | Sim | Usuário responsável pela geração do registro |
| HorGer | Number(005,0) | Sim | Hora da geração do registro |
| DatGer | Date | Sim | Data da geração do registro |
| UsuAlt | Number(010,0) | Sim | Usuário responsável pela última alteração do registro |
| HorAlt | Number(005,0) | Sim | Hora da última alteração do registro |
| DatAlt | Date | Não | Data da última alteração do registro |
| ExpWms | Number(001,0) | Sim | Indicativo se o código de barras foi exportado para o sistema WMS |
| CodEmb | Number(004,0) | Sim | Código da embalagem |
| CodGti | Number(014,0) | Sim | Deprecado |
| CodGtn | String(014) | Sim | GTIN Unidade Tributável |

---

## Chave Primária

- CodEmp
- CodBar

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
