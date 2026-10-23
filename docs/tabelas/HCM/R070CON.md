# R070CON

## Descrição

Controle de Acesso

---

## Resumo

- Campos: 116
- Chave Primária: 2 campo(s)
- Índices: 9
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| IdtPes | String(023) | Não | Identificador da Pessoa |
| NumCra | Number(012,0) | Não | Número do Crachá |
| TecCra | Number(001,0) | Sim | Tecnologia do Crachá |
| ChcPri | Number(012,0) | Sim | Número do Crachá Principal |
| NumFis | Number(012,0) | Não | Número Físico do Crachá |
| TipCra | Number(002,0) | Sim | Tipo de Crachá |
| CodPrm | Number(005,0) | Sim | Permissão de Acesso para os Dias Normais |
| PrmSab | Number(005,0) | Sim | Permissão de Acesso para os Sábados |
| PrmDom | Number(005,0) | Sim | Permissão de Acesso para os Domingos |
| PrmFer | Number(005,0) | Sim | Permissão de Acesso para os Feriados |
| SenCol | String(006) | Sim | Senha do Colaborador para o Controle de Acesso |
| SitCra | Number(002,0) | Sim | Situação do crachá |
| IniVal | String(016) | Sim | Data Inicial do Histórico de Crachá |
| DatVal | String(016) | Sim | Data Validade do Crachá |
| IniAfa | String(016) | Sim | Data Inicial do Afastamento |
| DatAfa | String(016) | Sim | Data Final do Afastamento |
| MsgAcc | String(032) | Sim | Descrição da Mensagem que Será Mostrada nos Coletores |
| DatMsg | String(016) | Sim | Data Final da Mensagem |
| QtdMsg | Number(002,0) | Sim | Qtde de Vezes que Será Mostrada a Mensagem nos Coletores |
| MsgAtu | Number(002,0) | Sim | Qtde de Mensagens a ser exibida no equipamento |
| ConIAl | Number(001,0) | Sim | Controla Intervalo de Almoço |
| TemAlm | Number(003,0) | Sim | Tempo Mínimo de Almoço (Minutos) |
| VerAfa | Number(001,0) | Sim | Verifica Afastamento |
| UsaBio | Number(001,0) | Sim | Utiliza Controle Biométrico |
| VerPrm | Number(001,0) | Sim | Verifica se Tem Permissão de Acesso |
| ConFai | Number(001,0) | Sim | Controla Faixa Horária de Acesso |
| ConAdp | Number(001,0) | Sim | Controla Anti-Dupla |
| ConCre | Number(001,0) | Sim | Controla Créditos de Acesso para Refeitório |
| ConPac | Number(001,0) | Sim | Controla Tempo de Permanência no Acesso |
| TemPac | Number(003,0) | Sim | Tempo Mínimo de Permanência no Acesso |
| ConRea | Number(001,0) | Sim | Revista aleatória |
| BloAut | Number(001,0) | Sim | Bloqueia Automaticamente o Acessso após Saída do Visitante |
| BloFal | Number(001,0) | Sim | Colaborador Bloqueado por Falta |
| NivAtu | String(005) | Sim | Nível de acesso atual |
| DatNiv | Date | Sim | Data da Última Atualização do Nível |
| HorNiv | Number(005,0) | Sim | Hora da Última Atualização do Nível |
| SeqNiv | Number(006,0) | Sim | Sequência da Última Atualização do Nível |
| FaiAc1 | String(056) | Sim | Faixa de acesso (domingo) |
| FaiAc2 | String(056) | Sim | Faixa de acesso (segunda-feira) |
| FaiAc3 | String(056) | Sim | Faixa de acesso (terça-feira) |
| FaiAc4 | String(056) | Sim | Faixa de acesso (quarta-feira) |
| FaiAc5 | String(056) | Sim | Faixa de acesso (quinta-feira) |
| FaiAc6 | String(056) | Sim | Faixa de acesso (sexta-feira) |
| FaiAc7 | String(056) | Sim | Faixa de acesso (sábado) |
| FaiPt1 | String(056) | Sim | Faixa de ponto (domingo) |
| FaiPt2 | String(056) | Sim | Faixa de ponto (segunda-feira) |
| FaiPt3 | String(056) | Sim | Faixa de ponto (terça-feira) |
| FaiPt4 | String(056) | Sim | Faixa de ponto (quarta-feira) |
| FaiPt5 | String(056) | Sim | Faixa de ponto (quinta-feira) |
| FaiPt6 | String(056) | Sim | Faixa de ponto (sexta-feira) |
| FaiPt7 | String(056) | Sim | Faixa de ponto (sábado) |
| FaiRef | String(056) | Sim | Faixa de Refeitório |
| CreAc1 | Number(002,0) | Sim | Quantidade de créditos de acesso 1 |
| CreFx1 | String(008) | Sim | Faixa horária de créditos de acesso 1 |
| QtdCr1 | Number(002,0) | Sim | Qtde atual de créditos 1 |
| CreAc2 | Number(002,0) | Sim | Quantidade de créditos de acesso 2 |
| CreFx2 | String(008) | Sim | Faixa horária de créditos de acesso 2 |
| QtdCr2 | Number(002,0) | Sim | Qtde atual de créditos 2 |
| CreAc3 | Number(002,0) | Sim | Quantidade de créditos de acesso 3 |
| CreFx3 | String(008) | Sim | Faixa horária de créditos de acesso 3 |
| QtdCr3 | Number(002,0) | Sim | Qtde atual de créditos 3 |
| CreAc4 | Number(002,0) | Sim | Quantidade de créditos de acesso 4 |
| CreFx4 | String(008) | Sim | Faixa horária de créditos de acesso 4 |
| QtdCr4 | Number(002,0) | Sim | Qtde atual de créditos 4 |
| CreAc5 | Number(002,0) | Sim | Quantidade de créditos de acesso 5 |
| CreFx5 | String(008) | Sim | Faixa horária de créditos de acesso 5 |
| QtdCr5 | Number(002,0) | Sim | Qtde atual de créditos 5 |
| CreAc6 | Number(002,0) | Sim | Quantidade de créditos de acesso 6 |
| CreFx6 | String(008) | Sim | Faixa horária de créditos de acesso 6 |
| QtdCr6 | Number(002,0) | Sim | Qtde atual de créditos 6 |
| PrmRt1 | Number(005,0) | Sim | Permissão adicional 1 |
| DInPr1 | String(010) | Sim | Data inicial da permissão adicional 1 |
| DFnPr1 | String(010) | Sim | Data final da permissão adicional 1 |
| PrmRt2 | Number(005,0) | Sim | Permissão adicional 2 |
| DInPr2 | String(010) | Sim | Data inicial da permissão adicional 2 |
| DFnPr2 | String(010) | Sim | Data final da permissão adicional 2 |
| PrmRt3 | Number(005,0) | Sim | Permissão adicional 3 |
| DInPr3 | String(010) | Sim | Data inicial da permissão adicional 3 |
| DFnPr3 | String(010) | Sim | Data final da permissão adicional 3 |
| GraCon | Number(003,0) | Sim | Grau de Conferência na Biometria (1-100) |
| ConInt | Number(001,0) | Sim | Controla Interjornada |
| TolInt | Number(003,0) | Sim | Tolerância para Controle de Interjornada (Minutos) |
| ConRee | Number(001,0) | Sim | Controla Tempo Mínimo de Reentrada |
| TolAcp | Number(002,0) | Sim | Tolerância Entrada/Saída para controle de permanência |
| DatSai | Date | Sim | Data de Última Passagem no Refeitório |
| HorSai | Number(005,0) | Sim | Hora de Última Passagem no Refeitório |
| SeqSai | Number(006,0) | Sim | Sequência de Última Passagem no Refeitório |
| ValAut | Number(001,0) | Sim | Necessita de Validação do Responsável |
| CodArc | Number(005,0) | Sim | Área controlada atual |
| DatArc | Date | Sim | Data da última atualização da área controlada |
| HorArc | Number(005,0) | Sim | Hora da última atualização da área controlada |
| SeqArc | Number(006,0) | Sim | Sequência da última atualização da área controlada |
| NomFun | String(040) | Sim | Nome do Colaborador |
| NumPis | Number(011,0) | Sim | Número do PIS/PASEP |
| DatCSM | Date | Sim | Data da última atualização do dado na CSM |
| HorCSM | Number(005,0) | Sim | Hora da última atualização do dado na CSM |
| SeqCSM | Number(002,0) | Sim | Sequência da última atualização do dado na CSM |
| TipDoc | Number(001,0) | Sim | Tipo do Documento |
| NumDoc | String(020) | Sim | Número do Documento |
| NomPes | String(040) | Sim | Nome da Pessoa |
| NumFon | String(020) | Sim | Número do Telefone |
| DdiFon | Number(003,0) | Sim | Código DDI do telefone |
| DddFon | Number(003,0) | Sim | Código DDD do telefone |
| QtdPrv | Number(002,0) | Sim | Quantidade de Provisórios |
| PesBlo | Number(001,0) | Sim | Bloqueio da pessoa |
| DesBlo | String(030) | Sim | Descrição do bloqueio da pessoa |
| RecVis | Number(001,0) | Sim | Colaborador Pode Receber Visita |
| ProPre | Number(001,0) | Sim | Processamento prévio da tabela Controle |
| NumEmp | Number(004,0) | Sim | Código da Empresa |
| TipCol | Number(001,0) | Sim | Tipo Colaborador |
| NumCad | Number(009,0) | Sim | Cadastro do Colaborador |
| NumMat | String(015) | Sim | Matrícula do Aluno |
| ProPac | String(020) | Sim | Prontuário do Paciente |
| NumCan | Number(007,0) | Sim | Cadastro do Candidato |
| ANDVIS | Number(003,0) | Sim | Andar da Visita |
| UsaRfa | Number(001,0) | Sim | Utiliza Reconhecimento Facial |

---

## Chave Primária

- IdtPes
- NumFis

---

## Índices

### R070CONIndice2

**Tipo:** Não unico

Campos:
- NumFis

### R070CONIndice3

**Tipo:** Não unico

Campos:
- NumCra

### R070CONIndice4

**Tipo:** Não unico

Campos:
- NumCra
- DatNiv
- HorNiv
- SeqNiv

### R070CONIndice5

**Tipo:** Não unico

Campos:
- IdtPes

### R070CONIndice6

**Tipo:** Não unico

Campos:
- ValAut
- IdtPes

### R070CONIndice7

**Tipo:** Não unico

Campos:
- IdtPes
- ValAut

### R070CONIndice8

**Tipo:** Não unico

Campos:
- SitCra
- NumFis

### R070CONIndice9

**Tipo:** Não unico

Campos:
- NumFis
- SitCra

### R070CONIndice10

**Tipo:** Não unico

Campos:
- VerPrm
- NumFis

---

## Relacionamentos

Nenhum relacionamento cadastrado.
