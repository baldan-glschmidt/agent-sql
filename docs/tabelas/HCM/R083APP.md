# R083APP

## Descrição

PPP Rubi - Atividades do PPP

---

## Resumo

- Campos: 20
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodAtv | Number(004,0) | Não | Código da atividade |
| DatIni | Date | Não | Data do início da atividade |
| CodAgt | Number(006,0) | Não | Código do Perigo/Fator de Risco |
| NomAtv | String(050) | Sim | Descrição reduzida da Atividade |
| DesAtv | String(4000) | Sim | Descrição detalhada da atividade |
| DesAgt | String(050) | Sim | Descrição do perigo/fator de risco |
| DesCon | String(050) | Sim | Descrição da concentração |
| TecUti | String(050) | Sim | Técnica utilizada |
| ProEfi | String(300) | Sim | Identifica se a proteção é eficaz - campo obsoleto |
| ExpAge | Number(001,0) | Sim | Define a exposição agente nocivo |
| DatFim | Date | Sim | Data fim da atividade |
| EPCEfi | String(001) | Sim | Identifica se os EPC´s são eficazes |
| EPIEfi | String(001) | Sim | Identifica se os EPI´s são eficazes |
| TipAge | String(001) | Sim | Tipo do perigo/fator de risco |
| CerAp1 | String(005) | Sim | Código de Certificado do EPI |
| CerAp2 | String(005) | Sim | Código de Certificado do EPI |
| CerAp3 | String(005) | Sim | Código de Certificado do EPI |
| CerAp4 | String(005) | Sim | Código de Certificado do EPI |
| CerAp5 | String(005) | Sim | Código de Certificado do EPI |
| AgeNoc | String(008) | Sim | Define o agente nocivo correspondente |

---

## Chave Primária

- CodAtv
- DatIni
- CodAgt

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
