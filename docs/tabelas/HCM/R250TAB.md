# R250TAB

## Descrição

Controle de alterações das tabelas alocadas em memória

---

## Resumo

- Campos: 99
- Chave Primária: 0 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| Tb1Dat | Date | Sim | Tabela 1 - Data da Última Alteração |
| Tb1Hor | Number(005,0) | Sim | Tabela 1 - Hora da Última Alteração |
| Tb2Dat | Date | Sim | Tabela 2 - Data da Última Alteração |
| Tb2Hor | Number(005,0) | Sim | Tabela 2 - Hora da Última Alteração |
| Tb3Dat | Date | Sim | Tabela 3 - Data da Última Alteração |
| Tb3Hor | Number(005,0) | Sim | Tabela 3 - Hora da Última Alteração |
| SrqDat | Date | Sim | Situação Requisição - Última Alteração |
| CEADat | Date | Sim | Conv Exames/Audiômetro |
| OriCan | Date | Sim | Inicializa Origem Candidato |
| CExDat | Date | Sim | Converter Exames |
| ConPpr | Date | Sim | Converter PPRA |
| ConCap | Date | Sim | Converter - Capacidade das Salas |
| ConRec | Number(003,0) | Sim | Controle de conversões módulo Recrutamento |
| ConTre | Number(003,0) | Sim | Controle de conversões módulo Treinamento |
| ConMed | Number(003,0) | Sim | Controle de conversões dos módulos Segurança/Medicina |
| ConIRS | String(001) | Sim | Controle do Início da Conversão do RS |
| ConITR | String(001) | Sim | Controle do Início da Conversão do TR |
| ConISM | String(001) | Sim | Controle do Início da Conversão do SM |
| DatIRS | Date | Sim | Data de Início Conversão RS |
| DatITR | Date | Sim | Data de Início Conversão TR |
| DatISM | Date | Sim | Data de Início Conversão SM |
| HorIRS | Number(005,0) | Sim | Hora de Início da Conversão RS |
| HorITR | Number(005,0) | Sim | Hora de Início da Conversão TR |
| HorISM | Number(005,0) | Sim | Hora de Início da Conversão SM |
| ConRub | Number(003,0) | Sim | Conversão Rubi |
| ConCar | Number(003,0) | Sim | Controle de conversões módulo CS |
| ConJur | Number(003,0) | Sim | Controle de conversões módulo JR |
| ConQua | Number(003,0) | Sim | Controle de conversões módulo QL |
| ConICS | String(001) | Sim | Controle do Início da Conversão do CS |
| ConIQL | String(001) | Sim | Controle do Início da Conversão do QL |
| ConIJR | String(001) | Sim | Controle do Início da Conversão do JR |
| DatICS | Date | Sim | Data de Início Conversão CS |
| DatIQL | Date | Sim | Data de Início Conversão QL |
| DatIJR | Date | Sim | Data de Início Conversão JR |
| HorICS | Number(005,0) | Sim | Hora de Início da Conversão CS |
| HorIQL | Number(005,0) | Sim | Hora de Início da Conversão QL |
| HorIJR | Number(005,0) | Sim | Hora de Início da Conversão JR |
| DatIRO | Date | Sim | Data de Início Conversão RONDA |
| HorIRO | Number(005,0) | Sim | Hora de Início da Conversão RONDA |
| ConIRO | String(001) | Sim | Controle do Início da Conversão do RONDA |
| ConRON | Number(003,0) | Sim | Controle de conversões módulo RONDA |
| UsoDat | Date | Sim | Uso Marcação - Data da Última Alteração |
| UsoHor | Number(005,0) | Sim | Uso Marcação - Hora da Última Alteração |
| ConM32 | Number(003,0) | Sim | Controle de conversões dos módulos Segurança/Medicina p/ 532 |
| ConIVT | String(001) | Sim | Controle do início da conversão do Vetorh |
| DatIVT | Date | Sim | Data de início conversão Vetorh |
| HorIVT | Number(005,0) | Sim | Hora de início da conversão Vetorh |
| ConVet | Number(003,0) | Sim | Controle de conversões do Vetorh |
| CntMan | String(001) | Sim | Controle de Manutenções de Veículos |
| CntAgm | String(001) | Sim | Controle de Agendamento Manutenções Veículos |
| ConAce | Number(003,0) | Sim | Controle de conversões do módulo de Acesso e Segurança |
| ConIAc | String(001) | Sim | Controle do Início da Conversão Acesso |
| DatIAc | Date | Sim | Data de Início Conversão Acesso |
| HorIAc | Number(005,0) | Sim | Hora de Início da Conversão Acesso |
| ConIMO | String(001) | Sim | Controle do início da conversão dos módulos (s/ Rubi) |
| DatIMO | Date | Sim | Data de início de conversão dos módulos (s/ Rubi) |
| HorIMO | Number(005,0) | Sim | Hora de início da conversão dos módulos (s/ Rubi) |
| ConMod | Number(003,0) | Sim | Controle de conversões dos módulos (s/ Rubi) |
| CodCal | Number(005,0) | Sim | Código de Cálculo Ativo para Kit Benefício (BS) |
| ForVal | Number(002,0) | Sim | Empresa Fornecedora de Vales |
| IniPer | Date | Sim | Período Inicial |
| FimPer | Date | Sim | Período Final |
| EmpAtu | Number(004,0) | Sim | Código da Empresa Atual |
| CalPrv | Number(004,0) | Sim | Cálculo Ativo na Provisão |
| EmpPrv | Number(004,0) | Sim | Definir Empresa Provisionada |
| UtiPsq | String(001) | Sim | Utiliza módulo pesquisa |
| DatVrp | Date | Sim | Data Verificação Validade da Proprietária |
| CodPas | Number(004,0) | Sim | Código do passo (Atualizador) |
| DesPas | String(999) | Sim | Descrição do passo (Atualizador) |
| BuiPas | Number(004,0) | Sim | Versão de origem(Atualizador) |
| OriPas | String(009) | Sim | Versão de origem do tbs(Atualização) |
| DATAMB | Date | Sim | Ambiente - Data da Última Alteração |
| HORAMB | Number(005,0) | Sim | Ambiente - Hora da Última Alteração |
| DatPBS | Date | Sim | Data Verificação Estouro Proprietária - BS |
| DatPCS | Date | Sim | Data Verificação Estouro Proprietária - CS |
| DatPJR | Date | Sim | Data Verificação Estouro Proprietária - JR |
| DatPPL | Date | Sim | Data Verificação Estouro Proprietária - PLR |
| DatPQL | Date | Sim | Data Verificação Estouro Proprietária - QL |
| DatPHR | Date | Sim | Data Verificação Estouro Proprietária - Ronda |
| DatPRS | Date | Sim | Data Verificação Estouro Proprietária - RS |
| DatPFP | Date | Sim | Data Verificação Estouro Proprietária - Rubi |
| DatPSM | Date | Sim | Data Verificação Estouro Proprietária - SM |
| DatPTR | Date | Sim | Data Verificação Estouro Proprietária - TR |
| IniVtr | Date | Sim | Inicio Apuração Vale Transporte |
| FimVtr | Date | Sim | Fim Apuração Vale Transporte |
| SibDat | Date | Sim | Data de Alteração das Tabelas de Símbolos |
| SibHor | Number(005,0) | Sim | Hora de Alteração das Tabelas de Símbolos |
| CodCli | Number(009,0) | Sim | Código do Cliente na Proprietária |
| PerRef | Date | Sim | Competência Ativa |
| DatPCP | Date | Sim | Data Verificação Estouro Proprietária - CP |
| DesVtr | String(001) | Sim | Desconta VT Folha Pagamento |
| IniFvt | Date | Sim | Inicio Faltas Vale Transporte |
| FimFvt | Date | Sim | Fim Faltas Vale Transporte |
| RotPCo | String(254) | Sim | Controle provisão e contabilização |
| CorDat | Date | Sim | Data de Corte |
| TbsPen | String(030) | Sim | Versão do TBS para Consulta Web de Leiautes do eSocial |
| PprLoc | String(255) | Sim | Controle PPRA por Local |
| LogMon | String(030) | Sim | Versão do TBS para Log de Monitoramento |
| LimILP | String(001) | Sim | Terminou Limpeza Inicial da R067LPR |

---

## Chave Primária

Não possui.

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
