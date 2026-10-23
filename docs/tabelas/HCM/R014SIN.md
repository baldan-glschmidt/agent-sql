# R014SIN

## Descrição

Sindicatos

---

## Resumo

- Campos: 132
- Chave Primária: 1 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodSin | Number(004,0) | Não | Código do Sindicato |
| NomSin | String(100) | Sim | Nome do Sindicato |
| TabEst | Number(004,0) | Sim | Define a qual estrutura pertence o Sindicato |
| SigSin | String(015) | Sim | Sigla do Sindicato |
| MesDis | Number(002,0) | Sim | Mês Data Base Sindicato |
| TfePro | String(001) | Sim | Tipo Férias Proporcionais na Rescisão |
| FerPro | Number(002,0) | Sim | Dias ou Meses de Férias Proporcionais |
| CodIdm | Number(003,0) | Sim | Código Tabela de Índices |
| DiaInd | Number(002,0) | Sim | Dia Índice de Correção |
| IndNeg | String(001) | Sim | Considerar Índice Negativo na Correção dos Valores p/ Médias |
| Tip13s | String(001) | Sim | Tipo Adto 13° Salário (U,D) |
| Mes13s | Number(002,0) | Sim | Mês Adto 13° Salário |
| Per13s | Number(002,0) | Sim | Percentual 13° Salário |
| ComMes | String(001) | Sim | Usar Comissões do Mês (S,N) |
| Mes15d | String(001) | Sim | Considerar Meses com Menos de 15 Dias no Cálculo de Médias |
| MesZer | String(001) | Sim | Considerar meses s/ valores p/ médias (S,N) |
| DivFix | String(001) | Sim | Divisor Fixo p/ Médias |
| MhePer | String(001) | Sim | Média de horas extras de férias do período aquisitivo (S,N) |
| MvvPer | String(001) | Sim | Média de valores variáveis de férias do período aquisitivo (S,N) |
| FerDem | String(001) | Sim | Pagar 1/3 Férias Ped.Demissão |
| AdiFer | Number(004,2) | Sim | Percentual Acres.(1/3) Férias |
| MesPfe | Number(002,0) | Sim | Meses do Período Aquisitivo de Férias |
| DaxDoe | Number(003,0) | Sim | Máximo Dias de Auxílio-Doença e Acidente Trabalho no Período |
| DliRem | Number(003,0) | Sim | Máximo Dias Licença Remunerada no Período |
| AdmMen | String(001) | Sim | 30 Dias Adm.Mensalistas (S,N) |
| TipDsr | Number(001,0) | Sim | Cálculo DSR Horas Extras |
| DiaRea | Number(003,0) | Sim | Dias Aviso Reavido |
| IniNot | Number(005,0) | Sim | Início Horas Noturnas |
| FimNot | Number(005,0) | Sim | Fim Horas Noturnas |
| AdiNot | Number(005,3) | Sim | Perc. Adic. Noturno |
| PerAdi | Number(005,2) | Sim | Perc. Adto. Salarial |
| SomRea | String(001) | Sim | Somar Dias Aviso Reavido ao Direito das Indenizações |
| Adm13s | String(001) | Sim | Adm.no Ano - Projetar Adto 13° Salário Até Dezembro (S,N) |
| M13Ano | String(001) | Sim | Médias 13° Salário - limitar ao ano |
| DirFer | String(001) | Sim | Avos de Férias |
| GerHor | String(001) | Sim | Geração Horistas |
| FgtCpd | Number(004,2) | Sim | % Fgts dos Colaboradores c/ Prazo Determinado |
| VenGrr | Number(002,0) | Sim | Dias para o Vencimento da GRFP Aviso Trabalhado |
| VenGri | Number(002,0) | Sim | Dias para o Vencimento da GRFP Aviso Indenizado |
| CodEnt | Number(012,0) | Sim | Código da Entidade Sindical |
| NumCgc | Number(015,0) | Sim | Número do CNPJ Sindicato |
| CfjCgc | String(014) | Sim | Número do CNPJ Sindicato |
| IndCor | Number(003,0) | Sim | Índice da Correção Monetária |
| IndCtr | Number(003,0) | Sim | Índice da Base de Contribuição |
| CobAdi | String(001) | Sim | Cobrar Adicional Multa |
| CobJur | String(001) | Sim | Cobrar Juros de Mora |
| UsaCor | String(001) | Sim | Usar Correção Juros/Multa |
| EndRua | String(040) | Sim | Endereço |
| EndNum | String(006) | Sim | Número Endereço |
| EndCpl | String(025) | Sim | Complemento Endereço |
| CodCid | Number(007,0) | Sim | Código da Cidade do Sindicato |
| CodBai | Number(004,0) | Sim | Código do Bairro do Sindicato |
| EndCep | Number(008,0) | Sim | Código do Cep |
| TipArr | String(001) | Sim | Tipo de Arredondamento |
| CasHor | Number(001,0) | Sim | Número de Casas Decimais do Salário dos Horistas e dos Tarefeiros |
| AltDir | String(001) | Sim | Mudou Direito de Férias |
| NomArq | String(250) | Sim | Arquivo |
| AdtFer | String(001) | Sim | Adiantamento de Férias na Folha |
| CodDSi | Number(003,0) | Sim | Código da Definição das Situações da Apuração |
| PerPer | String(001) | Sim | Periculosidade de férias do período aquisitivo (S,N) |
| InsPer | String(001) | Sim | Insalubridade de férias do período aquisitivo (S,N) |
| AdiPer | String(001) | Sim | Adicionais 1 e 2 de férias do período aquisitivo (S,N) |
| RegPer | String(001) | Sim | Regras 36, 38, 41 e 90 de férias do período aquisitivo (S,N) |
| NotPer | String(001) | Sim | Adicional noturno de férias do período aquisitivo (S,N) |
| VanRcs | Number(001,0) | Sim | Considerar Vantagens para Cálculo do Estouro na Rescisão |
| DesFer | Number(001,0) | Sim | Dias Desconsiderados Férias |
| CodBan | Number(004,0) | Sim | Código do Banco |
| CodAge | Number(005,0) | Sim | Código da Agência |
| ConBan | Number(012,0) | Sim | Conta Bancária |
| DigBan | String(003) | Sim | Dígito da Conta Bancário |
| ProNEx | String(001) | Sim | Considera Prorrogação de Noturno para Extras |
| ProNTr | String(001) | Sim | Considera Prorrogação de Noturno para Trabalho |
| HorNPr | Number(005,0) | Sim | Quantidade de Horas Mínimas Realizadas no Noturno para Considerar Prorrogação |
| GraInt | String(001) | Sim | Determina se a gratificação será paga na folha ou em cálculo específico |
| TipGra | Number(001,0) | Sim | Tipo da remuneração para o cálculo da gratificação |
| PerGra | Number(002,0) | Sim | Período entre o pagamento de uma gratificação e a próxima |
| RefGra | Number(005,2) | Sim | Percentual referente a cada um dos pagamentos |
| GerMen | Number(001,0) | Sim | Define como será a geração de horas para mensalistas |
| DiaGoz | Number(002,0) | Sim | Qtde de dias de gozo de férias para o pagto do adicional |
| MaxUte | Number(002,0) | Sim | Máximo de dias úteis gozados nas férias |
| CriTrb | Number(001,0) | Sim | Determina a relação entre trabalho e direito proporcional de férias |
| QtdTrb | Number(005,2) | Sim | Quantidade mínima trabalhada para ter direito de férias |
| CriFer | Number(001,0) | Sim | Critério para definir a unidade de cálculo do direito de férias |
| QtdFer | Number(005,2) | Sim | Quantidade de férias para cada unidade de tempo trabalhada |
| CntPer | Number(001,0) | Sim | Determina como será a contagem do período de férias |
| DurPer | Number(004,0) | Sim | Duração do período de férias de acordo com a contagem |
| CntFer | Number(001,0) | Sim | Define como será a contagem dos dias de férias |
| MesRcs | String(001) | Sim | Considera Mês Rescisão (S,N) |
| CodObr | Number(006,0) | Sim | Código da Obra Social |
| ExtIni | String(001) | Sim | Considera Horas Extras no Início da Jornada |
| MinHDe | Number(005,0) | Sim | Tempo de Descanso para Interromper Prorrogação Noturna |
| GerDsr | Number(001,0) | Sim | Definir a geração do DSR dos colaboradores |
| DiaFev | Number(001,0) | Sim | Define como é o direito ao avo de Fevereiro |
| ConFra | Number(001,0) | Sim | Consistência do Fracionamento/Dias Mínimo Férias |
| ConFer | String(001) | Sim | Consistir Início de Férias dois dias antes de DSR ou Feriado |
| FraPer | Number(002,0) | Sim | Quantidade máxima de recibos que podem ser emitidos para um período de férias. |
| MinRec | Number(002,0) | Sim | Quantidade mínima de dias em um recibo de férias |
| IntAbo | Number(001,0) | Sim | Integração Abono Pecuniário |
| DiaAvi | Number(003,0) | Sim | Dias Aviso Indenizado |
| SelIda | String(001) | Sim | Seleção por Idade |
| SelSer | String(001) | Sim | Seleção por Tempo Serviço |
| DiaAnd | Number(002,0) | Sim | Dias Ind.Mês Ant.Dissídio |
| DsrCom | Number(001,0) | Sim | DSR Comissões |
| Med13s | Number(001,0) | Sim | Média 13°  Salário Integral |
| For13s | Number(001,0) | Sim | Cálculo Médias 13° Salário |
| ForFer | Number(001,0) | Sim | Cálculo Médias Férias |
| ForAvi | Number(001,0) | Sim | Cálculo Médias Aviso Prévio |
| PagDsi | String(001) | Sim | Indenização Mês Anterior ao Dissídio |
| ProAmd | String(001) | Sim | Projetar Afastamento Multa Dobro |
| DesMul | Number(001,0) | Sim | Contabilizar dias desconsiderados nas férias para gerar a multa em dobro |
| Avo13a | Number(001,0) | Sim | Avos Adto. 13° Salário Adm. Ano |
| Afa13s | Number(001,0) | Sim | Afastamento Adto. 13° Salário |
| DatAvi | Date | Sim | Data da Última Alteração do Aviso Prévio |
| PagAEx | Number(001,0) | Sim | Pagar Adicional de Extras em Horário 12 Horas |
| MaxFal | Number(005,0) | Sim | Máximo Faltas para Horário 12 horas |
| TipHom | Number(001,0) | Sim | Tipo para homologação (Obsoleto) |
| QtdHom | Number(003,0) | Sim | Qtde. para Homologação (Obsoleto) |
| QtdMul | Number(002,0) | Sim | Quantidade Período Vencido Multa |
| EntAlf | String(020) | Sim | Código da Entidade Sindical Alfanumérico |
| CalDif | Number(001,0) | Sim | Apuração Recálculo das Médias |
| PgMDsr | String(001) | Sim | Pagar multa por trabalho no DSR |
| InMiJE | Number(005,0) | Sim | Intervalo mínimo para jornada entre 4 e 6 horas |
| InMiJA | Number(005,0) | Sim | Intervalo mínimo para jornada acima de 6 horas |
| TeMaJD | Number(005,0) | Sim | Tempo máximo de jornada diária |
| TeMaDC | Number(005,0) | Sim | Tempo máximo de direção contínua |
| TMiDeC | Number(005,0) | Sim | Tempo mínimo de descanso contínuo |
| PeFrRD | String(001) | Sim | Permite fracionar repouso diário |
| CaReSe | String(001) | Sim | Calcular repouso semanal |
| TpcPix | Number(002,0) | Sim | Tipo de Chave Pix - Pagamento Instantâneo |
| ChvPix | String(100) | Sim | Chave Pix - Pagamento Instantâneo |
| InMiTr | Number(005,0) | Sim | Intervalo mínimo Trabalho para jornada acima de 6 horas |
| TmpInt | Number(005,0) | Sim | Duração Intervalo Interjornada |

---

## Chave Primária

- CodSin

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
