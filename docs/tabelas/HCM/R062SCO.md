# R062SCO

## Descrição

Status dos Coletores

---

## Resumo

- Campos: 14
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodPlt | Number(005,0) | Não | Código do Site |
| CodRlg | Number(005,0) | Não | Código do Coletor Onde Foi Gerado o Alarme |
| EndEnt | Number(003,0) | Sim | Código do Endereço de Entrada |
| ModOpe | Number(001,0) | Sim | Modo de Operação do Coletor |
| SitCol | Number(002,0) | Sim | Situação do Coletor |
| StaMon | Number(001,0) | Sim | Status do Monitoramento (Quadro Sinótico) |
| HorSco | Number(005,0) | Sim | Hora da Mudança do Status |
| DatSco | Date | Sim | Data do Alarme |
| StaMem | Number(003,0) | Sim | Status da Memória Ocupada do Dispositivo |
| CodDsp | Number(009,0) | Não | Código do Dispositivo |
| DatInc | Date | Sim | Data de Atualização Incondicional |
| HorInc | Number(005,0) | Sim | Hora Atu. Incondicional |
| StaBat | Number(003,0) | Sim | Status da Bateria Restante do Dispositivo |
| StaBob | Number(003,0) | Sim | Status da Bobina Restante do Dispositivo |

---

## Chave Primária

- CodPlt
- CodRlg
- CodDsp

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R062SCO_000

**Tabela:** R058PLT

| Origem | Destino |
|--------|---------|
| CodPlt | CodPlt |

### IR_R062SCO_001

**Tabela:** R058RLG

| Origem | Destino |
|--------|---------|
| CodPlt | CodPlt |
| CodRlg | CodRlg |

