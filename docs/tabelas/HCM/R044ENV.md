# R044ENV

## Descrição

Códigos de Cálculo - Mensagens de Envelope

---

## Resumo

- Campos: 6
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| CodCal | Number(005,0) | Não | Código de Cálculo |
| SeqEnv | Number(002,0) | Não | Sequência |
| ExcCal | Number(001,0) | Sim | Tipo de Exceção do Código de Cálculo |
| AbrExc | String(100) | Sim | Abrangência |
| MsgEnv | String(070) | Sim | Mensagem do Envelope |

---

## Chave Primária

- NumEmp
- CodCal
- SeqEnv

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R044ENV_001

**Tabela:** R044CAL

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodCal | CodCal |

