# R109EEX

## Descrição

PCMSO - Exceções individuais de exames

---

## Resumo

- Campos: 6
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 3

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código Empresa |
| CodPcm | Number(004,0) | Não | Código de identificação do PCMSO |
| CodFic | Number(009,0) | Não | Código ficha médica |
| DatIni | Date | Não | Data de início da exceção do exame periódico |
| CodExa | Number(004,0) | Não | Código do Exame |
| DatTer | Date | Sim | Data de término da exceção do exame periódico |

---

## Chave Primária

- NumEmp
- CodPcm
- CodFic
- DatIni
- CodExa

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R109EEX_001

**Tabela:** R109PCM

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodPcm | CodPcm |

### IR_R109EEX_002

**Tabela:** R110FIC

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodFic | CodFic |

### IR_R109EEX_004

**Tabela:** R108EXA

| Origem | Destino |
|--------|---------|
| CodExa | CodExa |

