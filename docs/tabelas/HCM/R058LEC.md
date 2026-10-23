# R058LEC

## Descrição

Leitoras do controlador

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
| CodDsp | Number(009,0) | Não | Código do Dispositivo |
| ModLei | Number(003,0) | Sim | Modelo da Leitora |
| LeiCra | Number(001,0) | Sim | Tipo da Leitora |
| LocLei | Number(002,0) | Sim | Localização Leitora |
| FxhPrm | String(001) | Sim | Verifica Faixa Horária da Permissão |
| FxhPes | Number(001,0) | Sim | Verifica Faixa Horária |
| VerPrm | String(001) | Sim | Verifica Permissão de Acesso |
| VerAfa | String(001) | Sim | Verifica Afastamento |
| VerVal | String(001) | Sim | Verifica Validade |
| VerCre | Number(001,0) | Sim | Verifica Créditos de Acesso ao Refeitório |
| VerNiv | String(001) | Sim | Verifica Nível de Acesso |
| VerDup | String(001) | Sim | Verifica Anti-dupla Passagem |
| ConIAl | String(001) | Sim | Controla Intervalo de Almoço |
| BloFal | String(001) | Sim | Bloqueia por Falta |
| VerLLb | String(001) | Sim | Verifica Lista de Liberação |
| VerLBl | String(001) | Sim | Verifica Lista de Bloqueio |
| ConInt | String(001) | Sim | Controla Interjornada |
| VerSen | Number(001,0) | Sim | Verifica Senha |
| TipEvc | Number(001,0) | Sim | Tipo do Evento |
| UsaDis | String(001) | Sim | Usa Display |
| NivOri | Number(002,0) | Sim | Nível de Origem da Leitora |
| NivDes | Number(002,0) | Sim | Nível de Destino da Leitora |
| TipPes | String(038) | Sim | Tipo Pessoas Controladas |
| DirAcc | Number(001,0) | Sim | Direção de Acesso |
| EntRel | Number(001,0) | Sim | Interface de Entrada Digital Relacionada |
| LeiBio | Number(001,0) | Sim | Leitora Biométrica |
| TipBio | Number(001,0) | Sim | Tipo de conferência biométrica |
| QtdBio | Number(001,0) | Sim | Quantidade de usuários de biometria |
| GraCon | Number(003,0) | Sim | Grau de Conferência na Biometria (1-100) |
| AmbSen | String(001) | Sim | Controla Ambos Sentidos |
| SenGir | Number(001,0) | Sim | Sentido do Giro da Catraca do Nível de Origem para o Nível de Destino |
| DirN12 | Number(001,0) | Sim | Direção do Sentido Horário ou N1 para N2 (Nivel) |
| DirN21 | Number(001,0) | Sim | Direção do Sentido Anti-Horário ou N2 para N1 (Nivel) |
| UsaSen | Number(001,0) | Sim | Utiliza sensor de urna |
| TemSUR | Number(003,0) | Sim | Tempo de espera do sensor da urna |
| LocBuz | Number(001,0) | Sim | Localização do Buzzer |
| EntAcc | String(007) | Sim | Entradas Digitais utilizadas para validação de Acesso |
| SegSgr | String(001) | Sim | Segue Modelo Sugerido |
| LeiEmb | String(001) | Sim | Leitora Embarcada |
| CodPlt | Number(005,0) | Sim | Código do Site |
| CodRlg | Number(005,0) | Sim | Código do Coletor da Permissão |
| ValAut | Number(001,0) | Sim | Validação por Autorizador |
| ValLoc | Number(001,0) | Sim | Validação Utiliza Autorizador por Local Físico |
| LisAut | String(001) | Sim | Somente Autorizadores do Local Físico na Geração de Lista |
| ArcOri | Number(005,0) | Sim | Área Controlada de Origem |
| ArcDes | Number(005,0) | Sim | Área Controlada de Destino |
| EndCom | Number(003,0) | Sim | Endereço de Comunicação |
| SenPor | String(001) | Sim | Notificar acesso após o ciclo completo |
| AciPor | Number(002,0) | Sim | Tempo para acesso |
| AlmPor | Number(002,0) | Sim | Tempo para geração do alarme de porta aberta |
| UsaPar | String(001) | Sim | Trabalha em paridade com outras leitoras |
| TipOnl | Number(001,0) | Sim | Tipo de validação on-line |
| TipOff | Number(001,0) | Sim | Tipo de validação off-line |
| MsgDir | String(001) | Sim | Mostra direção do acesso no display |
| BaiAut | String(001) | Sim | Baixa Automática do Crachá na Saída do Visitante |
| CodSin | Number(003,0) | Sim | Código do Sinal de Alarme de Intrusão |
| TemAdp | Number(003,0) | Sim | Tempo de expiração do controle de anti-dupla |
| QtdEsc | Number(003,0) | Sim | Quantidade de pessoas escoltadas |
| SinPtA | Number(003,0) | Sim | Código do Sinal de Alarme de Porta Aberta |
| CodTBi | Number(002,0) | Sim | Código da Tecnologia Biométrica |
| CodEnt | Number(009,0) | Sim | Código da Entrada Relacionada |
| EntUrn | Number(009,0) | Sim | Utiliza sensor de urna |
| BaiAen | String(001) | Sim | Baixa automática de crachás de autorização de entrada |
| BloIdt | String(001) | Sim | Bloqueia por identificador de uso do crachá |
| BloFil | String(001) | Sim | Bloqueia por Filial |
| ConFlE | String(001) | Sim | Controla Filial Estrangeira |
| AtuSai | String(001) | Sim | Controla saída almoço |
| IntRev | Number(004,0) | Sim | Intervalo em Minutos para Revista Aleatória |
| BaiPro | String(001) | Sim | Baixa Automática de Crachá Provisório |
| EndMra | Number(010,0) | Sim | Endereço MRA |
| TipVal | Number(001,0) | Sim | Tipo de Validação |
| ConVei | Number(001,0) | Sim | Controla Veículo? |
| ValCSM | String(001) | Sim | Faz validação de acesso na concentradora. |
| EIPLPR | String(015) | Sim | Endereço TCP/IP Câmera LPR |
| ConLot | String(001) | Sim | Controla Lotação |
| DspAss | Number(009,0) | Sim | Leitora Associada |
| RevAle | Number(001,0) | Sim | Controla Revista Aleatória |
| ValCtm | String(001) | Sim | Controla validação customizada |
| EndVaC | String(1000) | Sim | Endereço da validação customizada |

---

## Chave Primária

- CodDsp

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
