# R005DAT

## Descrição

Horários/Local do Serviço

---

## Resumo

- Campos: 7
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodSrv | Number(004,0) | Não | Código do Serviço |
| CodTSe | Number(002,0) | Não | Turno de Serviço |
| DatAlt | Date | Não | Data de Alteração |
| DiaSem | Number(001,0) | Não | Dia Semana |
| CodHor | Number(004,0) | Sim | Horário na Data |
| GLoPeg | Number(002,0) | Sim | Grupo de Localização da Pegada do Ônibus |
| GLoLar | Number(002,0) | Sim | Grupo de Localização da Largada do Ônibus |

---

## Chave Primária

- CodSrv
- CodTSe
- DatAlt
- DiaSem

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R005DAT_000

**Tabela:** R005SRV

| Origem | Destino |
|--------|---------|
| CodSrv | CodSrv |

### IR_R005DAT_001

**Tabela:** R005TSE

| Origem | Destino |
|--------|---------|
| CodTSe | CodTSe |

