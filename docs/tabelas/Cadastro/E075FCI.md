# E075FCI

## Descrição

Cadastros - Cálculo do FCI

---

## Resumo

- Campos: 22
- Chave Primária: 8 campo(s)
- Índices: 1
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| CodPro | String(014) | Não | Código do produto |
| CodDer | String(007) | Não | Código da derivação |
| NumSep | String(050) | Não | Número de série do produto |
| CodLot | String(050) | Não | Código do lote de fabricação do produto |
| CodDep | String(010) | Não | Código do depósito |
| PerFim | Date | Não | Competência de cálculo do FCI |
| VlrImp | Number(015,2) | Sim | Valor da parcela importada do exterior |
| VlrSai | Number(015,2) | Sim | Valor da saída interestadual da mercadoria |
| CoeFci | Number(005,2) | Sim | Coeficiente do conteúdo de importação calculado |
| CodFci | String(036) | Sim | Código da ficha de conteúdo de importação (FCI) |
| RecEnt | String(015) | Sim | Número do recibo de entrega do FCI |
| UsuGer | Number(010,0) | Sim | Usuário responsável pela geração do registro |
| DatGer | Date | Sim | Data da geração do registro |
| HorGer | Number(005,0) | Sim | Hora da geração do registro |
| UsuAlt | Number(010,0) | Sim | Usuário responsável pela última alteração do registro |
| DatAlt | Date | Sim | Data da última alteração do registro |
| HorAlt | Number(005,0) | Sim | Hora da última alteração do registro |
| OriMer | String(001) | Sim | Origem fiscal da mercadoria |
| VlrInt | Number(015,2) | Sim | Valor da saída estadual da mercadoria |
| CoeInt | Number(005,2) | Sim | Coeficiente do conteúdo de importação para o mercado interno calculado |

---

## Chave Primária

- CodEmp
- CodFil
- CodPro
- CodDer
- NumSep
- CodLot
- CodDep
- PerFim

---

## Índices

### E075FCIIndice1

**Tipo:** Não unico

Campos:
- CodEmp
- CodPro

---

## Relacionamentos

### IR_E075FCI_002

**Tabela:** E075PRO

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodPro | CodPro |

