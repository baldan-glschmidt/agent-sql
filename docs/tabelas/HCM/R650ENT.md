# R650ENT

## Descrição

Câmeras das Entradas de Sinais de Alarme

---

## Resumo

- Campos: 6
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 4

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| SrvCFT | Number(002,0) | Não | Servidor de Câmeras CFTV |
| CamCFT | Number(005,0) | Não | Câmera CFTV |
| CodDsp | Number(009,0) | Não | Código do Dispositivo |
| EndEnt | Number(003,0) | Sim | Endereço da Entrada no Coletor |
| CodPlt | Number(005,0) | Sim | Código do Site |
| CodRlg | Number(005,0) | Sim | Código do Coletor |

---

## Chave Primária

- SrvCFT
- CamCFT
- CodDsp

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R650ENT_000

**Tabela:** R650SRV

| Origem | Destino |
|--------|---------|
| SrvCFT | SrvCFT |

### IR_R650ENT_001

**Tabela:** R650CAM

| Origem | Destino |
|--------|---------|
| SrvCFT | SrvCFT |
| CamCFT | CamCFT |

### IR_R650ENT_004

**Tabela:** R058PLT

| Origem | Destino |
|--------|---------|
| CodPlt | CodPlt |

### IR_R650ENT_005

**Tabela:** R058RLG

| Origem | Destino |
|--------|---------|
| CodPlt | CodPlt |
| CodRlg | CodRlg |

