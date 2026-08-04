# E055SPC

## Descrição

Tabelas - Impostos - Parâmetro Contribuição SPED Pis/Cofins

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
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| CodImp | String(003) | Não | Código do imposto |
| DatBas | Date | Não | Data base inicial de validade para apuração do valor base do imposto |
| ConSoc | Number(002,0) | Não | Código da contribuição social apurada |
| CodDfs | Number(006,0) | Sim | Código do dispositivo fiscal |

---

## Chave Primária

- CodEmp
- CodFil
- CodImp
- DatBas
- ConSoc

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E055SPC_002

**Tabela:** E055PAR

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodFil | CodFil |
| CodImp | CodImp |

