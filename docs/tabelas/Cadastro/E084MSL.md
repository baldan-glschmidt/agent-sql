# E084MSL

## Descrição

Cadastros - Máscara Séries e Lotes

---

## Resumo

- Campos: 14
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Empresa |
| CodMsl | String(008) | Não | Código da Máscara de Produto |
| DesMsl | String(020) | Não | Descrição da Máscara |
| AbrMsl | String(010) | Não | Abreviatura da Máscara |
| PosMsl | Number(002,0) | Não | Quantidade de posições do componente da máscara (máximo 50) |
| SitMsl | String(001) | Não | Situação da Máscara |
| MslLiv | String(001) | Sim | Indica se Máscara é livre (sem componentes) |
| TipMsl | String(001) | Sim | Indicativo se o componente da máscara é Numérico ou Alfanumérico |
| CodReg | Number(004,0) | Sim | Código da Regra |
| MslQip | Number(004,0) | Sim | Valor para incremento utilizado p/ sequenciar automaticamente Códigos numéricos da Máscara |
| MslSep | String(001) | Não | Indicativo se a Máscara é utilizada p/ compor código da Série |
| MslLot | String(001) | Não | Indicativo se a Máscara é utilizada p/ compor código do Lote |
| UltCod | Number(014,0) | Sim | Último código numérico gerado (para máscaras com numeração auto incrementada) |
| UltNum | String(050) | Sim | Último código numérico gerado (para máscaras com numeração auto incrementada) |

---

## Chave Primária

- CodEmp
- CodMsl

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
