# R058ENT

## Descrição

Entradas do Coletor

---

## Resumo

- Campos: 19
- Chave Primária: 1 campo(s)
- Índices: 0
- Relacionamentos: 3

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodPlt | Number(005,0) | Sim | Código do Site |
| CodRlg | Number(005,0) | Sim | Código do Coletor |
| EndEnt | Number(003,0) | Sim | Endereço da Entrada no Coletor |
| CodSin | Number(003,0) | Sim | Código do Sinal de Alarme |
| CodRac | Number(003,0) | Sim | Código da Reação |
| GraImg | String(001) | Sim | Ativa Gravação da Imagem CFTV na Coleta do Alarme |
| IntGra | Number(003,0) | Sim | Intervalo em Segundos para Gravação da Imagem |
| NumAmb | Number(009,0) | Sim | Ambiente da Planta |
| CodPlf | Number(007,0) | Sim | Código do Local Físico |
| VerPlf | Number(003,0) | Sim | Versão do Plano de Localização Física |
| CodDsp | Number(009,0) | Não | Código do Dispositivo |
| EndCom | Number(003,0) | Sim | Endereço de Comunicação |
| EstDef | Number(001,0) | Sim | Estado default |
| DlyAtv | Number(003,0) | Sim | Delay para ativação do alarme |
| DlyDtv | Number(003,0) | Sim | Delay para desativação do alarme |
| TemBuz | Number(003,0) | Sim | Tempo Buzzer (Aviso Sonoro) |
| UsaDis | String(001) | Sim | Usa Display |
| IDLaco | Number(003,0) | Sim | Identificador do Laço |
| TipSen | Number(001,0) | Sim | Tipo do Sensor |

---

## Chave Primária

- CodDsp

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R058ENT_000

**Tabela:** R058PLT

| Origem | Destino |
|--------|---------|
| CodPlt | CodPlt |

### IR_R058ENT_001

**Tabela:** R058RLG

| Origem | Destino |
|--------|---------|
| CodPlt | CodPlt |
| CodRlg | CodRlg |

### IR_R058ENT_003

**Tabela:** R062SIN

| Origem | Destino |
|--------|---------|
| CodSin | CodSin |

