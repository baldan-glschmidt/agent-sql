# E084MPJ

## Descrição

Cadastros - Máscara Projeto

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
| CodMpj | String(008) | Não | Código da Máscara de Projeto |
| DesMpj | String(020) | Não | Descrição da Máscara |
| AbrMpj | String(010) | Não | Abreviatura da Máscara |
| PosPrj | Number(002,0) | Não | Quantidade de posições que o componente da máscara pode ser codificado (máximo 20) |
| SitMpj | String(001) | Não | Situação da Máscara de Projeto |
| MpjLiv | String(001) | Sim | Indica se Máscara de Projeto é livre (sem componentes) |
| TipMpj | String(001) | Sim | Indicativo se o componente da máscara é Numérico ou Alfanumérico |
| CodReg | Number(004,0) | Sim | Código da Regra |
| MpjQip | Number(004,0) | Sim | Valor para incremento utilizado p/ sequenciar automaticamente Códigos numéricos da Máscara |
| UltCod | Number(014,0) | Sim | Último código numérico gerado (p/ máscaras c/ numeração auto incrementada) |

---

## Chave Primária

- CodEmp
- CodMpj

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
