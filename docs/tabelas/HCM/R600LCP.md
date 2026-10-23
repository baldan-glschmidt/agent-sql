# R600LCP

## Descrição

Lista de Comandos Pendentes

---

## Resumo

- Campos: 15
- Chave Primária: 4 campo(s)
- Índices: 2
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodCmd | Number(003,0) | Não | Código do Comando |
| CodPlt | Number(005,0) | Não | Código do Site |
| CodRlg | Number(005,0) | Não | Código do Coletor |
| IdtReg | String(014) | Não | Identificador do Registro de Atualização |
| NumFis | Number(012,0) | Sim | Número Físico do Crachá (Número Serial) |
| DatChe | Date | Sim | Data de Chegada do Comando |
| HorChe | Number(005,0) | Sim | Hora de Chegada do Comando |
| SeqChe | Number(003,0) | Sim | Sequência do Registro |
| QtdTen | Number(001,0) | Sim | Qtde de Tentativas de Envio do Comando |
| StaLcp | Number(001,0) | Sim | Status do Comando |
| DatExe | Date | Sim | Data para Próxima Execução do Comando |
| HorExe | Number(005,0) | Sim | Hora para Próxima Execução do Comando |
| CodUsu | Number(010,0) | Sim | Código do Usuário que Gerou a Pendência |
| CicAtu | Number(002,0) | Sim | Ciclo Atual para Tentativa de Envio de Comando |
| OriLcp | Number(001,0) | Sim | Origem da Pendência |

---

## Chave Primária

- CodCmd
- CodPlt
- CodRlg
- IdtReg

---

## Índices

### R600LCPIndice2

**Tipo:** Não unico

Campos:
- NumFis

### R600LCPIndice3

**Tipo:** Não unico

Campos:
- DatChe
- HorChe

---

## Relacionamentos

### IR_R600LCP_001

**Tabela:** R058PLT

| Origem | Destino |
|--------|---------|
| CodPlt | CodPlt |

### IR_R600LCP_002

**Tabela:** R058RLG

| Origem | Destino |
|--------|---------|
| CodPlt | CodPlt |
| CodRlg | CodRlg |

