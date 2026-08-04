# E069CXC

## Descrição

Cadastros - Convênios - Convênios x Condições de Pagamento

---

## Resumo

- Campos: 13
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodCpg | String(006) | Não | Código da condição de pagamento |
| CodCnv | Number(004,0) | Não | Código do convênio |
| DesCnv | String(050) | Sim | Descrição do convênio |
| DesCpg | String(050) | Sim | Descrição da condição de pagamento |
| SitReg | String(001) | Não | Situação do registro |
| IndPad | String(001) | Sim | Indicativo de que esta forma de pagamento é padrão para o convênio |
| UsuGer | Number(010,0) | Sim | Usuário responsável pela geração do registro |
| DatGer | Date | Sim | Data da geração do registro |
| HorGer | Number(005,0) | Sim | Hora da geração do registro |
| UsuAlt | Number(010,0) | Sim | Usuário responsável pela última alteração do registro |
| DatAlt | Date | Sim | Data da última alteração do registro |
| HorAlt | Number(005,0) | Sim | Hora da última alteração do registro |

---

## Chave Primária

- CodEmp
- CodCpg
- CodCnv

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
