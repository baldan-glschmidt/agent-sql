# R090TVI

## Descrição

Tipos de Visitas

---

## Resumo

- Campos: 23
- Chave Primária: 1 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| TipVis | Number(003,0) | Não | Tipo da Visita |
| DesVis | String(040) | Sim | Descrição do Tipo da Visita |
| CodPrm | Number(005,0) | Sim | Código da Permissão Padrão para o Tipo de Visita |
| HorVis | Number(005,0) | Sim | Quantidade de Horas de Limite para a Visita |
| HorLim | Number(005,0) | Sim | Hora Limite para a Visita |
| BloAut | String(001) | Sim | Bloqueia Automaticamente o Acessso após Saída do Visitante |
| BaiAut | String(001) | Sim | Baixa Automática do Crachá na Saída do Visitante |
| TipPev | Number(001,0) | Sim | Tipo do Visitante |
| GerCrv | String(001) | Sim | Gera Créditos de Acesso no Refeitório para Visitantes na Entrada |
| ConCre | Number(001,0) | Sim | Controla Créditos de Acesso para Visitantes |
| VidPla | String(001) | Sim | Controle de Vídeo de Segurança por Planta |
| CodReg | Number(003,0) | Sim | Código da Regra (Vídeo de Segurança) |
| ConAdp | String(001) | Sim | Controla Anti-Dupla para Visitantes |
| UsaBio | Number(001,0) | Sim | Utiliza Controle Biométrico |
| GraCon | Number(003,0) | Sim | Grau de Conferência Biométrica (1-100) |
| ConRea | String(001) | Sim | Participa da revista aleatória |
| UtiAlf | String(001) | Sim | Acessa área alfandegária. |
| ConFai | Number(001,0) | Sim | Controla Faixa Horária de Acesso |
| UsaTAA | String(001) | Sim | Utiliza terminal de autoatendimento para validação |
| EnvAge | Number(001,0) | Sim | Forma de envio da notificação de confirmação de agendamento ao visitante |
| EnvChe | Number(001,0) | Sim | Forma de envio da notificação de chegada do visitante |
| UsaRfa | String(001) | Sim | Utiliza Reconhecimento Facial |
| CodCst | Number(002,0) | Sim | Código do consentimento da LGPD |

---

## Chave Primária

- TipVis

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
