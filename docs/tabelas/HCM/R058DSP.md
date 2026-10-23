# R058DSP

## Descrição

Dispositivos Gerais

---

## Resumo

- Campos: 18
- Chave Primária: 1 campo(s)
- Índices: 1
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
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
| SeqReg | Number(015,0) | Sim | Sequencia Registro |
| PlfEnt | Number(009,0) | Sim | Código do Local Físico Entrada |
| PlfSai | Number(009,0) | Sim | Código do Local Físico Saída |
| Azimut | Number(003,0) | Sim | Azimute, ref. às coordenadas de posicionamento da câmera |
| LatDsp | Number(009,6) | Sim | Latitude que compõe a coordenada de georreferenciamento do dispositivo |
| LonDsp | Number(009,6) | Sim | Longitude que compõe a coordenada de georreferenciamento do dispositivo |
| Protcl | String(036) | Sim | Protocolo do evento retornado pela ADE-02 |
| StaADE | Number(001,0) | Sim | Status do dispositivo para ADE-02 |

---

## Chave Primária

- CodDsp

---

## Índices

### R058DSPIndice2

**Tipo:** Não unico

Campos:
- VerPlf
- PlfEnt
- CodDsp

---

## Relacionamentos

### IR_R058DSP_001

**Tabela:** R058MOD

| Origem | Destino |
|--------|---------|
| ModRlg | ModRlg |

