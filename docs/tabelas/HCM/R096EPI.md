# R096EPI

## Descrição

Epi

---

## Resumo

- Campos: 29
- Chave Primária: 1 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEpi | Number(008,0) | Não | Código do Epi |
| DesEpi | String(150) | Sim | Descrição do Epi |
| DiaVal | Number(004,0) | Sim | Dias de Validade do Epi |
| DiaRev | Number(004,0) | Sim | Dias de Revisão do Epi |
| DevEpi | String(001) | Sim | Devolver Epi |
| ValEpi | Number(011,2) | Sim | Valor do Epi |
| NumAlm | String(015) | Sim | Nº do Epi no Almoxarifado |
| CerApr | String(020) | Sim | Certificado de Aprovação |
| CarEpi | String(7800) | Sim | Características do EPI |
| TipEpi | String(020) | Sim | Tipo do Epi |
| InsUso | String(001) | Sim | Indica se necessita de instrução de uso |
| EpiDes | String(001) | Sim | Epi Descartável |
| ConUso | String(001) | Sim | Confirmar Uso do EPI |
| TipEqu | Number(003,0) | Sim | Código do tipo de EPI |
| FatRed | Number(011,5) | Sim | Fator de redução de exposição ao risco |
| ConEst | Number(001,0) | Sim | Define se o EPI possui controle de estoque |
| QtdMin | Number(007,0) | Sim | Quantidade de estoque mínimo tolerável |
| DatInu | Date | Sim | Data de Inutilização |
| CerCon | String(100) | Sim | Número do Certificado de Conformidade |
| DatVcc | Date | Sim | Data de Validade do Certificado de Conformidade |
| CatRis | Number(001,0) | Sim | Categoria de risco na qual o EPI se enquadra |
| USU_EPIMED | String(010) | Sim | Medida EPI |
| USU_CodPro | String(014) | Sim | Código do produto no Sapiens |
| USU_DesPro | String(070) | Sim | Descrição Produto |
| USU_DatVal | Date | Sim | Data Validade CA |
| USU_MEDEPI | String(001) | Sim | Utiliza Medida |
| USU_ParPro | String(001) | Sim | Participa Processo Automatico |
| USU_EpiUni | String(001) | Sim | O EPI é um uniforme? |
| USU_EpiMedU | String(010) | Sim | Medida EPI |

---

## Chave Primária

- CodEpi

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
