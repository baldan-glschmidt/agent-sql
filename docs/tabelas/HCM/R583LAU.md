# R583LAU

## Descrição

GHE - Revisão do GHE - Laudo

---

## Resumo

- Campos: 65
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodPRA | Number(009,0) | Não | Código do Cadastro do PGR |
| CodGHE | Number(009,0) | Não | Código do GHE - Grupo Homogêneo de Exposição |
| RevGHE | String(010) | Não | Código da Revisão do GHE |
| CodAgt | Number(006,0) | Não | Código do Perigo/Fator de Risco |
| DatLau | Date | Sim | Data do Laudo |
| HorLau | Number(005,0) | Sim | Hora do Laudo |
| HorTer | Number(005,0) | Sim | Hora de término da medição |
| SinAge | String(002) | Sim | Operador da quantificação do perigo/fator de risco |
| QuaAge | Number(011,5) | Sim | Quantificação do perigo/fator de risco (Critério Portaria MTE 3214/78) |
| SinCol | String(002) | Sim | Operador da quantificação reduzida |
| QuaCol | Number(011,5) | Sim | Quantificação do perigo/fator de risco com fator de redução (Crit. Port. MTE 3214/78) |
| SinAte | String(002) | Sim | Operador da quantificação final |
| QuaAte | Number(011,5) | Sim | Quantificação final do perigo/fator de risco (Critério Portaria MTE 3214/78) |
| VlrTWA | Number(011,5) | Sim | Nível Médio de Pressão Sonora (Ruído) |
| VlrLEq | Number(011,5) | Sim | Nível Médio Baseado na Equivalência de Energia Sonora (Ruído) |
| VlrNEN | Number(011,5) | Sim | Nível de Exposição Normalizado (Ruído) - 8hs |
| TecUti | Number(004,0) | Sim | Código da Técnica de Medição |
| GraRis | Number(001,0) | Sim | Grau de Risco |
| NivAca | Number(011,5) | Sim | Intensidade/concentração p/Nível de Ação |
| LimTol | Number(011,5) | Sim | Intensidade/Concentração considerado Limite de Tolerância |
| QtdDos | Number(006,2) | Sim | Dose |
| MeiPpg | String(500) | Sim | Meio de Propagação |
| TemExp | String(200) | Sim | Tempo de Exposição Diário |
| JorTra | String(200) | Sim | Jornada de Trabalho (semanal) |
| ForExp | Number(001,0) | Sim | Forma de exposição |
| ConEfi | String(001) | Sim | Identifica se os EPI´s são eficazes |
| EPCEfi | String(001) | Sim | Identifica se os EPC´s são eficazes |
| SitAgt | String(001) | Sim | Situação de Controle do perigo/fator de risco |
| EmiPPP | String(001) | Sim | Considera este agente na emissão do PPP |
| EmiLTC | String(001) | Sim | Considera este agente na emissão do LTCAT |
| OutCon | String(8001) | Sim | Outras medidas de controle existentes |
| DesAva | String(8001) | Sim | Laudo |
| DesRes | String(1000) | Sim | Resultado do laudo para fins previdenciários |
| ResTra | String(1000) | Sim | Resultado do laudo para fins trabalhistas |
| ObsLau | String(8001) | Sim | Observação |
| CodOem | Number(008,0) | Sim | Código da empresa que realizou o laudo |
| CodPes | Number(009,0) | Sim | Código da Pessoa responsável pelo Laudo |
| IdeAgN | String(015) | Sim | Identificador do agente nocivo (Obsoleto) |
| IdeFaR | Number(007,0) | Sim | Código do Fator de Risco |
| CodAna | Number(007,0) | Sim | Código do Agente Nocivo |
| DesAna | String(999) | Sim | Descrição do Agente Nocivo |
| ConIns | String(001) | Sim | A exposição ao fator de risco configura trabalho insalubre? |
| ConPer | String(001) | Sim | A exposição ao fator de risco configura trabalho perigoso? |
| QuaAIN | Number(011,5) | Sim | Quantificação do perigo/fator de risco (Critério INSS) |
| QuaRIN | Number(011,5) | Sim | Quantificação do perigo/fator de risco considerando fator de redução (Critério INSS) |
| QuaFIN | Number(011,5) | Sim | Quantificação final do perigo/fator de risco (Critério INSS) |
| ApoEsp | Number(002,0) | Sim | A exposição ao fator de risco/execução da atividade enseja recolhimento do adicional para o financiamento da aposentadoria especial? |
| UtiEpi | Number(001,0) | Sim | Utilização de EPI |
| UtiEpc | Number(001,0) | Sim | O empregador implementa medidas de proteção coletiva (EPC)? |
| MedPro | String(001) | Sim | Foi tentada a implementação de medidas de proteção coletiva? |
| ConFun | String(001) | Sim | Foram observadas as condições de funcionamento do EPI ao longo do tempo? |
| UsoIni | String(001) | Sim | Foi observado o uso ininterrupto do EPI ao longo do tempo? |
| PraVal | String(001) | Sim | Foi observado o prazo de validade do Certificado de Aprovação - CA do MTb? |
| PerTro | String(001) | Sim | É observada a periodicidade de troca definida pelo fabricante nacional ou importador e/ou programas ambientais? |
| ObsHig | String(001) | Sim | É observada a higienização conforme orientação do fabricante nacional ou importador? |
| ConAso | String(001) | Sim | Informar se o risco deste laudo deve ser considerado no ASO |
| MatRis | Number(006,0) | Sim | Matriz de risco utilizada para realizar a classificação do agente |
| NivPro | Number(001,0) | Sim | Informar o nível de probabilidade do risco |
| NivSev | Number(001,0) | Sim | Informar o nível de severidade do risco |
| NivCla | Number(001,0) | Sim | Resultado da classificação do risco |
| ClaRis | String(250) | Sim | Classificação do risco |
| DesFat | String(080) | Sim | Descrição Fator de Risco/Perigo |
| EmPPRA | String(001) | Sim | Considera este perigo/fator de risco na emissão do PPRA |
| EmpPro | Number(004,0) | Sim | Código da Empresa do Processo |
| CodPro | Number(009,0) | Sim | Número do processo, em caso de agente nocivo incluído por determinação judicial |

---

## Chave Primária

- CodPRA
- CodGHE
- RevGHE
- CodAgt

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R583LAU_002

**Tabela:** R583REV

| Origem | Destino |
|--------|---------|
| CodPRA | CodPRA |
| CodGHE | CodGHE |
| RevGHE | RevGHE |

### IR_R583LAU_003

**Tabela:** R082AGT

| Origem | Destino |
|--------|---------|
| CodAgt | CodAgt |

