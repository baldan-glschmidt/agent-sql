# R058LEI

## Descrição

Leitoras do Modelo do Controlador

---

## Resumo

- Campos: 44
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| ModRlg | Number(004,0) | Não | Código do Modelo do Coletor |
| ModLei | Number(003,0) | Não | Modelo da Leitora |
| LocLei | Number(002,0) | Sim | Localização Leitora |
| FxhPrm | String(001) | Sim | Verifica Faixa Horária da Permissão |
| FxhPes | String(001) | Sim | Verifica Faixa Horária |
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
| DirAcc | Number(001,0) | Sim | Direção do Acesso |
| EntRel | Number(001,0) | Sim | Interface de Entrada Digital Relacionada |
| LeiBio | Number(001,0) | Sim | Leitora Biométrica |
| TipBio | Number(001,0) | Sim | Tipo de conferência biométrica |
| QtdBio | Number(001,0) | Sim | Quantidade de usuários de biometria |
| GraCon | Number(003,0) | Sim | Grau de Conferência na Biometria (1-100) |
| AmbSen | String(001) | Sim | Controla Ambos Sentidos |
| SenGir | Number(001,0) | Sim | Sentido do Giro da Catraca do Nível de Origem para o Nível de Destino |
| DirN12 | Number(001,0) | Sim | Direção do Sentido Horário ou N1 para N2 (Nível) |
| DirN21 | Number(001,0) | Sim | Direção do Sentido Anti-Horário ou N2 para N1 (Nível) |
| BloN21 | String(038) | Sim | Tipo Pessoas Controladas |
| UsaSen | Number(001,0) | Sim | Utiliza sensor de urna |
| TemSUR | Number(003,0) | Sim | Tempo de espera do sensor da urna |
| LocBuz | Number(001,0) | Sim | Localização do Buzzer |
| EntAcc | String(007) | Sim | Entradas Digitais utilizadas para validação de Acesso |
| ValAut | Number(001,0) | Sim | Validação por Autorizador |
| MsgDir | String(001) | Sim | Mostra direção do acesso no display |
| TemAdp | Number(003,0) | Sim | Tempo de expiração do controle de anti-dupla |
| QtdEsc | Number(003,0) | Sim | Quantidade de pessoas escoltadas |
| TemPer | String(058) | Sim | Tempo Mínimo de Permanência |
| AtuSai | String(001) | Sim | Atualiza data de saída |
| EIPLPR | String(015) | Sim | Endereço TCP/IP Câmera LPR |

---

## Chave Primária

- ModRlg
- ModLei

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
