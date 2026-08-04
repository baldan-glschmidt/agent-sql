# E009PTE

## Descrição

Tabelas - Parâmetros por Transação e Estado

---

## Resumo

- Campos: 13
- Chave Primária: 2 campo(s)
- Índices: 1
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da Empresa |
| SeqPte | Number(004,0) | Não | Seqüência de registro |
| CodFil | Number(005,0) | Sim | Código da filial |
| TnsBpo | String(005) | Não | Transação base de pedido ou ordem de compra |
| SigUfs | String(002) | Sim | Sigla do estado |
| TnsPro | String(005) | Sim | Transação de produto para NF saída ou NF entrada |
| TnsSer | String(005) | Sim | Transação de serviço para NF saída ou NF entrada |
| CprFix | String(005) | Sim | Transação padrão para NF de entrada na fixação de preços |
| VenTdp | String(005) | Sim | Transação padrão de devolução de itens de produto |
| TnsDtp | String(005) | Sim | Transação padrão de devolução para transferência entre produtores |
| TnsDfp | String(005) | Sim | Transação padrão de devolução para fixação de preços |
| VenTdt | String(005) | Sim | Transação de Devolução de Produto em Taxa |
| CprTct | String(005) | Sim | Transação de Compra de Produto em Taxa |

---

## Chave Primária

- CodEmp
- SeqPte

---

## Índices

### E009PTEIndice2

**Tipo:** Unico

Campos:
- CodEmp
- TnsBpo
- SigUfs
- CodFil

---

## Relacionamentos

### IR_E009PTE_003

**Tabela:** E001TNS

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| TnsBpo | CodTns |

