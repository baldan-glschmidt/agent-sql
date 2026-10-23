# R124QID

## Descrição

Colaborador - Itens de Respostas Descritivas

---

## Resumo

- Campos: 8
- Chave Primária: 7 campo(s)
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
| DesRes | String(400) | Sim | Descrição da Resposta |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- CodQue
- DatQue
- CodPer
- IteRes

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R124QID_004

**Tabela:** R124QRE

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |
| CodQue | CodQue |
| DatQue | DatQue |

### IR_R124QID_006

**Tabela:** R117IRE

| Origem | Destino |
|--------|---------|
| CodPer | CodPer |
| IteRes | IteRes |

