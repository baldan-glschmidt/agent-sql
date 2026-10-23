# R062SIN

## Descrição

Sinais de Alarme

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
| CodSin | Number(003,0) | Não | Código do Sinal de Alarme |
| DesSin | String(040) | Sim | Descrição do Sinal de Alarme |
| PriSin | Number(002,0) | Sim | Prioridade do Sinal de Alarme |
| MosMon | String(001) | Sim | Mostrar Sinal de Alarme na Tela de Monitoramento |
| CorSin | Number(009,0) | Sim | Cor do Sinal de Alarme Não Tratado na Tela de Monitoramento |
| CorRec | Number(009,0) | Sim | Cor do Sinal de Alarme Reconhecido na Tela de Monitoramento |
| BeeSin | String(001) | Sim | Beep para o Sinal de Alarme na Tela de Monitoramento |
| ImgSin | Image | Sim | Imagem do Sinal |
| TipSen | Number(002,0) | Sim | Tipo do Alarme |
| RecCol | String(001) | Sim | Permite Reconhecimento Coletivo |
| RecAut | String(001) | Sim | Permite Reconhecimento Automático |
| TraAut | String(001) | Sim | Permite Tratamento Automático do Alarme |
| IntNor | Number(005,0) | Sim | Intervalo em Segundos de Normalização para Rec. Automático |
| IntNot | Number(005,0) | Sim | Intervalo em Segundos de Normalização para Trat. Automático |
| VisCam | String(001) | Sim | Visualiza Câmera CFTV no Monitoramento do Alarme |
| AlmTes | String(001) | Sim | Alarme de Testes |
| IntTes | Number(005,0) | Sim | Intervalo do Alarme de Teste |
| ResTel | String(001) | Sim | Restaura Tela de Alarmes |
| IntMap | Number(005,0) | Sim | Intervalo em Minutos para Sinalização no A-Map |
| OriAlm | Number(001,0) | Sim | Origem do Alarme |
| IntNta | Number(005,0) | Sim | Intervalo de Notificação do Alarme (em minutos) |
| DlyCon | Number(005,0) | Sim | Intervalo de notificação do alarme de conexão (em segundos) |
| DesCEA | String(001) | Sim | Descartar a coleta de eventos do alarme |

---

## Chave Primária

- CodSin

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
