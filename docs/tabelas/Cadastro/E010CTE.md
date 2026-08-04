# E010CTE

## Descrição

Cadastros - Características de Produto

---

## Resumo

- Campos: 9
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodCte | String(003) | Não | Código da característica de produto |
| DesCte | String(030) | Não | Descrição da característica de produto |
| TemCcp | String(001) | Não | Indicativo se a característica de produto tem ou não componentes |
| TipCcp | String(001) | Não | Indicativo se o componente da característica é Numérico ou Alfanumérico |
| PosCte | Number(003,0) | Sim | Quantidade de posições do componente da característica de produto |
| CodReg | Number(004,0) | Sim | Código da Regra |
| CteDer | String(001) | Não | Característica é  para Derivação (S=Sim) ou p/ Produto (N=Não) |
| IndNve | String(001) | Sim | Indica se Característica é para NVE |

---

## Chave Primária

- CodEmp
- CodCte

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
