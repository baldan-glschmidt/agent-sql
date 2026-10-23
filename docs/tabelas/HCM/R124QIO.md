# R124QIO

## Descrição

Colaborador - Itens de Respostas Objetivas

---

## Resumo

- Campos: 8
- Chave Primária: 8 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo do Entrevistado |
| NumCad | Number(009,0) | Não | Cadastro do Entrevistado |
| CodQue | Number(002,0) | Não | Código do Questionário |
| DatQue | Date | Não | Data da Resposta do Questionário |
| CodPer | Number(002,0) | Não | Código da Pergunta |
| IteRes | Number(002,0) | Não | Item Resposta |
| IteEsc | Number(002,0) | Não | Item de Escolha da Resposta |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- CodQue
- DatQue
- CodPer
- IteRes
- IteEsc

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R124QIO_004

**Tabela:** R124QRE

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |
| CodQue | CodQue |
| DatQue | DatQue |

### IR_R124QIO_007

**Tabela:** R117IER

| Origem | Destino |
|--------|---------|
| CodPer | CodPer |
| IteRes | IteRes |
| IteEsc | IteEsc |

