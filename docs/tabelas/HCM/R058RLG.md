# R058RLG

## Descrição

Coletores

---

## Resumo

- Campos: 80
- Chave Primária: 2 campo(s)
- Índices: 1
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodPlt | Number(005,0) | Não | Código do Site |
| CodRlg | Number(005,0) | Não | Código do Coletor |
| DesRlg | String(050) | Sim | Descrição do Coletor |
| LocRlg | Number(001,0) | Sim | Localização do Coletor |
| CodPor | Number(003,0) | Sim | Código da Portaria de Localização do Coletor |
| TipLei | Number(002,0) | Sim | Tipo da Leitora do Coletor |
| ComRlg | Number(001,0) | Sim | Funcionamento do Coletor |
| ModRlg | Number(004,0) | Sim | Código do Modelo do Coletor |
| CodCen | Number(002,0) | Sim | Central de Gerenciamento do Acesso |
| RlgAlf | String(006) | Sim | Número do Terminal na Arl |
| NumEIP | String(015) | Sim | Número do Endereço IP do Coletor |
| NivAce | Number(002,0) | Sim | Nível de Acesso do Coletor p/ Controle Anti-Dupla |
| CreAcc | String(001) | Sim | Coletor Controla Créditos de Acesso |
| NomApl | String(015) | Sim | Nome do Aplicativo do Coletor |
| BaiAut | String(001) | Sim | Baixa Automática do Crachá na Saída do Visitante |
| StaRlg | Number(001,0) | Sim | Status Atual do Coletor |
| ImgRlg | Image | Sim | Imagem do Coletor |
| SisGer | Number(001,0) | Sim | Sistema que Gerencia este Coletor |
| NumAmb | Number(009,0) | Sim | Ambiente da Planta |
| NomFir | String(015) | Sim | Nome do Firmware do Coletor |
| IniAlm | Number(001,0) | Sim | Início controle de intervalo de almoço |
| FimAlm | Number(001,0) | Sim | Final controle de intervalo de almoço |
| MasSub | String(015) | Sim | Máscara de Subrede |
| EndGat | String(015) | Sim | Endereço de Gateway |
| IntCom | Number(001,0) | Sim | Interface de Comunicação |
| VelCom | Number(001,0) | Sim | Velocidade de Comunicação |
| ConInt | String(001) | Sim | Controla Interjornada |
| NumSer | String(030) | Sim | Número de Série do Coletor |
| VerPlf | Number(003,0) | Sim | Versão do Plano de Localização Física |
| CodPlf | Number(007,0) | Sim | Código do Local Físico |
| CodDsp | Number(009,0) | Sim | Código do Dispositivo |
| PorCom | Number(005,0) | Sim | Porta de Comunicação |
| QtdCra | Number(007,0) | Sim | Quantidade limite de crachás controlados pelo dispositivo |
| TipEip | Number(001,0) | Sim | Tipo de endereço IP |
| NumFis | String(017) | Sim | Número Fiscal |
| UsaDis | String(001) | Sim | Possui Display |
| MsgPad | String(016) | Sim | Mensagem padrão |
| MarCol | String(100) | Sim | Registro de Marcação dos Arquivos de Marcações do Coletor |
| TemBur | Number(003,0) | Sim | Tempo para Burla |
| RFIDBT | Number(002,0) | Sim | Tipo de Leitora RFID |
| StarPr | Number(001,0) | Sim | Bit de Paridade (Início) |
| StopPr | Number(001,0) | Sim | Bit de Paridade (Fim) |
| ValRFI | Number(001,0) | Sim | Valor de leitura do RFID |
| AciFn0 | String(001) | Sim | Executa Acionamentos na Função 0 |
| AtvTec | String(001) | Sim | Ativa bloqueio do teclado |
| PicLt1 | Number(001,0) | Sim | Pictograma Lateral 1 |
| PicLt2 | Number(001,0) | Sim | Pictograma Lateral 2 |
| OpeFir | Number(001,0) | Sim | Modo de Operação do Firmware Digicon |
| UnsAlm | Number(009,0) | Sim | Tamanho do arquivo de Alarmes Não Enviados (em bytes) |
| UnsAcc | Number(009,0) | Sim | Tamanho do arquivo de Acessos Não Enviados (em bytes) |
| SntAlm | Number(009,0) | Sim | Tamanho do arquivo de Alarmes Enviados (em bytes) |
| SntAcc | Number(009,0) | Sim | Tamanho do arquivo de Acessos Enviados (em bytes) |
| ArqLog | Number(009,0) | Sim | Tamanho dos Arquivos de Log (em bytes) |
| TecLei | Number(001,0) | Sim | Tecnologia da Leitora |
| VerFir | Number(008,0) | Sim | Versão do Firmware (comunicação Digicon) - G6 |
| BaiAen | String(001) | Sim | Baixa automática de crachás de autorização de entrada |
| NumEmp | Number(004,0) | Sim | Código da Empresa |
| CodFil | Number(006,0) | Sim | Código da Filial |
| ConApb | Number(001,0) | Sim | Controla Acesso Alfandegado |
| CodMsc | Number(002,0) | Sim | Código Mapa Smart Card |
| SenUsu | Number(004,0) | Sim | Senha do usuário |
| GraCon | Number(003,0) | Sim | Grau de Conferência na Biometria |
| BloCon | String(001) | Sim | Bloquear conexão com dispositivo |
| IDGate | Number(003,0) | Sim | Identificador do Gateway |
| ValLPR | Number(001,0) | Sim | Validação de Veículos LPR |
| FaiLPR | Number(003,0) | Sim | Faixa de Validação LPR |
| MarVon | Number(001,0) | Sim | Marcação de Veículos On line |
| AutPes | String(001) | Sim | Atualização Automática de Pessoas |
| IPServ | String(015) | Sim | IP do Servidor de Imagem |
| PorSer | Number(005,0) | Sim | Porta do Servidor de Imagem |
| TemLPR | Number(003,0) | Sim | Tempo de Validação LPR |
| DisEve | String(001) | Sim | Disponibiliza Evento SDK |
| IntEle | String(001) | Sim | Integra com Elevadores |
| GerLis | Number(001,0) | Sim | Tecnologia utilizada na geração de listas |
| DetMas | String(001) | Sim | Detectar uso de máscara |
| BloMas | String(001) | Sim | Bloquear pessoa sem uso de máscara |
| DetTem | String(001) | Sim | Detectar temperatura da pessoa |
| BloTem | String(001) | Sim | Bloquear pessoa com temperatura anormal |
| TemMin | Number(004,2) | Sim | Temperatura mínima da pessoa para acesso |
| TemMax | Number(004,2) | Sim | Temperatura máxima da pessoa para acesso |

---

## Chave Primária

- CodPlt
- CodRlg

---

## Índices

### R058rlgIndice2

**Tipo:** Não unico

Campos:
- CodDsp

---

## Relacionamentos

### IR_R058RLG_000

**Tabela:** R058PLT

| Origem | Destino |
|--------|---------|
| CodPlt | CodPlt |

### IR_R058RLG_007

**Tabela:** R058MOD

| Origem | Destino |
|--------|---------|
| ModRlg | ModRlg |

