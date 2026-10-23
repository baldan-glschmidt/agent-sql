# R110REM

## Descrição

Medicamentos

---

## Resumo

- Campos: 27
- Chave Primária: 1 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodRem | Number(006,0) | Não | Código do Medicamento |
| NomRem | String(060) | Sim | Nome do Medicamento |
| AprRem | String(050) | Sim | Apresentação |
| ConRem | String(700) | Sim | Concentração |
| PosRem | String(700) | Sim | Posologia |
| LabRem | String(050) | Sim | Laboratório |
| ConInd | String(700) | Sim | Contra-Indicações |
| ReaAdv | String(700) | Sim | Reações Adversas |
| PreRem | String(500) | Sim | Prescrição |
| UsoRem | String(050) | Sim | Uso do Medicamento |
| CodApr | Number(003,0) | Sim | Cód. forma de apresentação do medicamento |
| IndVcn | String(001) | Sim | Identifica se o medicamento é uma vacina |
| ConEst | Number(001,0) | Sim | Define como é o controle de estoque do medicamento |
| EstMin | Number(010,4) | Sim | Quantidade de estoque mínimo tolerável |
| DefPer | Number(001,0) | Sim | Controle da validade e periodicidade da vacina(1-Dias/2-Meses) |
| CodReg | Number(003,0) | Sim | Código da regra para estabelecer periodicidade da vacinação |
| PriDos | Number(003,0) | Sim | Periodicidade da primeira dose |
| SegDos | Number(003,0) | Sim | Periodicidade da segunda dose |
| TerDos | Number(003,0) | Sim | Periodicidade da terceira dose |
| OutDos | Number(003,0) | Sim | Periodicidade das demais doses |
| PriVal | Number(003,0) | Sim | Validade da primeira dose |
| SegVal | Number(003,0) | Sim | Validade da segunda dose |
| TerVal | Number(003,0) | Sim | Validade da terceira dose |
| OutVal | Number(003,0) | Sim | Validade das demais doses |
| QtdApl | Number(010,4) | Sim | Quantidade medicação para sugestão na aplicação |
| QtdDos | Number(002,0) | Sim | Quantidade de doses |
| USU_CodPro | String(014) | Sim | Codigo do Produto (Sapiens) |

---

## Chave Primária

- CodRem

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
