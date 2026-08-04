# E081FLC

## Descrição

Tabelas - Tabela de Preços de Frete - Preços por Localização

---

## Resumo

- Campos: 15
- Chave Primária: 5 campo(s)
- Índices: 1
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodTab | String(004) | Não | Código da tabela de preço frete |
| DatIni | Date | Não | Data início de validade da tabela de preço |
| LocEnt | Number(008,0) | Não | Código da localização do local para entrega do frete |
| SeqFlc | Number(004,0) | Não | Sequência da localização do frete |
| FilFlc | Number(005,0) | Sim | Código da filial |
| VlrIni | Number(015,2) | Não | Valor Inicial |
| VlrFim | Number(015,2) | Não | Valor Final |
| Desfre | String(050) | Sim | Descrição do frete |
| FreCli | Number(015,2) | Sim | Valor do frete a ser cobrado do cliente |
| PerCli | Number(005,2) | Sim | Percentual frete a ser cobrado do cliente |
| FreMot | Number(015,2) | Sim | Valor do frete a ser pago ao motorista |
| PerMot | Number(005,2) | Sim | Percentual do frete a ser pago ao motorista |
| CodSer | String(014) | Sim | Código do serviço da tabela de preço de frete |
| SitReg | String(001) | Não | Situação |

---

## Chave Primária

- CodEmp
- CodTab
- DatIni
- LocEnt
- SeqFlc

---

## Índices

### E081FLCIndice1

**Tipo:** Unico

Campos:
- CodEmp
- CodTab
- DatIni
- LocEnt
- CodSer

---

## Relacionamentos

Nenhum relacionamento cadastrado.
