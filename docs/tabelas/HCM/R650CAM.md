# R650CAM

## Descrição

Câmeras CFTV

---

## Resumo

- Campos: 6
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| SrvCFT | Number(002,0) | Não | Servidor de Câmeras CFTV |
| CamCFT | Number(005,0) | Não | Câmera CFTV |
| DesCam | String(049) | Sim | Descrição da Câmera CFTV |
| CodDsp | Number(009,0) | Sim | Código do Dispositivo |
| PorCom | Number(005,0) | Sim | Porta de Comunicação com o Servidor CFTV |
| CodCen | Number(002,0) | Sim | Central de Gerenciamento do Acesso |

---

## Chave Primária

- SrvCFT
- CamCFT

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R650CAM_000

**Tabela:** R650SRV

| Origem | Destino |
|--------|---------|
| SrvCFT | SrvCFT |

