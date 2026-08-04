# E084MBM

## Descrição

Cadastros - Máscara Código do Bem

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
| CodMbm | String(008) | Não | Código da Máscara do Bem |
| DesMbm | String(020) | Não | Descrição da Máscara |
| AbrMbm | String(010) | Não | Abreviatura da Máscara |
| PosPro | Number(002,0) | Não | Quantidade de posições que o componente da máscara pode ser codificado (máximo 20) |
| SitMbm | String(001) | Não | Situação da Máscara do Bem |
| MbmLiv | String(001) | Sim | Indica se Máscara do Bem é livre (sem componentes) |
| TipMbm | String(001) | Sim | Indicativo se o componente da máscara é Numérico ou Alfanumérico |
| IndEsp | String(001) | Não | Indicativo se a máscara verifica a espécie (somente para máscaras com componentes MbmLiv = 'N') |
| CodReg | Number(004,0) | Sim | Código da Regra |
| MbmQip | Number(004,0) | Sim | Valor para incremento utilizado p/ sequenciar automaticamente Códigos numéricos da Máscara |
| UltCod | Number(014,0) | Sim | Último código numérico gerado (p/ máscaras c/ numeração auto incrementada) |
| IndFil | String(001) | Sim | Indicativo se a máscara verifica a filial (somente para máscaras com componentes MbmLiv = 'N') |
| MbmInc | String(008) | Sim | Código da máscara final para incremento |

---

## Chave Primária

- CodEmp
- CodMbm

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
