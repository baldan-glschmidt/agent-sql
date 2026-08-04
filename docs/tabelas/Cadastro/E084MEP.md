# E084MEP

## Descrição

Cadastros - Máscara endereçamento do produto

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
| CodMep | String(008) | Não | Código da máscara endereçamento do produto |
| DesMep | String(050) | Não | Descrição da Máscara |
| AbrMep | String(020) | Não | Abreviatura da Máscara |
| PosMep | Number(002,0) | Não | Quantidade de posições que o componente da máscara pode ser codificado |
| SitMep | String(001) | Não | Situação da máscara |
| MepLiv | String(001) | Sim | Indica se máscara é livre (sem componentes) |
| TipMep | String(001) | Sim | Indicativo se o componente da máscara é numérico ou alfanumérico |
| CodReg | Number(004,0) | Sim | Código da Regra |
| MepQip | Number(004,0) | Sim | Valor para incremento utilizado p/ sequenciar automaticamente Códigos numéricos da Máscara |
| UltCod | Number(014,0) | Sim | Último código numérico gerado (p/ máscaras c/ numeração auto incrementada) |

---

## Chave Primária

- CodEmp
- CodMep

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
