# R058DSP_AUD

## Descrição

Dispositivos Gerais - Auditoria

---

## Resumo

- Campos: 15
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| SeqReg | Number(015,0) | Não | Sequência Registro |
| VerSeq | Number(010,0) | Não | Versão Sequência |
| CodDsp | Number(009,0) | Não | Código do Dispositivo |
| ModRlg | Number(004,0) | Sim | Código do Modelo do Dispositivo |
| DesDsp | String(050) | Sim | Descrição do Dispositivo |
| VerPlf | Number(003,0) | Sim | Versão do Plano de Localização Física |
| CodPlf | Number(007,0) | Sim | Código do Local Físico |
| DspPai | Number(009,0) | Sim | Código do Dispositivo Pai. |
| StaDsp | Number(001,0) | Sim | Status do Dispositivo |
| ImgDsp | Image | Sim | Imagem do Dispositivo |
| ObsDsp | String(080) | Sim | Observação |
| StaAtu | Number(001,0) | Sim | Status das alterações realizadas nos dispositivos |
| Azimut | Number(003,0) | Sim | Azimute, ref. às coordenadas de posicionamento da câmera |
| LatDsp | String(015) | Sim | Latitude que compõe a coordenada de georreferenciamento do dispositivo |
| LonDsp | String(015) | Sim | Longitude que compõe a coordenada de georreferenciamento do dispositivo |

---

## Chave Primária

- SeqReg
- VerSeq
- CodDsp

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R058DSP_AUD_003

**Tabela:** R058MOD

| Origem | Destino |
|--------|---------|
| ModRlg | ModRlg |

