# R058MOD

## Descrição

Modelos de Coletor

---

## Resumo

- Campos: 98
- Chave Primária: 1 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| ModRlg | Number(004,0) | Não | Código do Modelo do Coletor |
| DesMod | String(040) | Sim | Descrição do Modelo do Coletor |
| ModCol | Number(002,0) | Sim | Modelo do Coletor |
| DirMar | String(200) | Sim | Diretório dos Arquivos de Marcações do Coletor |
| DirRej | String(200) | Sim | Diretório dos Arquivos das Marcações Rejeitadas |
| MesCol | String(035) | Sim | Registro Mestre dos Arquivos de Marcações do Coletor |
| MarCol | String(100) | Sim | Registro de Marcação dos Arquivos de Marcações do Coletor |
| TipMod | Number(003,0) | Sim | Modelo do Controlador |
| LisVal | Number(001,0) | Sim | Tipo de Lista de Validação |
| TipCom | Number(001,0) | Sim | Protocolo |
| MsgPad | String(016) | Sim | Mensagem padrão |
| TemBur | Number(003,0) | Sim | Tempo para Burla |
| RFIDBT | Number(002,0) | Sim | Tipo de Leitora RFID |
| StarPr | Number(001,0) | Sim | Bit de Paridade (Início) |
| StopPr | Number(001,0) | Sim | Bit de Paridade (Fim) |
| ValRFI | Number(001,0) | Sim | Valor de leitura do RFID |
| ImgMod | Image | Sim | Imagem do equipamento |
| CodDrv | Number(003,0) | Sim | Código de Cadastro do Driver Integrador |
| CatMod | Number(002,0) | Sim | Categoria do Modelo |
| ClaMod | Number(002,0) | Sim | Classificação do Modelo |
| ArqAFD | String(001) | Sim | Arquivos no formato AFD(Arquivos Fonte de Dados) |
| FabMod | Number(002,0) | Sim | Fabricante |
| QtdInt | Number(003,0) | Sim | Quantidade Interface Entrada |
| QtdSai | Number(003,0) | Sim | Quantidade Interface Saida |
| UsaDis | String(001) | Sim | Possui Display |
| AciFn0 | String(001) | Sim | Executa Acionamentos na Função 0 |
| MidCom | Number(002,0) | Sim | Mídia de Comunicação |
| BanCom | Number(002,0) | Sim | Banda de Comunicação |
| TecLei | Number(002,0) | Sim | Tipo de Tecnologia |
| QtdMod | Number(003,0) | Sim | Quantidade de Módulos |
| QtdCam | Number(003,0) | Sim | Quantidade de Câmeras |
| QtdZon | Number(003,0) | Sim | Quantidade de Zonas |
| ArqRed | Number(002,0) | Sim | Arquitetura de Rede |
| DisImg | String(050) | Sim | Dispositivo de Imagem |
| NumPix | Number(002,0) | Sim | Número de Pixels Efetivos |
| MedLen | Number(006,2) | Sim | Medida da Lente em Milímetros |
| MedFil | Number(006,2) | Sim | Medida do Filtro em Milímetros |
| PamTit | String(001) | Sim | Pam/Tilt |
| ZomDig | Number(006,2) | Sim | Zoom Digital |
| ZomOpt | Number(006,2) | Sim | Zoom Óptico |
| ResHor | Number(004,0) | Sim | Resolução Horizontal em Linhas |
| IluMin | Number(006,2) | Sim | Iluminação Mínima (Lux) |
| DayNig | String(001) | Sim | Day Night |
| InfRed | String(001) | Sim | Infrared |
| AlcaIR | Number(004,0) | Sim | Alcance Infrared em Metros |
| AutIri | String(001) | Sim | Auto Íris |
| TipTrs | Number(002,0) | Sim | Tipo de Transmissão |
| CarMod | String(255) | Sim | Características do Modelo |
| AtvTec | String(001) | Sim | Ativa bloqueio do teclado |
| VerBio | Number(001,0) | Sim | Tipo da verificação biométrica |
| MemMrp | Number(002,0) | Sim | Memória de Registro Permanente (MRP) |
| ComBob | Number(004,0) | Sim | Comprimento da bobina |
| CorTAA | String(011) | Sim | Cor do terminal |
| DesBVP | String(2500) | Sim | Boas vindas em Português |
| DesBVI | String(2500) | Sim | Boas vindas em Inglês |
| DesBVE | String(2500) | Sim | Boas vindas em Espanhol |
| TAcAgP | String(2500) | Sim | Termos de Aceite Credenciais Agendadas em Português |
| TAcAgI | String(2500) | Sim | Termos de Aceite Credenciais Agendadas em Inglês |
| TAcAgE | String(2500) | Sim | Termos de Aceite Credenciais Agendadas em Espanhol |
| TAcNAP | String(2500) | Sim | Termos de Aceite Credenciais não Agendadas em Português |
| TAcNAI | String(2500) | Sim | Termos de Aceite Credenciais não Agendadas em Inglês |
| TAcNAE | String(2500) | Sim | Termos de Aceite Credenciais não Agendadas em Espanhol |
| METTCS | Number(001,0) | Sim | Tipo de Credencial Provisória |
| METBar | String(001) | Sim | Usar Código de Barras |
| METQrC | String(001) | Sim | QRCode |
| METFot | String(001) | Sim | Usar Foto do Provisório |
| METLog | String(001) | Sim | Logotipo da Empresa |
| MEPTCS | Number(001,0) | Sim | Tipo de Credencial de Visitante |
| MEPBar | String(001) | Sim | Usar Código de Barras |
| MEPQrC | String(001) | Sim | QRCode |
| MEPFot | String(001) | Sim | Usar Foto do Visitante |
| MEPLog | String(001) | Sim | Logotipo da Empresa |
| MEPPVi | String(001) | Sim | Permissão do Visitante |
| MEPVis | String(001) | Sim | Visitado |
| ValFot | Number(004,0) | Sim | Validade da foto do visitante (dias) |
| IdeDoc | String(001) | Sim | Identificar por documento |
| IdeLDA | String(001) | Sim | Identificar por Login de rede (LDAP) |
| IdeFac | String(001) | Sim | Utilizar reconhecimento facial para colaborador |
| UtiPsq | String(001) | Sim | Utilizar pesquisa de satisfação |
| ValPsq | Number(004,0) | Sim | Validade da pesquisa de satisfação (dias) |
| MosTac | String(001) | Sim | Mostrar termo de aceite para colaborador |
| MosTav | String(001) | Sim | Mostrar termo de aceite para visitante |
| ValFoc | Number(004,0) | Sim | Validade da foto do colaborador (dias) |
| QtdTen | Number(002,0) | Sim | Quantidade de tentativas de login de rede |
| ArqCss | Image | Sim | Arquivo CSS de customização do terminal de autoatendimento |
| ArqPor | Image | Sim | Arquivo do dicionário de dados em português |
| ArqEsp | Image | Sim | Arquivo do dicionário de dados em espanhol |
| ArqIng | Image | Sim | Arquivo do dicionário de dados em inglês |
| PerAtc | Number(004,0) | Sim | Pergunta da pesquisa de satisfação para colaborador |
| PerAtv | Number(004,0) | Sim | Pergunta da pesquisa de satisfação para visitante |
| IdeFav | String(001) | Sim | Utilizar reconhecimento facial para visitante |
| FotCol | String(001) | Sim | Permitir alterar a foto do cadastro do colaborador |
| FotVis | String(001) | Sim | Permitir alterar a foto do cadastro do visitante |
| PerFac | Number(003,0) | Sim | Grau de similaridade para o reconhecimento facial |
| ImpVis | String(001) | Sim | Imprimir comprovante para visitantes |
| ImpCol | String(001) | Sim | Imprimir comprovante para colaboradores |
| FotAut | String(001) | Sim | Capturar foto automaticamente |
| TipRep | Number(001,0) | Sim | Tipo de REP |

---

## Chave Primária

- ModRlg

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
