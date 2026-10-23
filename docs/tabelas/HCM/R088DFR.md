# R088DFR

## Descrição

Definições Frota

---

## Resumo

- Campos: 56
- Chave Primária: 0 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| MaxPon | Number(002,0) | Sim | Número Máximo de Pontos na Carteira para Conduzir Veículo |
| PerCon | String(001) | Sim | Utiliza Condutor que Excedeu Número Máximo de Pontos Carteira (Infrações) |
| EnvEma | String(001) | Sim | Enviar E-mail para Chefia quando Condutor Irregular |
| EmaChe | String(100) | Sim | E-mail da Chefia do Condutor Irregular |
| FroOnl | String(001) | Sim | Controle de veículos on-line |
| UsaAge | String(001) | Sim | Permite Saída de Veículos sem Agendamento (S/N) |
| ConCon | String(001) | Sim | Utiliza controle de condutores de veículos (S/N) |
| ObrAut | String(001) | Sim | Utiliza Autorizador para Movimentação de Veículos |
| UsaPan | String(001) | Sim | Utiliza Painel Eletrônico na Movimentação de Veículos |
| UtiAgm | String(001) | Sim | Utiliza Agendamento Automático na Manutenção |
| UtiLis | String(001) | Sim | Utiliza Controle de Check-List para Manutenção |
| LibVei | Number(001,0) | Sim | Liberar Saída de Veículo da Frota (Controle On-line) |
| UsuOnl | String(001) | Sim | Utiliza Controle de Usuários On Line |
| VisTsi | String(001) | Sim | Registra Crachá do Visitante e do Veículo na Tabela da Telemática (CONTVEI) |
| ModPrt | String(011) | Sim | Nome do Modelo para  Impressão do Prontuário de Veículos |
| ModExp | String(011) | Sim | Nome do Modelo para Exportação de Despesas de Veículos |
| UsuSap | String(001) | Sim | Utiliza Exportação de Despesas para Sistema ERP da Senior |
| QtdMes | Number(003,0) | Sim | Previsão em Meses Para Troca de Veículo da Frota |
| DiaNfs | Number(003,0) | Sim | Quantidade de Dias de Validade da Nota Fiscal |
| UsaPS2 | String(001) | Sim | Utiliza leitoras com conector PS2 |
| NomSrv | String(020) | Sim | Nome do Servidor para Integração com ERP |
| DirVrt | String(020) | Sim | Diretório Virtual |
| NomUsr | String(020) | Sim | Nome do Usuário para Conexão com o Servidor ERP |
| SenUsr | String(020) | Sim | Senha do Usuário para Conexão com o Servidor ERP |
| BasSrv | String(020) | Sim | Base do Servidor para a Integração com o ERP |
| PrmSap | String(100) | Sim | Parâmetros de Conexão com o ERP |
| ModPvt | String(011) | Sim | Modelo p/ Impressão de Programações de Veículos de Testes |
| ModPtx | String(011) | Sim | Modelo p/ Impressão de Solicitação de Táxi |
| ModVcd | String(011) | Sim | Modelo p/ Impressão de Movimentação de Carga e Descarga |
| DspAba | Number(004,0) | Sim | Código Padrão da Despesas de Abastecimento |
| DspMan | Number(004,0) | Sim | Código Padrão de Despesas de Manutenção |
| DspInf | Number(004,0) | Sim | Código Padrão de Despesas de Infrações |
| IntPnd | Number(004,0) | Sim | Intervalo Envio Email Pendência Manutenção (Em minutos) |
| UsaLib | String(001) | Sim | Utiliza Liberação para Carga e Descarga |
| EmaMan | String(100) | Sim | E-mail do Responsável pela Gestão de Manutenção |
| HorSol | Number(005,0) | Sim | Qtde Máxima de Horas para a Validade de Solicitação de Veículo |
| EdiArt | String(006) | Sim | Edição do Código de Infração |
| ModBil | String(011) | Sim | Modelo para Impressão de Bilhete de Viagem |
| HorCcd | Number(005,0) | Sim | Qtde de Horas para Validade para Cadastro de Carga e Descarga |
| SolUsu | String(001) | Sim | Sugere Usuário em Solicitação de Manutenção |
| UsaApr | String(001) | Sim | Utiliza Aprovador na Solicitação de Veículo da Frota |
| ConIti | String(001) | Sim | Utiliza Controle de Itinerário no Grupo de Itinerário |
| UsaPes | String(001) | Sim | Utiliza Tela de Pesagem para Movimentação de  Carga e Descarga |
| DefPes | String(001) | Sim | Utiliza Crachá nas Telas de Pesagens para Carga e Descarga |
| DspLic | Number(004,0) | Sim | Código Padrão de Despesas de Licença |
| FotVei | Number(001,0) | Sim | Tipo de Armazenamento da Foto do Veículo |
| PrvMan | Number(006,0) | Sim | Iniciar geração de pendências de manutenção com quantos km antes da km programada |
| UltSen | Number(009,0) | Sim | Número da última senha de chegada |
| ConMPr | String(001) | Sim | Mostra concluídas em manutenções programadas (S/N) |
| EmaMPr | String(001) | Sim | Envia e-mail em manutenções programadas (S/N) |
| ModMan | String(011) | Sim | Nome do Modelo para Impressão para Manutenções Programadas |
| UtiChg | String(001) | Sim | Utiliza controle de chegadas pendentes em carga e descarga |
| MasPla | String(010) | Sim | Máscara da Placa |
| ModSol | String(011) | Sim | Nome do Modelo para Impressão de Solicitações de Oficina |
| ModUso | String(011) | Sim | Nome do Modelo para Impressão de Solicitações de Uso |
| ModBio | Number(001,0) | Sim | Modelo da Leitora Biométrica |

---

## Chave Primária

Não possui.

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
