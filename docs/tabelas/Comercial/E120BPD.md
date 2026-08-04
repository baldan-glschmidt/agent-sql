# E120BPD

## Descrição

Vendas - Pedidos - Bloqueios do Pedido

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
| SeqBlo | Number(005,0) | Não | Sequência do item de bloqueio |
| ProSer | String(001) | Sim | Indicativo se é bloqueio de produto ou serviço |
| SeqIte | Number(004,0) | Não | Sequência do item de produto ou serviço |
| TipBlo | Number(002,0) | Sim | Tipo do bloqueio do pedido |
| VlrInf | Number(015,2) | Sim | Valor Informado |
| VlrPer | Number(015,2) | Sim | Valor Permitido para a ação |
| BloLib | String(001) | Sim | Indicativo se o bloqueio está liberado |
| UsuGer | Number(009,0) | Sim | Usuário responsável pela liberação do bloqueio |
| UsuBlo | Number(009,0) | Sim | Usuário responsável pela geração do bloqueio |

---

## Chave Primária

- CodEmp
- CodFil
- NumPed
- SeqBlo

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E120BPD_001

**Tabela:** E070FIL

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodFil | CodFil |

