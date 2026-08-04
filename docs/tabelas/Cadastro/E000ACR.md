# E000ACR

## Descrição

Tabelas - Integrações - Hub de Royalties - Atualização de Consumo de Royalties

---

## Resumo

- Campos: 5
- Chave Primária: 1 campo(s)
- Índices: 1
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| SeqInt | Number(008,0) | Não | Sequência da integração |
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| DatEnt | Date | Não | Data da entrada |
| SeqEnt | Number(006,0) | Não | Sequência de entrada na data |

---

## Chave Primária

- SeqInt

---

## Índices

### E000ACRIndice1

**Tipo:** Unico

Campos:
- CodEmp
- CodFil
- DatEnt
- SeqEnt

---

## Relacionamentos

Nenhum relacionamento cadastrado.
