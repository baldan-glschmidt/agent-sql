# R017DAC

## Descrição

Definições de Acesso por Posto de Trabalho

---

## Resumo

- Campos: 35
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| EstPos | Number(003,0) | Não | Código da Estrutura de Postos de trabalho |
| PosTra | String(024) | Não | Posto de trabalho |
| VerPrm | String(001) | Sim | Verifica se Tem Permissão de Acesso |
| CodPrm | Number(005,0) | Sim | Permissão de Acesso para os Dias Normais |
| PrmFer | Number(005,0) | Sim | Permissão de Acesso para os Feriados |
| PrmSab | Number(005,0) | Sim | Permissão de Acesso para os Sábados |
| PrmDom | Number(005,0) | Sim | Permissão de Acesso para os Domingos |
| PrmVis | Number(005,0) | Sim | Permissão de Acesso do Visitante Quando for Visitá-lo |
| ConFai | Number(001,0) | Sim | Controla Faixa Horária de Acesso |
| ConAdp | String(001) | Sim | Controla Nível e Anti-Dupla |
| ConCre | Number(001,0) | Sim | Controla Créditos de Acesso para Refeitório |
| ConIAl | String(001) | Sim | Controla Intervalo de Almoço |
| TemAlm | Number(003,0) | Sim | Tempo Mínimo de Almoço (Minutos) |
| BloFal | String(001) | Sim | Bloqueia Colaborador por Falta |
| RecVis | String(001) | Sim | Colaborador Pode Receber Visita |
| AutAgv | String(001) | Sim | Colaborador Pode Autorizar Agendamento de Visita |
| AutAsa | String(001) | Sim | Colaborador Pode Autorizar Saída de Colaboradores |
| AutExt | String(001) | Sim | Colaborador Pode Autorizar Hora Extra |
| UsaFro | String(001) | Sim | Colaborador Pode Utilizar Veículo da Frota |
| GraCon | Number(003,0) | Sim | Grau de Conferência na Biometria |
| ConPac | String(001) | Sim | Controla Tempo de Permanência no Acesso |
| TemPac | Number(003,0) | Sim | Tempo Mínimo de Permanência no Acesso |
| ConRee | String(001) | Sim | Controla Tempo Mínimo de Reentrada |
| TolAcp | Number(005,0) | Sim | Tolerância Acesso Entr./Saída  para Controle de Permanência |
| UsaBio | Number(001,0) | Sim | Utiliza Controle Biométrico |
| AutDbl | String(001) | Sim | Autorizador de  Desbloqueio de Crachás e Colaboradores |
| VerAfa | String(001) | Sim | Verifica Afastamento |
| AprSol | String(001) | Sim | Colaborador pode ser Aprovador de Solicitação de Veículos WEB |
| ConInt | String(001) | Sim | Controla Interjornada |
| TolInt | Number(003,0) | Sim | Tolerância para Controle de Interjornada (Minutos) |
| ConRea | String(001) | Sim | Participa da revista aleatória |
| UtiChv | String(001) | Sim | Utiliza Controle de Chaves |
| RepOnl | String(001) | Sim | Utiliza controle on line de ponto eletrônico - REP |
| UsaRfa | String(001) | Sim | Utiliza Reconhecimento Facial |
| CodUsu | Number(010,0) | Sim | Código do Usuário que Cadastrou a Permissão |

---

## Chave Primária

- EstPos
- PosTra

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R017DAC_001

**Tabela:** R017POS

| Origem | Destino |
|--------|---------|
| EstPos | EstPos |
| PosTra | PosTra |

