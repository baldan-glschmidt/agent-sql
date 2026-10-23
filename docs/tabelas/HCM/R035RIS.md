# R035RIS

## Descrição

PPP - Fatores de Riscos

---

## Resumo

- Campos: 26
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do Colaborador |
| SeqReg | Number(004,0) | Não | Sequência do registro |
| DatIni | Date | Sim | Data de início do Fator de Risco |
| DatTer | Date | Sim | Data de término do Fator de Risco |
| TipRis | String(010) | Sim | Tipo do Risco |
| DesAgt | String(060) | Sim | Descrição do Fator de Risco |
| IntCon | String(050) | Sim | Intensidade/Concentração do Fator de Risco |
| TecUti | String(100) | Sim | Descrição da técnica utilizada |
| EPCEfi | String(001) | Sim | Identifica se os EPC´s são eficazes |
| EPIEfi | String(001) | Sim | Identifica se os EPI´s são eficazes |
| DCAEPI | String(200) | Sim | Descrição do Certificado de Aprovação do EPI |
| SitRPP | Number(001,0) | Sim | Situação do Registro |
| IgnReg | String(001) | Sim | Define se o registro será ignorado na emissão do PPP |
| IndCon | String(001) | Sim | Apresenta se o registro está em conflito com outro |
| ObsLau | String(8001) | Sim | Observação sobre o Laudo |
| IdeAgN | String(015) | Sim | Identificador do agente nocivo (Obsoleto) |
| IdeFaR | Number(007,0) | Sim | Código do Fator de Risco |
| MedPro | String(001) | Sim | Medidas de proteção |
| ConFun | String(001) | Sim | Condições de funcionamento |
| PraVal | String(001) | Sim | Prazo de validade |
| PerTro | String(001) | Sim | Periocidade de troca |
| ObsHig | String(001) | Sim | Higienização |
| ConIns | String(001) | Sim | Considera insalubridade |
| ConPer | String(001) | Sim | Considera periculosidade |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- SeqReg

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
