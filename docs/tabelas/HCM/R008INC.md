# R008INC

## Descrição

Eventos - Incidências

---

## Resumo

- Campos: 47
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodTab | Number(003,0) | Não | Código da Tabela Eventos |
| CodEve | Number(004,0) | Não | Código do Evento |
| CmpInc | Date | Não | Data de Alteração das Incidências |
| SeqInc | Number(002,0) | Não | Sequência |
| IncRem | String(001) | Sim | Incide p/ Remuneração |
| IncMvv | String(001) | Sim | Incide p/ Média de Valores Variáveis |
| IncAd1 | String(001) | Sim | Incide p/ Média Adicionais 1 |
| IncAd2 | String(001) | Sim | Incide p/ Média Adicionais 2 |
| IncFgm | String(001) | Sim | Incide p/ Fgts Mensal |
| IncFgd | String(001) | Sim | Incide p/ FGTS 13° Salário |
| IncInm | String(001) | Sim | Incide p/ INSS Mensal |
| IncInd | String(001) | Sim | Incide p/ INSS 13° Salário |
| IncIna | String(001) | Sim | Incide p/ INSS Acordos Internacionais de Previdência Social |
| IncIrm | String(001) | Sim | Incide p/ IRRF Mensal |
| IncIrf | String(001) | Sim | Incide p/ IRRF Férias |
| IncIrd | String(001) | Sim | Incide p/ IRRF 13° Salário |
| IncIrp | String(001) | Sim | Incide p/ IRRF Participação nos Lucros |
| IncIra | String(001) | Sim | Incide p/ IRRF Acordos Internacionais de Previdência Social |
| IncIpm | String(001) | Sim | Incide p/ IPE Mensal |
| IncIpf | String(001) | Sim | Incide p/ IPE Férias |
| IncIpd | String(001) | Sim | Incide p/ IPE 13° Salário |
| IncPis | String(001) | Sim | Incide p/ PIS Mensal |
| IncPid | String(001) | Sim | Incide p/ PIS 13º Salário |
| IncRer | String(001) | Sim | Incide p/ Remuneração Rais |
| IncMsc | String(001) | Sim | Incide p/ Média Salário Contratual Rais |
| AbrVin | String(100) | Sim | Abrangência de Vínculo |
| ConMed | String(001) | Sim | Considera p/ Médias (S/N) |
| ComSal | String(001) | Sim | Evento faz parte da Composição Salarial |
| MotMai | Number(003,0) | Sim | Motivo Maior |
| MotMen | Number(003,0) | Sim | Motivo Menor |
| MotZer | Number(003,0) | Sim | Motivo Cancelamento |
| NatRub | Number(004,0) | Sim | Código de classificação da rubrica |
| RepDSR | String(001) | Sim | Indica se a rubrica repercute no cálculo do Descanso Semanal Remunerado |
| RepRcs | String(001) | Sim | Indica se a rubrica repercute no cálculo do aviso prévio |
| Rep13s | String(001) | Sim | Indica se a rubrica repercute no cálculo do 13º Salário |
| RepFer | String(001) | Sim | Indica se a rubrica repercute no cálculo das Férias |
| IncSin | String(001) | Sim | Incide p/ contribuição sindical |
| RegIpe | Number(001,0) | Sim | Regime Próprio (IPE) |
| IncINS | Number(002,0) | Sim | Incidência tributária da rubrica para a Previdência Social |
| IncIRR | Number(004,0) | Sim | Incidência tributária da rubrica para o IRRF |
| IncFGT | Number(002,0) | Sim | Incidência tributária da rubrica para o FGTS |
| IncMat | String(001) | Sim | Incide p/ Maternidade Intermitente |
| IncAPIN | String(001) | Sim | Incide p/ Aviso Prévio Indenizado Intermitente |
| TetRem | String(001) | Sim | Informar se a rubrica compõe o teto remuneratório específico (art. 37, XI, da CF/1988) |
| IncFgi | String(001) | Sim | Incide p/ FGTS Indenizado |
| IncFdi | String(001) | Sim | Incide p/ FGTS 13° Salário Indenizado |
| IncCrt | String(001) | Sim | Incide p/ Composição Crédito Trabalhador |

---

## Chave Primária

- CodTab
- CodEve
- CmpInc
- SeqInc

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R008INC_001

**Tabela:** R008EVC

| Origem | Destino |
|--------|---------|
| CodTab | CodTab |
| CodEve | CodEve |

