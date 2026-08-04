# E065AVL

## Descrição

Cadastros - Agenda de Visitas/Ligações

---

## Resumo

- Campos: 15
- Chave Primária: 2 campo(s)
- Índices: 1
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| DatVis | Date | Não | Data para o contato com o cliente |
| SeqVis | Number(004,0) | Não | Sequência da visita |
| CodCli | Number(009,0) | Não | Código do Cliente |
| CodRep | Number(009,0) | Sim | Código do representante |
| HorIni | Number(005,0) | Sim | Hora inicial para visita/ligação |
| HorFim | Number(005,0) | Sim | Hora final para visita/ligação |
| SeqCto | Number(005,0) | Não | Sequência de contato |
| ObsVis | String(250) | Sim | Observação da Visita/Ligação |
| CodNve | Number(002,0) | Não | Código do Motivo de Não Venda |
| EmpPed | Number(004,0) | Sim | Código da empresa do pedido |
| FilPed | Number(005,0) | Sim | Código da filial do Pedido |
| NumPed | Number(008,0) | Sim | Número do pedido |
| SeqIpd | Number(004,0) | Sim | Sequência de item do pedido |
| MotAge | Number(006,0) | Sim | Código do motivo do agendamento |
| VarSer | String(001) | Sim | Indica o tipo de serviço para o Varejo |

---

## Chave Primária

- DatVis
- SeqVis

---

## Índices

### E065AVLIndice1

**Tipo:** Não unico

Campos:
- CodCli

---

## Relacionamentos

### IR_E065AVL_002

**Tabela:** E085CLI

| Origem | Destino |
|--------|---------|
| CodCli | CodCli |

