# E000TMO

## Descrição

Tabelas - Integrações - Transações X Motivos

---

## Resumo

- Campos: 5
- Chave Primária: 1 campo(s)
- Índices: 1
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| SeqInt | Number(009,0) | Não | Número sequencial dos registros de integração |
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| CodTns | String(005) | Não | Código da transação |
| CodMot | Number(006,0) | Não | Código do motivo |

---

## Chave Primária

- SeqInt

---

## Índices

### E000TMOIndice1

**Tipo:** Não unico

Campos:
- CodEmp
- CodFil
- CodTns
- CodMot

---

## Relacionamentos

### IR_E000TMO_004

**Tabela:** E001TMO

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodFil | CodFil |
| CodTns | CodTns |
| CodMot | CodMot |

