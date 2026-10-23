# R111VLO

## Descrição

Vacinação - Vacinas por Local

---

## Resumo

- Campos: 19
- Chave Primária: 7 campo(s)
- Índices: 0
- Relacionamentos: 3

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código Empresa |
| CodCam | Number(004,0) | Não | Código de identificação da campanha |
| SeqCam | Number(002,0) | Não | Sequência da campanha |
| TabOrg | Number(004,0) | Não | Código da tabela de organograma do local |
| NumLoc | Number(009,0) | Não | Local do organograma |
| CodRem | Number(006,0) | Não | Código da vacina |
| DatIni | Date | Não | Data de início da vacinação |
| DatTer | Date | Sim | Data de término da vacinação |
| CodReg | Number(003,0) | Sim | Código da regra para estabelecer periodicidade da vacinação |
| PerDet | String(001) | Sim | Define se a periodicidade está detalhada neste registro |
| PriDos | Number(003,0) | Sim | Periodicidade da primeira dose |
| SegDos | Number(003,0) | Sim | Periodicidade da segunda dose |
| TerDos | Number(003,0) | Sim | Periodicidade da terceira dose |
| OutDos | Number(003,0) | Sim | Periodicidade das demais doses |
| PriVal | Number(003,0) | Sim | Validade da primeira dose |
| SegVal | Number(003,0) | Sim | Validade da segunda dose |
| TerVal | Number(003,0) | Sim | Validade da terceira dose |
| OutVal | Number(003,0) | Sim | Validade das demais doses |
| QtdDos | Number(002,0) | Sim | Quantidade de doses |

---

## Chave Primária

- NumEmp
- CodCam
- SeqCam
- TabOrg
- NumLoc
- DatIni
- CodRem

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R111VLO_002

**Tabela:** R111DEF

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodCam | CodCam |
| SeqCam | SeqCam |

### IR_R111VLO_004

**Tabela:** R016ORN

| Origem | Destino |
|--------|---------|
| TabOrg | TabOrg |
| NumLoc | NumLoc |

### IR_R111VLO_005

**Tabela:** R110REM

| Origem | Destino |
|--------|---------|
| CodRem | CodRem |

