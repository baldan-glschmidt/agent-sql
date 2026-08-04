# E140PMV

## Descrição

Vendas - Notas Fiscais de Saída - Pendência de movimentação de estoque

---

## Resumo

- Campos: 30
- Chave Primária: 1 campo(s)
- Índices: 5
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| SeqPmv | Number(009,0) | Não | Sequencia movimento |
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| CodSnf | String(003) | Não | Código da série da nota fiscal |
| NumNfv | Number(009,0) | Não | Número da nota fiscal de saída |
| SeqIpv | Number(003,0) | Não | Sequência do item na nota fiscal de saída |
| CodPro | String(014) | Sim | Código do produto |
| CodDer | String(007) | Sim | Código da derivação |
| CodDep | String(010) | Sim | Código do depósito |
| SeqAgr | Number(009,0) | Sim | Sequencia do agrupamento |
| SitPmv | Number(001,0) | Não | Situação da pendência |
| MsgExe | String(999) | Sim | Mensagem de informação relacionada a execução |
| UsuGer | Number(010,0) | Sim | Usuário responsável pela geração do registro |
| DatGer | Date | Sim | Data da geração do registro |
| HorGer | Number(005,0) | Sim | Hora da geração do registro |
| UsuAlt | Number(010,0) | Sim | Usuário responsável pela última alteração do registro |
| DatAlt | Date | Sim | Data da última alteração do registro |
| HorAlt | Number(005,0) | Sim | Hora da última alteração do registro |
| CodLot | String(050) | Sim | Código do Lote de Fabricação para estocagem |
| QtdMov | Number(014,5) | Sim | Quantidade do movimento |
| VlrMov | Number(015,2) | Sim | Valor do movimento |
| TnsEst | String(005) | Sim | Código da transação de estoque |
| CmpKit | Number(001,0) | Sim | Indica que o item a ser movimnetado é um componente kit |
| FilPed | Number(005,0) | Sim | Código da filial do pedido |
| NumPed | Number(008,0) | Sim | Número do pedido |
| SeqIpd | Number(004,0) | Sim | Sequência do item do pedido |
| QtdTtv | Number(004,0) | Sim | Quantidade total de tentativas de movimentação já efetuadas |
| QtdTat | Number(004,0) | Sim | Quantidade de tentativas desde que foi zerado o contador |
| HorExe | Number(005,0) | Sim | Hora da execução da primeira tentativa de movimentação |
| DatExe | Date | Sim | Data de execução da primeira tentativa de movimentação |

---

## Chave Primária

- SeqPmv

---

## Índices

### E140PMVProduto

**Tipo:** Não unico

Campos:
- CodEmp
- CodFil
- CodPro
- CodDer
- CodDep

### E140PMVNotaFiscal

**Tipo:** Não unico

Campos:
- CodEmp
- CodFil
- CodSnf
- NumNfv

### E140PMVDataGeracao

**Tipo:** Não unico

Campos:
- DatGer

### E140PMVAgrupamento

**Tipo:** Não unico

Campos:
- SeqAgr

### E140PMVQtdTentativa

**Tipo:** Não unico

Campos:
- QtdTat
- DatAlt
- HorAlt

---

## Relacionamentos

Nenhum relacionamento cadastrado.
