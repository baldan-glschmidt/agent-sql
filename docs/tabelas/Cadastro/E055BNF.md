# E055BNF

## Descrição

Cadastros - Tributos - Benefício fiscal

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
| CodBnf | Number(004,0) | Não | Código do benefício fiscal |
| DesBnf | String(250) | Não | Descrição do benefício fiscal |
| TipBnf | Number(002,0) | Sim | Tipo do benefício fiscal |
| PerRed | Number(007,4) | Sim | Percentual de redução |
| IndPrj | Number(002,0) | Não | Indicador de projeto |
| AtoCon | String(030) | Não | Ato concessório |
| PerIni | Date | Não | Início da vigência |
| PerFim | Date | Não | Fim da vigência |
| UsuGer | Number(010,0) | Sim | Usuário responsável pela geração do registro |
| DatGer | Date | Sim | Data da geração do registro |
| HorGer | Number(005,0) | Sim | Hora da geração do registro |
| UsuAlt | Number(010,0) | Sim | Usuário responsável pela última alteração do registro |
| DatAlt | Date | Sim | Data da última alteração do registro |
| HorAlt | Number(005,0) | Sim | Hora da última alteração do registro |

---

## Chave Primária

- CodEmp
- CodBnf

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
