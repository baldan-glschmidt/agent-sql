# R082AGT

## Descrição

Perigos/Fatores de Risco

---

## Resumo

- Campos: 36
- Chave Primária: 1 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodAgt | Number(006,0) | Não | Código do Perigo/Fator de Risco |
| DesAgt | String(060) | Sim | Descrição do Perigo/Fator de Risco |
| TipRis | Number(002,0) | Sim | Tipo do Risco |
| CorRis | Number(001,0) | Sim | Cor do perigo/fator de risco |
| TolMin | Number(011,5) | Sim | Intensidade/concentração p/Nível de Ação |
| TolMax | Number(011,5) | Sim | Intensidade/Concentração considerado Limite de Tolerância |
| UniAfe | String(010) | Sim | Unidade de Medição do Agente |
| TabAdo | String(015) | Sim | Tabela Adotada |
| CdNB18 | Number(009,0) | Sim | Código NBR14280 da ABNT |
| IndUso | Number(001,0) | Sim | Identifica agente causador de lesão e perigo/fator de risco |
| DesCpl | String(500) | Sim | Descrição detalhada do perigo/fator risco |
| ObsAgt | String(700) | Sim | Observação sobre o perigo/fator risco |
| ValMax | Number(011,5) | Sim | Intensidade/Concentração considerada Máxima |
| IndTet | String(001) | Sim | OBSOLETO 5.5.1.10 - Identifica se o agente tem valor teto |
| DefLTN | String(001) | Sim | Nível de ação/limite tolerância definido por agente ou laudo |
| AgeQua | String(001) | Sim | Identifica se o agente é somente qualitativo |
| AprQua | String(015) | Sim | Descrição p/apresentação PPP p/ agente somente qualitativo |
| UtiDos | String(001) | Sim | Define se deve ser informada a dose no cadastro do laudo |
| EmiPPP | String(001) | Sim | Considera este perigo/fator de risco na emissão do PPP |
| EmiLTC | String(001) | Sim | Considera este perigo/fator de risco na emissão do LTCAT |
| SubAti | String(060) | Sim | Descrição da substância ativa |
| QtdCas | Number(001,0) | Sim | Define a Quantidade de Casas decimais do agente |
| UsaFat | String(001) | Sim | Define se no laudo será aplicado o fator de redução |
| ConPPP | String(001) | Sim | Define se o controle de medição será pelo NA ou LT |
| ConLim | String(001) | Sim | Critério para identificar medição alterada |
| InfInt | String(001) | Sim | Informa intervalo de quantificação no Laudo |
| InfTec | String(001) | Sim | Apresenta técnica utilizada na medição cadastrada no laudo |
| UtiTWA | String(001) | Sim | Define se utiliza LAVG (TWA) para medir o nível do ruído |
| UtiLEq | String(001) | Sim | Define se utiliza LEq para medir o nível do ruído |
| UtiNEN | String(001) | Sim | Define se utiliza NEN para medir o nível do ruído |
| IdeAgN | String(015) | Sim | Identificador do agente nocivo (Obsoleto) |
| IdeFaR | Number(007,0) | Sim | Código do Fator de Risco |
| CodAna | Number(007,0) | Sim | Código do Agente Nocivo |
| DesAna | String(999) | Sim | Descrição do Agente Nocivo |
| UniMed | Number(002,0) | Sim | Unidade de medida da intensidade ou concentração no eSocial |
| MatRis | Number(006,0) | Sim | Informar a técnica utilizada para realizar a avaliação dos riscos |

---

## Chave Primária

- CodAgt

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
