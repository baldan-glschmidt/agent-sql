# E020SEL

## Descrição

Cadastros - Controle dos Selos de IPI

---

## Resumo

- Campos: 12
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| CodSip | String(010) | Não | Código do selo do IPI |
| GruSip | String(050) | Não | Grupo do selo do IPI |
| CorSip | String(030) | Não | Cor do selo do IPI |
| NumGui | String(010) | Não | Número da guia do fornecimento do lote dos selos de IPI |
| SerSip | String(006) | Sim | Série do selo do IPI |
| DatGui | Date | Não | Data do fornecimento da guia |
| QtdSip | Number(015,0) | Sim | Quantidade de selos de IPI |
| SelIni | Number(015,0) | Sim | Número do selo inicial |
| SelFim | Number(015,0) | Sim | Número do selo final |
| SalSel | Number(015,0) | Sim | Saldo de selos do IPI |

---

## Chave Primária

- CodEmp
- CodFil
- CodSip

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E020SEL_001

**Tabela:** E070FIL

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodFil | CodFil |

