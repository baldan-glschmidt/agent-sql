# R583EPI

## Descrição

GHE - Revisão do GHE - EPIs

---

## Resumo

- Campos: 15
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodPRA | Number(009,0) | Não | Código do Cadastro do PGR |
| CodGHE | Number(009,0) | Não | Código do GHE - Grupo Homogêneo de Exposição |
| RevGHE | String(010) | Não | Código da Revisão do GHE |
| CodAgt | Number(006,0) | Não | Código do Perigo/Fator de Risco |
| CodEpi | Number(008,0) | Não | Código do EPI |
| DiaVal | Number(004,0) | Sim | Dias de validade do EPI |
| DiaRev | Number(004,0) | Sim | Dias de revisão do EPI |
| EpiEfi | String(001) | Sim | Identifica se o EPI é eficaz |
| MedPro | String(001) | Sim | Foi tentada a implantação de medidas de proteção coletiva? |
| ConFun | String(001) | Sim | Foram observadas as condições de funcionamento? |
| UsoIni | String(001) | Sim | Foi observado o uso ininterrupto? |
| PraVal | String(001) | Sim | Foi observado o prazo de validade? |
| PerTro | String(001) | Sim | É observada a periodicidade de troca? |
| ObsHig | String(001) | Sim | É observada a higienização? |
| USU_QtdEpi | Number(002,0) | Sim | Quantidade EPI |

---

## Chave Primária

- CodPRA
- CodGHE
- RevGHE
- CodAgt
- CodEpi

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R583EPI_004

**Tabela:** R096EPI

| Origem | Destino |
|--------|---------|
| CodEpi | CodEpi |

