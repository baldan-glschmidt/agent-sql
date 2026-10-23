# R108RES

## Descrição

Resultados Exames

---

## Resumo

- Campos: 122
- Chave Primária: 4 campo(s)
- Índices: 2
- Relacionamentos: 3

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Número da Empresa |
| CodFic | Number(009,0) | Não | Código Ficha Médica |
| CodExa | Number(004,0) | Não | Código do Exame |
| DatSol | Date | Não | Data Solicitação do Exame |
| DatMar | Date | Sim | Data Marcada Para o Exame |
| HorMar | Number(005,0) | Sim | Hora Marcada Para o Exame |
| DatRes | Date | Sim | Data Resultado do Exame |
| OriExa | Number(003,0) | Sim | Origem do Exame |
| ModOri | String(001) | Sim | Modulo Origem |
| CodOem | Number(008,0) | Sim | Cadastro do Convênio |
| OemExa | Number(008,0) | Sim | Entidade Realização Exame |
| CodAte | Number(006,0) | Sim | Código do Atendente |
| CodPar | Number(003,0) | Sim | Código do Parecer |
| ObsRex | String(800) | Sim | Observação |
| CodUsu | Number(010,0) | Sim | Código do Usuário |
| TipExa | String(001) | Sim | Tipo Exame |
| IndMas | String(001) | Sim | Indicador de Mascaramento |
| CodAud | Number(003,0) | Sim | Código do Audiômetro |
| CodMas | Number(003,0) | Sim | Tipo do Mascaramento |
| ParEsq | Number(003,0) | Sim | Código do Parecer Orelha Esquerda |
| NumGer | Number(009,0) | Sim | Nr. identificação da geração de solicitação |
| RepAud | Number(002,0) | Sim | Horas em repouso auditivo |
| AteAso | Number(006,0) | Sim | Código do atendente que emitiu o ASO |
| NumAte | Number(009,0) | Sim | Número  ASO onde o exame foi emitido |
| OriOcu | String(001) | Sim | Define se a origem do problema audiométrico é ocupacional |
| AteRes | Number(006,0) | Sim | Código do Atendente Responsável pelo Exame |
| MeatOD | Number(003,0) | Sim | Meatoscopia da Orelha Direita |
| MeatOE | Number(003,0) | Sim | Meatoscopia da Orelha Esquerda |
| OtosOD | String(300) | Sim | Otoscopia Orelha Direita |
| OtosOE | String(300) | Sim | Otoscopia Orelha Esquerda |
| MasViA | Number(003,0) | Sim | Tipo do Mascaramento da Via Aérea |
| MasViO | Number(003,0) | Sim | Tipo do Mascaramento da Via Óssea |
| MiVAOD | Number(003,0) | Sim | Mascaramento Mínimo - Via Aérea - OD |
| MaVAOD | Number(003,0) | Sim | Mascaramento Máximo - Via Aérea - OD |
| MiVOOD | Number(003,0) | Sim | Mascaramento Mínimo - Via Óssea - OD |
| MaVOOD | Number(003,0) | Sim | Mascaramento Máximo - Via Óssea - OD |
| MiVAOE | Number(003,0) | Sim | Mascaramento Mínimo - Via Aérea - OE |
| MaVAOE | Number(003,0) | Sim | Mascaramento Máximo - Via Aérea - OE |
| MiVOOE | Number(003,0) | Sim | Mascaramento Mínimo - Via Óssea - OE |
| MaVOOE | Number(003,0) | Sim | Mascaramento Máximo - Via Óssea - OE |
| MasLog | Number(003,0) | Sim | Tipo do Mascaramento da Logoaudiometria |
| MasLOD | Number(003,0) | Sim | Quantificação Mascaramento Logoaudiometria Orelha Direita |
| PalMOD | Number(002,0) | Sim | IRF - Quantidade de palavras Monossílabas OD |
| MaMoOD | String(001) | Sim | IRF - Mascaramento Monossílabas OD |
| PalDOD | Number(002,0) | Sim | IRF - Quantidade de palavras Dissílabas OD |
| MaDiOD | String(001) | Sim | IRF - Mascaramento Dissílabas OD |
| QSDTOD | Number(003,0) | Sim | Limiar de Detecção de Fala - Orelha Direita |
| MSDTOD | String(001) | Sim | Mascaramento SDT OD |
| QSRTOD | Number(003,0) | Sim | Limiar de Reconhecimento de Fala - Orelha Direita |
| MSRTOD | String(001) | Sim | Mascaramento SRT OD |
| MasLOE | Number(003,0) | Sim | Quantificação Mascaramento Logoaudiometria Orelha Esquerda |
| PalMOE | Number(002,0) | Sim | IRF - Quantidade de palavras Monossílabas OE |
| MaMoOE | String(001) | Sim | IRF - Mascaramento Monossílabas OE |
| PalDOE | Number(002,0) | Sim | IRF - Quantidade de palavras Dissílabas OE |
| MaDiOE | String(001) | Sim | IRF - Mascaramento Dissílabas OE |
| QSDTOE | Number(003,0) | Sim | Limiar de Detecção de Fala - Orelha Esquerda |
| MSDTOE | String(001) | Sim | Mascaramento SDT OE |
| QSRTOE | Number(003,0) | Sim | Limiar de Reconhecimento de Fala - Orelha Esquerda |
| MSRTOE | String(001) | Sim | Mascaramento SRT OE |
| SobAve | String(001) | Sim | Define se o resultado está sob averiguação |
| ConPPP | String(001) | Sim | Considera este resultado na emissão do PPP |
| SitExa | String(001) | Sim | Define a situação do Exame |
| PODTPe | Number(003,0) | Sim | Tipo de Perda da Orelha Direita |
| POETPe | Number(003,0) | Sim | Tipo de Perda da Orelha Esquerda |
| PODCli | Number(003,0) | Sim | Parecer Clínico da Orelha Direita |
| POECli | Number(003,0) | Sim | Parecer Clínico da Orelha Esquerda |
| PODPer | Number(003,0) | Sim | Parecer Pereira da Orelha Direita |
| POEPer | Number(003,0) | Sim | Parecer Pereira da Orelha Esquerda |
| PODIns | Number(003,0) | Sim | Parecer INSS da Orelha Direita |
| POEIns | Number(003,0) | Sim | Parecer INSS da Orelha Esquerda |
| NorAlt | String(001) | Sim | Resultado do exame (N-Normal/A-Alterado) |
| EvoRes | String(001) | Sim | Evolução resultado (E-Estável/A-Agravamento/M-Melhorado) |
| SitRes | String(001) | Sim | Situação do resultado(O-Ocupacional/N-Não Ocupacional) |
| UltAte | Number(006,0) | Sim | Atendente que efetuou a última alteração no Resultado |
| StaExa | Number(001,0) | Sim | Status do exame (Aberto/Concluído) |
| PODMDS | Number(003,0) | Sim | Parecer Davis & Silverman da Orelha Direita |
| POEMDS | Number(003,0) | Sim | Parecer Davis & Silverman da Orelha Esquerda |
| PFDSDe | Number(007,4) | Sim | Fowler - Percentual de perda da Orelha direita s/ desconto |
| PFDCDe | Number(007,4) | Sim | Fowler - Percentual de perda da Orelha direita c/ desconto |
| PFDFow | Number(003,0) | Sim | Parecer Fowler da Orelha Direita |
| PFESDe | Number(007,4) | Sim | Fowler - Percentual de perda da Orelha esquerda s/ desconto |
| PFECDe | Number(007,4) | Sim | Fowler - Percentual de perda da Orelha esquerda c/ desconto |
| PFEFow | Number(003,0) | Sim | Parecer Fowler da Orelha Esquerda |
| PFBSDe | Number(007,4) | Sim | Fowler - Percentual de perda Bilateral s/ desconto |
| PFBCDe | Number(007,4) | Sim | Fowler - Percentual de perda Bilateral c/ desconto |
| PFBFow | Number(003,0) | Sim | Parecer Fowler Bilateral |
| WEB005 | String(002) | Sim | Resultado do Teste de Weber - 500 Hz |
| WEB010 | String(002) | Sim | Resultado do Teste de Weber - 1000 Hz |
| WEB020 | String(002) | Sim | Resultado do Teste de Weber - 2000 Hz |
| WEB040 | String(002) | Sim | Resultado do Teste de Weber - 4000 Hz |
| ObsOto | String(500) | Sim | Observação sobre a otoscopia/meatoscopia |
| ObsLog | String(500) | Sim | Observação sobre a logoaudiometria |
| TSRTOD | String(001) | Sim | Indica se houve teste SRT (orelha direita) |
| TSRTOE | String(001) | Sim | Indica se houve teste SRT (orelha esquerda) |
| TSDTOD | String(001) | Sim | Indica se houve teste SDT (orelha direita) |
| TSDTOE | String(001) | Sim | Indica se houve teste SDT (orelha esquerda) |
| RSDTOD | String(001) | Sim | Indica se houve resposta SDT (orelha direita) |
| RSDTOE | String(001) | Sim | Indica se houve resposta SDT (orelha esquerda) |
| RSRTOD | String(001) | Sim | Indica se houve resposta SRT (orelha direita) |
| RSRTOE | String(001) | Sim | Indica se houve resposta SRT (orelha esquerda) |
| CodCab | Number(003,0) | Sim | Código da Cabine |
| HorAte | Number(005,0) | Sim | Hora do Atendimento |
| ParAud | String(500) | Sim | Parecer Audiológico |
| TipEsq | String(001) | Sim | Tipo Exame Orelha Esquerda |
| ResEsq | String(001) | Sim | Resultado do exame da orelha esquerda (N-Normal/A-Alterado) |
| EvoEsq | String(001) | Sim | Evolução resultado orelha esquerda (E-Estável/A-Agravamento/M-Melhorado) |
| OcuEsq | String(001) | Sim | Situação do resultado da orelha esquerda (O-Ocupacional/N-Não Ocupacional) |
| CodRqu | Number(009,0) | Sim | Código Requisição |
| CodEta | Number(003,0) | Sim | Código Etapa |
| SeqEta | Number(003,0) | Sim | Sequência Etapa |
| ExpExc | String(001) | Sim | Exposição excessiva |
| IntExp | Number(001,0) | Sim | Interpretação exposição conforme Quadro I da NR 7 |
| TPaMOD | String(001) | Sim | Teste de palavras monossílabas OD |
| TPaDOD | String(001) | Sim | Teste de palavras dissílabas OD |
| TPaMOE | String(001) | Sim | Teste de palavras monossílabas OE |
| TPaDOE | String(001) | Sim | Teste de palavras dissílabas OE |
| ConQd3 | String(001) | Sim | Define se deve considerar exame no relatório do Quadro III da NR7 |
| CodIde | String(017) | Sim | Código Identificação do Exame |
| DatCol | Date | Sim | Data de Coleta/Realização do Exame |
| CliCpl | Number(001,0) | Sim | Define se o exame é considerado clínico ou complementar |
| USU_CAE | String(001) | Sim | CAE |
| USU_CodEpi | Number(008,0) | Sim | Codigo EPI |

---

## Chave Primária

- NumEmp
- CodFic
- CodExa
- DatSol

---

## Índices

### R108RESIndice2

**Tipo:** Não unico

Campos:
- NumEmp
- AteAso
- NumAte

### R108RESIndice3

**Tipo:** Não unico

Campos:
- CodFic
- CodRqu
- CodEta
- SeqEta

---

## Relacionamentos

### IR_R108RES_001

**Tabela:** R110FIC

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodFic | CodFic |

### IR_R108RES_002

**Tabela:** R108EXA

| Origem | Destino |
|--------|---------|
| CodExa | CodExa |

### IR_R108RES_007

**Tabela:** R108ORI

| Origem | Destino |
|--------|---------|
| OriExa | OriExa |

