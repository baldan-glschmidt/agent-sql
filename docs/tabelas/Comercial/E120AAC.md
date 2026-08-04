# E120AAC

## Descrição

Vendas - Pedidos - Aprovação da Análise de Crédito

---

## Resumo

- Campos: 11
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
| SeqPac | Number(004,0) | Não | Sequência da análise de crédito do pedido |
| UsuApr | Number(010,0) | Sim | Usuário responsável pela aprovação da análise de crédito do pedido |
| RotNap | Number(002,0) | Sim | Código da rotina para controle de aprovação |
| NumApr | Number(010,0) | Sim | Número da aprovação gerado pelo sistema |
| SitApr | String(003) | Sim | Situação do controle de aprovação |
| UsuGer | Number(010,0) | Sim | Usuário responsável pela geração do registro |
| DatGer | Date | Sim | Data da geração do registro |
| HorGer | Number(005,0) | Sim | Hora da geração do registro |

---

## Chave Primária

- CodEmp
- CodFil
- NumPed
- SeqPac

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E120AAC_001

**Tabela:** E070FIL

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodFil | CodFil |

