# E084MPR

## Descrição

Cadastros - Máscara Produto

---

## Resumo

- Campos: 11
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Empresa |
| CodMpr | String(008) | Não | Código da Máscara de Produto |
| DesMpr | String(050) | Não | Descrição da Máscara |
| AbrMpr | String(020) | Não | Abreviatura da Máscara |
| PosPro | Number(002,0) | Não | Quantidade de posições que o componente da máscara pode ser codificado (máximo 14) |
| SitMpr | String(001) | Não | Situação da Máscara de Produto |
| MprLiv | String(001) | Sim | Indica se Máscara de Produto é livre (sem componentes) |
| TipMpr | String(001) | Sim | Indicativo se o componente da máscara é Numérico ou Alfanumérico |
| CodReg | Number(004,0) | Sim | Código da Regra |
| MprQip | Number(004,0) | Sim | Valor para incremento utilizado p/ sequenciar automaticamente Códigos numéricos da Máscara |
| UltCod | Number(014,0) | Sim | Último código numérico gerado (p/ máscaras c/ numeração auto incrementada) |

---

## Chave Primária

- CodEmp
- CodMpr

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
