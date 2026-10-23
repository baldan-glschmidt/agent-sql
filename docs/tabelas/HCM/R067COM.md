# R067COM

## Descrição

Log de Envio de Comandos

---

## Resumo

- Campos: 9
- Chave Primária: 3 campo(s)
- Índices: 2
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| DatLog | Date | Não | Data do Log |
| HorLog | Number(005,0) | Não | Hora do Log |
| SeqLog | Number(002,0) | Não | Sequência do Registro |
| CodCmd | Number(003,0) | Sim | Código do Comando |
| CnxUsu | Number(005,0) | Sim | Número da Conexão do Usuário |
| CodPlt | Number(005,0) | Sim | Código do Site |
| CodRlg | Number(005,0) | Sim | Código do Coletor |
| CodUsu | Number(010,0) | Sim | Código do Usuário do Processamento |
| MsgLog | String(300) | Sim | Mensagem do Log |

---

## Chave Primária

- DatLog
- HorLog
- SeqLog

---

## Índices

### R067COMIndice2

**Tipo:** Não unico

Campos:
- CodPlt
- CodRlg

### R067COMIndice3

**Tipo:** Não unico

Campos:
- CodCmd

---

## Relacionamentos

### IR_R067COM_005

**Tabela:** R058PLT

| Origem | Destino |
|--------|---------|
| CodPlt | CodPlt |

### IR_R067COM_006

**Tabela:** R058RLG

| Origem | Destino |
|--------|---------|
| CodPlt | CodPlt |
| CodRlg | CodRlg |

