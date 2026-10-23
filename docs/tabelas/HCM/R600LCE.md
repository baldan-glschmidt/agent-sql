# R600LCE

## Descrição

Lista de Comandos Enviados

---

## Resumo

- Campos: 10
- Chave Primária: 4 campo(s)
- Índices: 3
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
| StaCmd | Number(001,0) | Sim | Status do Comando |
| DatEnv | Date | Sim | Data de Envio do Comando |
| HorEnv | Number(005,0) | Sim | Hora de Envio do Comando |
| SeqEnv | Number(003,0) | Sim | Sequência do Registro |
| RetCmd | String(255) | Sim | Mensagem de Retorno do Comando |

---

## Chave Primária

- CodCmd
- CodPlt
- CodRlg
- IdtReg

---

## Índices

### R600LCEIndice2

**Tipo:** Não unico

Campos:
- CodCmd
- IdtReg

### R600LCEIndice3

**Tipo:** Não unico

Campos:
- DatEnv
- HorEnv

### R600LCEIndice4

**Tipo:** Não unico

Campos:
- NumFis

---

## Relacionamentos

### IR_R600LCE_001

**Tabela:** R058PLT

| Origem | Destino |
|--------|---------|
| CodPlt | CodPlt |

### IR_R600LCE_002

**Tabela:** R058RLG

| Origem | Destino |
|--------|---------|
| CodPlt | CodPlt |
| CodRlg | CodRlg |

