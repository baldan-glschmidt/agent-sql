# R010SIT

## Descrição

Situações

---

## Resumo

- Campos: 59
- Chave Primária: 1 campo(s)
- Índices: 3
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodSit | Number(003,0) | Não | Código da Situação |
| DesSit | String(030) | Sim | Descrição da Situação |
| DesAbr | String(004) | Sim | Descrição Abreviatura Situação |
| SitCmp | Number(003,0) | Sim | Situação Complementar |
| TipSit | Number(002,0) | Sim | Tipo da Situação |
| SitDJu | Number(003,0) | Sim | Situação para os Dias Justificados |
| LetHor | String(003) | Sim | Letra Característica de Horas |
| DesRai | String(001) | Sim | Situação Válida p/ Rais |
| TpoSer | String(001) | Sim | Tempo de Serviço |
| TpoSeA | String(001) | Sim | Tempo de Serviço Anuidade |
| DecTer | String(001) | Sim | Paga 13° Salário |
| DscFer | String(001) | Sim | Perde o Direito ao Período Aquisitivo de Férias |
| PerFer | String(001) | Sim | Tratamento das Faltas para Redução do Direito de Férias |
| PerVtr | String(001) | Sim | Perde Vale Transporte |
| PerDih | String(001) | Sim | Perde Dia Horista |
| PerDim | String(001) | Sim | Perde Dia Mensalista |
| PerDsr | String(001) | Sim | Perde DSR |
| PerFed | String(001) | Sim | Perde Feriado |
| IgnMar | String(001) | Sim | Ignorar Marcações |
| ConNot | String(001) | Sim | Converte Noturnas |
| ConNPr | String(001) | Sim | Converte Noturnas Prorrogadas |
| SitExc | String(001) | Sim | Situação de Exceção |
| PerAdt | String(001) | Sim | Perde Adt Salarial |
| BloAce | String(001) | Sim | Bloquear Acesso |
| ExcBnf | String(001) | Sim | Bloqueia Benefício |
| BloBnf | String(001) | Sim | Desconsiderar Envio Coletor Benefício |
| IncAbs | Number(001,0) | Sim | Incide no Cálculo do Absenteísmo (PPR) |
| IncOci | String(001) | Sim | Incide no Cálculo do Ócio (PPR) |
| PerLic | String(001) | Sim | Perde Licença Especial |
| PerAsd | String(001) | Sim | Perde Assiduidade (S,N) |
| PerPlr | String(001) | Sim | Perde Participação nos Lucros e Resultados (S,N) |
| ExmRet | String(001) | Sim | Default do Exame de Retorno para Histórico Afastamento |
| AfaQua | String(001) | Sim | Considera Afastados Quadro (S,N) |
| CarQua | Number(003,0) | Sim | Define a carência para o afastamento liberar vaga do quadro |
| GerEst | String(001) | Sim | Gerar Estabilidade |
| DiaEst | Number(004,0) | Sim | Dias Estabilidade |
| CodEtb | Number(002,0) | Sim | Código da Estabilidade |
| PerTra | String(001) | Sim | Perde Valor Trajeto |
| NumMax | Number(004,0) | Sim | Máximo Dias Estabilidade |
| PerApo | String(001) | Sim | Perde Aposentadoria |
| PrrBHr | String(001) | Sim | Prorrogar Banco de Horas nos Afastamento |
| MotObr | String(001) | Sim | Motivo de Acerto Obrigatório (S,N) |
| ConPro | String(001) | Sim | Indica se poderá haver prorrogação no afastamento (S,N) |
| PerGra | String(001) | Sim | Indicar se esta situação ocasiona perda da gratificação |
| SitSij | Number(002,0) | Sim | Indica qual é a situação referente ao SIJP |
| CodSin | Number(002,0) | Sim | Utilizado nos casos de acidente de trabalho |
| PerAco | String(001) | Sim | Define se permite registro de acompanhamento médico |
| FicReg | String(001) | Sim | Define a Situação de Afastamento na Ficha Registro |
| DiaBlq | Number(001,0) | Sim | Número de dias, após a data de demissão,  que o crachá será bloqueado |
| DsrPro | String(001) | Sim | Calcula DSR do Professor |
| MSitWF | String(001) | Sim | Situação para Workflow |
| SitDiu | String(001) | Sim | Situação é Diurna (sim) ou Noturna (não) |
| CorSit | String(010) | Sim | Cor para a Situação |
| ArrNot | String(001) | Sim | Arredonda Horas Convertidas para Noturnas |
| ParTre | String(001) | Sim | Indica se colaborador nesta situação pode participar de treinamento |
| DesCts | Number(001,0) | Sim | Descontar Contribuição Sindical |
| ProSin | String(001) | Sim | Perde Provento Sindical |
| ConAbs | Number(001,0) | Sim | Considera para o Cálculo do Absenteísmo |
| ObrAne | String(001) | Sim | Obrigar anexo no afastamento |

---

## Chave Primária

- CodSit

---

## Índices

### R010SITIndice2

**Tipo:** Não unico

Campos:
- DesSit

### R010SITIndice3

**Tipo:** Não unico

Campos:
- TipSit
- CodSit

### R010SITIndice4

**Tipo:** Não unico

Campos:
- SitCmp

---

## Relacionamentos

Nenhum relacionamento cadastrado.
