# R058MOM

## Descrição

Monitoramento de Eventos no Mapa

---

## Resumo

- Campos: 20
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodSin | Number(003,0) | Não | Código do Sinal de Alarme |
| CodDsp | Number(009,0) | Não | Código do Dispositivo |
| TipSin | Number(001,0) | Não | Tipo do Sinal |
| TipAcc | Number(003,0) | Não | Tipo do Acesso |
| EstEve | String(001) | Não | Estado do Evento - Reconhecido ou Alarmado |
| CodPlt | Number(005,0) | Sim | Código do Site |
| CodRlg | Number(005,0) | Sim | Código do Coletor |
| FocMpa | String(001) | Sim | Focalizar Mapa |
| SinGrd | String(001) | Sim | Sinalizar Evento na Grid do Mapa |
| AleMpa | Number(001,0) | Sim | Alertar Evento no Mapa |
| TipMap | Number(001,0) | Sim | Tipo de cor do alerta |
| CorMap | String(009) | Sim | Cor do Alerta |
| ImgMap | Image | Sim | Imagem do Alerta |
| SinTre | String(001) | Sim | Sinalizar Evento na Tree |
| DesRac | String(255) | Sim | Descrição da Reação |
| CorLin | String(009) | Sim | Cor da Linha na Grid do Mapa |
| AleSon | String(001) | Sim | Alerta Sonoro |
| DesSon | String(049) | Sim | Descrição do alerta sonoro |
| VisCam | String(001) | Sim | Vizualiza imagem da câmera |
| CodCam | Number(009,0) | Sim | Código da Câmera |

---

## Chave Primária

- CodDsp
- TipSin
- CodSin
- TipAcc
- EstEve

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
