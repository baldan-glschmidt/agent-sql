# E016PVP

## Descrição

Tabelas - Períodos de  Produção/Vendas

---

## Resumo

- Campos: 13
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da Empresa |
| CodPvp | String(008) | Não | Código do Período de  Produção e Venda |
| DesPvp | String(030) | Não | Descrição do período de venda e produção |
| AbrPvp | String(010) | Não | Abreviatura do período de venda e produção |
| DatIni | Date | Não | Data inicial do período |
| DatFim | Date | Não | Data final do período |
| CodOri | String(003) | Sim | Código de Origem do Produto p/ este Período |
| MesAno | Date | Sim | Mês e Ano de Referencia Base do Período |
| CgaSml | String(001) | Não | Indicativo se a carga é simulada (quando o cálculo é encadeado) |
| DtfPvp | Date | Sim | Data do Fechamento do período p/ geração de necessidades |
| CodUsu | Number(010,0) | Sim | Código do Usuário que fechou o período |
| DatAlt | Date | Sim | Data Atualização do Fechamento |
| HorAlt | Number(005,0) | Sim | Hora Atualização do Fechamento |

---

## Chave Primária

- CodEmp
- CodPvp

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
