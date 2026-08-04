# E120EBP

## Descrição

Vendas - Pedidos - Embarques do Pedido

---

## Resumo

- Campos: 12
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| NumPed | Number(008,0) | Não | Número do pedido |
| NumEbp | Number(004,0) | Não | Número do embarque do pedido |
| DatEng | Date | Não | Data limite para engenharia |
| DatPrd | Date | Não | Data limite para produção |
| DatEbq | Date | Não | Data limite para embarque |
| ObsEbp | String(250) | Sim | Texto da observação do embarque |
| SitEbp | Number(002,0) | Não | Situação do embarque |
| UsuGer | Number(010,0) | Sim | Usuário responsável pela geração do registro |
| DatGer | Date | Sim | Data da geração do registro |
| HorGer | Number(005,0) | Sim | Hora da geração do registro |

---

## Chave Primária

- CodEmp
- CodFil
- NumPed
- NumEbp

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E120EBP_002

**Tabela:** E120PED

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodFil | CodFil |
| NumPed | NumPed |

