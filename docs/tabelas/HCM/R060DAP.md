# R060DAP

## Descrição

Definições Gerais da Apuração

---

## Resumo

- Campos: 79
- Chave Primária: 1 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodDAp | Number(002,0) | Não | Código da Definição da Apuração |
| DesDAp | String(040) | Sim | Descrição da Definição de Apuração |
| RgrIAp | Number(003,0) | Sim | Regra Início do Cálculo Apuração |
| RgrEli | Number(003,0) | Sim | Regra para Eliminar Marcações no Cálculo |
| RgrApu | Number(003,0) | Sim | Regra de Apuração |
| RgrCon | Number(003,0) | Sim | Regra Consistência de Acertos |
| RgrExt | Number(003,0) | Sim | Regra de Aprovação das Programações de Horas Extras |
| RgrRef | Number(003,0) | Sim | Regra de Cálculo de Refeitório |
| SepJoN | Number(010,0) | Sim | Separação Jornada Dia Normal |
| ConInt | Number(001,0) | Sim | Considerar Intervalo Entre Marcações |
| IntMar | Number(002,0) | Sim | Intervalo Entre Marcações de Ponto |
| LimMar | Number(001,0) | Sim | Limite de Marcações |
| MarSPr | String(001) | Sim | Considerar p/ Ponto Marcações Relizadas em Coletores sem Permissão |
| UsaMpN | String(001) | Sim | Considerar Marcações Pares Dias Normais |
| UsaMpF | String(001) | Sim | Considerar Marcações Pares Dias de Folga |
| PrgFer | String(001) | Sim | Programação Sobrepõe Feriado |
| IntRef | String(001) | Sim | Desprezar Intermediárias nos Períodos de Refeição |
| UsaHFo | String(001) | Sim | Utilizar Horário na Folga |
| ArqMod | String(011) | Sim | Nome do Modelo do Relatório a Ser Emitido Após Leitura |
| UsaDir | String(001) | Sim | Utilizar Direção da Marcação para Alocação |
| PrgRet | Number(002,0) | Sim | Limite de Dias para Programações Retroativas |
| CalCNo | Number(001,0) | Sim | Cálculo da Conversão das Horas Noturnas |
| THrDFo | String(001) | Sim | Considerar Troca de Horário para Projeção em Dias de Folga |
| PonDFo | String(001) | Sim | Considerar Pontes para Projeção em Dias de Folga |
| ObrDtF | String(001) | Sim | Obrigar a Digitação da Data Final nas Programações |
| ApmAlt | String(001) | Sim | Permitir Gravar Marcações sem Apurar na tela de Acertos. |
| UtiRgm | String(001) | Sim | Utiliza Rotina de Regularização de Marcações |
| ModEsp | String(011) | Sim | Modelo Para Ícone de Cartão Ponto |
| UtiSol | Number(001,0) | Sim | Utiliza Rotina de Solicitação de Horas Extras. |
| PrgSsl | String(001) | Sim | Permite Cadastrar Programação de H. Extra sem Solicitação. |
| TipELm | Number(001,0) | Sim | Tipo para Eliminar Marcações |
| ModRAc | String(011) | Sim | Modelo de Relatório para Tela de Acerto |
| SitDem | Number(003,0) | Sim | Situação de Demissão |
| PonSob | String(001) | Sim | Indica se a Ponte Sobrepõe a Troca de Horário |
| MThGer | String(001) | Sim | Mostra Menu Troca de Horário em Gerenciar Horários |
| JusMar | String(001) | Sim | Justificar Marcações Digitadas na Tela de Acertos |
| MarAle | String(001) | Sim | Marcações Geradas Aleatoriamente |
| ConVer | Number(001,0) | Sim | Controle de Dias Verificados |
| ExcPto | String(001) | Sim | Controlar Exclusão do Ponto |
| MotAce | String(001) | Sim | Controlar Motivos de Acerto |
| RecAut | String(001) | Sim | Recálculo Automático em Programações/Afastamentos |
| AlFCol | Number(003,0) | Sim | Altura Frame Colaboradores |
| AlFAux | Number(003,0) | Sim | Altura Frame Auxiliar |
| UtFAux | String(001) | Sim | Utiliza Frame Auxiliar |
| MCoExc | String(001) | Sim | Mostra Todos Colaboradores no Somente Exceções |
| CMaEle | String(010) | Sim | Cor Marcação Eletrônica |
| CMaDig | String(010) | Sim | Cor Marcação Digitada |
| CMaGer | String(010) | Sim | Cor Marcação Gerada |
| CMaReg | String(010) | Sim | Cor Marcação Regularizada |
| RgrIns | Number(003,0) | Sim | Regra para Inserir Marcações no Cálculo |
| OBtPes | String(001) | Sim | Ocultar Botão de Pesquisa |
| MUsuAl | String(001) | Sim | Mostra nos Acertos na Data o Último Usuário que Alterou Situação Apurada |
| ConDMa | String(001) | Sim | Considerar Direção pela Ordem de Marcações |
| RgrAGA | Number(003,0) | Sim | Regra Após Gravar Apuração do Colaborador |
| RgrICC | Number(003,0) | Sim | Regra Início Cálculo Colaborador |
| ObsMot | String(001) | Sim | Observação Motivo |
| RelPor | String(011) | Sim | Nome do Modelo do Relatório de Arquivo de Fonte de Dados Tratado |
| RgrGAc | Number(003,0) | Sim | Regra Após Gravar os Acertos |
| MosApu | String(001) | Sim | Habilitar o Botão Apurar na Tela de Acertos |
| MosApuGrav | String(001) | Sim | Habilitar o Botão Apu/Grav na Tela de Acertos |
| DiaRet | Number(002,0) | Sim | Dias para Retornar |
| MtAObs | String(001) | Sim | Sugerir Motivo de Acerto na Observação |
| TBtDia | Number(001,0) | Sim | Tratamento de Tolerâncias por Batida e por Dia |
| Rg6AGA | String(099) | Sim | Regra Após Gravar Apuração do Colaborador |
| Rg6Apu | String(099) | Sim | Regra de Apuração |
| Rg6Con | String(099) | Sim | Regra Consistência de Acertos |
| Rg6Eli | String(099) | Sim | Regra para Eliminar Marcações no Cálculo |
| Rg6ICA | String(099) | Sim | Regra Inicio do Cálculo de Apuração |
| Rg6ICC | String(099) | Sim | Regra de Início do Cálculo do Colaborador |
| Rg6GAC | String(099) | Sim | Regra Após Gravar os Acertos |
| AltPon | String(001) | Sim | Permitir alterar ponto antes da transferência de filial |
| SobApu | String(001) | Sim | Calcular sobreaviso pela apuração |
| DeTSob | String(001) | Sim | Permite descontar horas trabalhadas do sobreaviso |
| AceRet | String(001) | Sim | Acerto Retroativo |
| ApuJin | String(001) | Sim | Apurar jornada incompleta |
| SitJin | Number(003,0) | Sim | Situação para jornada incompleta |
| ApuEsp | String(001) | Sim | Complementar trabalho com cálculo de espera |
| QDRAce | Number(002,0) | Sim | Quantidade de dias para realizar acertos |
| CalFFR | String(001) | Sim | Calcular faltas no feriado em escala de revezamento |

---

## Chave Primária

- CodDAp

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
