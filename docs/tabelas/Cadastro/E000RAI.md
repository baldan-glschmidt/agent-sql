# E000RAI

## Descrição

Tabelas - Integrações - Retorno de Análise de Crédito

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
| NumPed | Number(008,0) | Não | Número do pedido |
| SeqSpa | Number(004,0) | Não | Sequência do situação do pedido na análise de crédito |

---

## Chave Primária

- SeqInt

---

## Índices

### E000RAIIndice1

**Tipo:** Unico

Campos:
- CodEmp
- CodFil
- NumPed
- SeqSpa

---

## Relacionamentos

### IR_E000RAI_001

**Tabela:** E070EMP

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |

