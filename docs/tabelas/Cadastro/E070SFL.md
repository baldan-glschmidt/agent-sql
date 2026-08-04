# E070SFL

## Descrição

Cadastros - Filiais - Serviços Financeiros para Varejo

---

## Resumo

- Campos: 13
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| CodSer | String(014) | Não | Código do serviço |
| CodPro | String(014) | Não | Código do produto |
| VarSer | String(001) | Sim | Indica o tipo de serviço para o Varejo |
| VarPro | String(001) | Sim | Indica o tipo de produto para o Varejo |
| CodSeg | Number(009,0) | Sim | Código da Seguradora |
| CodTpr | String(004) | Sim | Código da tabela de preço padrão para serviços de varejo |
| CodOte | Number(004,0) | Sim | Código da operadora de telefonia |
| BloqVen | String(001) | Sim | Indicativo se a venda deve ser bloqueada quando este serviço não for informado |
| SugVen | String(001) | Sim | Indicativo se este serviço deve ser sugerido automaticamente na venda |
| ObsSer | String(250) | Sim | Observação da ligação |
| SitReg | String(001) | Não | Situação do registro |

---

## Chave Primária

- CodEmp
- CodFil
- CodSer
- CodPro

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
