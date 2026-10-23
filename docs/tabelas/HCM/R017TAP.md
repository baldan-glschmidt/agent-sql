# R017TAP

## Descrição

Tipo de Atuação do Posto

---

## Resumo

- Campos: 12
- Chave Primária: 1 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodTap | Number(003,0) | Não | Código do Tipo de atuação do Posto |
| DesTap | String(040) | Sim | Descrição do Tipo de atuação |
| ConVag | String(001) | Sim | Indica se atuações deste tipo contabilizam uma vaga no Quadro de Lotação |
| HisPri | String(001) | Sim | Indica se atuações deste tipo caracterizam Históricos Principais |
| ConCar | String(001) | Sim | Indica se atuações deste tipo consistem as características do Posto |
| ObjTap | String(700) | Sim | Objetivo do Tipo de atuação |
| ConPPP | String(001) | Sim | Considerar o posto adicional na rotina de PPP |
| ConLTC | String(001) | Sim | Considerar o posto adicional nos relatórios de LTCAT |
| PerAdi | Number(009,5) | Sim | Percentual de Adicional de Posto |
| PagPos | Number(001,0) | Sim | Pagamento Adicional Posto |
| TipAtu | String(001) | Sim | Titular ou Substituto |
| ConEmp | String(001) | Sim | Indicar se históricos com esse tipo de atuação devem ser considerados como empréstimo |

---

## Chave Primária

- CodTap

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
