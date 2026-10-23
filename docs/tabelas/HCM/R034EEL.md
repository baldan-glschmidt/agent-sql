# R034EEL

## Descrição

Colaborador - Endereços eletrônicos

---

## Resumo

- Campos: 6
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do Colaborador |
| CodEEl | Number(004,0) | Não | Código do tipo de endereço eletrônico |
| SeqEEl | Number(002,0) | Não | Sequência |
| EndEle | String(250) | Sim | Endereço eletrônico |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- CodEEl
- SeqEEl

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R034EEL_003

**Tabela:** R022EEL

| Origem | Destino |
|--------|---------|
| CodEEl | CodEEl |

