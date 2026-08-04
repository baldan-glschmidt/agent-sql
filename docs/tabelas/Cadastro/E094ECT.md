# E094ECT

## Descrição

Cadastros - Especificações Conformidade  Produto

---

## Resumo

- Campos: 8
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodEct | String(014) | Não | Código da especificação de conformidade |
| DesEct | String(030) | Não | Descrição da especificação de conformidade do produto |
| AbrEct | String(010) | Sim | Abreviatura da especificação de conformidade |
| TemCet | String(001) | Não | Indicativo se a Especificação de conformidade de produto tem ou não componentes pré definidos |
| UniEct | String(015) | Não | Unidade de medição da especificação de conformidade |
| ObsEct | String(240) | Sim | Observação complementar |
| CodReg | Number(004,0) | Sim | Código da Regra |

---

## Chave Primária

- CodEmp
- CodEct

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
