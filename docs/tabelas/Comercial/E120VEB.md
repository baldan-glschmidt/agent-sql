# E120VEB

## Descrição

Vendas - Pedidos - Veículos do Embarque

---

## Resumo

- Campos: 10
- Chave Primária: 5 campo(s)
- Índices: 1
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| NumPed | Number(008,0) | Não | Número do pedido |
| NumEbp | Number(004,0) | Não | Número do embarque do pedido |
| SeqVeb | Number(003,0) | Não | Sequência |
| CodTip | Number(004,0) | Não | Código do tipo de veículo |
| DatCar | Date | Sim | Data do carregamento do veículo |
| UsuLib | Number(010,0) | Sim | Usuário responsável pela liberação financeira do veículo do embarque |
| DatLib | Date | Sim | Data liberação financeira do veículo |
| HorLib | Number(005,0) | Sim | Hora liberação financeira do veículo do embarque |

---

## Chave Primária

- CodEmp
- CodFil
- NumPed
- NumEbp
- SeqVeb

---

## Índices

### E120VEBIndice1

**Tipo:** Não unico

Campos:
- CodTip

---

## Relacionamentos

### IR_E120VEB_003

**Tabela:** E120EBP

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodFil | CodFil |
| NumPed | NumPed |
| NumEbp | NumEbp |

### IR_E120VEB_005

**Tabela:** E073TIP

| Origem | Destino |
|--------|---------|
| CodTip | CodTip |

