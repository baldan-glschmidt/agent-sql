# R034EDP

## Descrição

Exceções (Origem) de Definições de Acesso

---

## Resumo

- Campos: 30
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do Colaborador |
| VerPrm | Number(001,0) | Sim | Verifica se Tem Permissão de Acesso |
| ConFai | Number(001,0) | Sim | Faixa Horária |
| ConAdp | Number(001,0) | Sim | Controla Nível e Anti-Dupla |
| ConCre | Number(001,0) | Sim | Controla Créditos de Acesso para Refeitório |
| ConIAl | Number(001,0) | Sim | Controla Intervalo de Almoço |
| TemAlm | Number(001,0) | Sim | Tempo Mínimo de Almoço (Minutos) |
| BloFal | Number(001,0) | Sim | Bloqueia Colaborador por Falta |
| RecVis | Number(001,0) | Sim | Colaborador Pode Receber Visita |
| AutAgv | Number(001,0) | Sim | Colaborador Pode Autorizar Agendamento de Visita |
| AutAsa | Number(001,0) | Sim | Colaborador Pode Autorizar Saída de Colaboradores |
| AutExt | Number(001,0) | Sim | Colaborador Pode Autorizar Hora Extra |
| UsaFro | Number(001,0) | Sim | Colaborador Pode Utilizar Veículo da Frota |
| GraCon | Number(001,0) | Sim | Grau de Conferência na Biometria |
| ConPac | Number(001,0) | Sim | Controla Tempo de Permanência no Acesso |
| TemPac | Number(001,0) | Sim | Tempo Mínimo de Permanência no Acesso |
| ConRee | Number(001,0) | Sim | Controla Tempo Mínimo de Reentrada |
| TolAcp | Number(001,0) | Sim | Tolerância Acesso Entr./Saída  para Controle de Permanência |
| UsaBio | Number(001,0) | Sim | Utiliza Controle Biométrico |
| AutDbl | Number(001,0) | Sim | Autorizador de  Desbloqueio de Crachás e Colaboradores |
| VerAfa | Number(001,0) | Sim | Verifica Afastamento |
| AprSol | Number(001,0) | Sim | Colaborador pode ser Aprovador de Solicitação de Veículos WEB |
| ConInt | Number(001,0) | Sim | Controla Interjornada |
| TolInt | Number(001,0) | Sim | Tolerância para Controle de Interjornada (Minutos) |
| ConRea | Number(001,0) | Sim | Participa da Revista Aleatória |
| UtiChv | Number(001,0) | Sim | Utiliza Controle de Chaves |
| RepOnl | Number(001,0) | Sim | Utiliza Controle On-line de Ponto Eletrônico - REP |
| UsaRfa | Number(001,0) | Sim | Utiliza Reconhecimento Facial |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
