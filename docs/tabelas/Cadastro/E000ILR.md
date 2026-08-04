# E000ILR

## Descrição

Tabelas - Integrações - Carga Inicial

---

## Resumo

- Campos: 9
- Chave Primária: 1 campo(s)
- Índices: 1
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| SeqIlr | Number(009,0) | Não | Número sequencial dos registros de inicialização |
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| CodInt | Number(002,0) | Não | Código do sistema integrado |
| DatIni | Date | Não | Data em que o processo foi inicializado |
| DatFim | Date | Não | Data em que o processo foi finalizado |
| HorIni | Number(005,0) | Sim | Hora de início do processo |
| HorFim | Number(005,0) | Sim | Hora de finalização do processo |
| SitIlr | Number(001,0) | Sim | Situação do processo |

---

## Chave Primária

- SeqIlr

---

## Índices

### E000ILRIndice1

**Tipo:** Não unico

Campos:
- CodEmp
- CodFil
- CodInt

---

## Relacionamentos

### IR_E000ILR_002

**Tabela:** E070FIL

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodFil | CodFil |

