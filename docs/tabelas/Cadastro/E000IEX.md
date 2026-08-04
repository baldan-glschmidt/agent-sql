# E000IEX

## Descrição

Tabelas - Integrações - Índices de controle de exportação dados

---

## Resumo

- Campos: 32
- Chave Primária: 0 campo(s)
- Índices: 3
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodInt | Number(002,0) | Não | Código da Integração |
| IdeInt | String(015) | Não | Código Identificador do tipo de informação |
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| TipExp | Number(002,0) | Não | Tipo de Exportação |
| IndExp | String(001) | Não | Indicativo de Exportação |
| CodCli | Number(009,0) | Sim | Código do cliente |
| CodFpg | Number(002,0) | Sim | Código da forma de pagamento |
| CodCpg | String(006) | Sim | Código da condição de pagamento |
| UniMed | String(003) | Sim | Código da unidade de medida |
| CodTpt | String(003) | Sim | Código interno do tipo de título |
| CodCnv | Number(004,0) | Sim | Código do convênio |
| CodMoe | String(003) | Sim | Código da moeda ou índice |
| CodRep | Number(009,0) | Sim | Código do representante |
| CodTns | String(005) | Sim | Código da transação |
| CodTra | Number(009,0) | Sim | Código da Transportadora |
| CodPro | String(014) | Sim | Código do produto |
| CodDer | String(007) | Sim | Código da derivação do Produto (tamanho, cor, etc.) |
| CodSer | String(014) | Sim | Código do serviço |
| CodTpr | String(004) | Sim | Código da tabela de preço |
| CodDep | String(010) | Sim | Código do depósito |
| CodOpe | Number(004,0) | Sim | Código da operadora |
| NumPed | Number(008,0) | Sim | Número do pedido |
| DatIni | Date | Sim | Data validade inicial da tabela de preço |
| DatExp | Date | Não | Data da última exportação dos dados |
| HorExp | Number(005,0) | Não | Hora da última exportação dos dados |
| DatAlt | Date | Não | Data da última alteração do registro |
| HorAlt | Number(005,0) | Não | Hora da última alteração dos dados |
| SegAlt | Number(005,0) | Sim | Segundo e milissegundo da alteração |
| UsuAlt | Number(010,0) | Sim | Usuário responsável pela última alteração do registro |
| SitIex | String(001) | Sim | Situação do processamento da pendência de integração |
| MsgErr | String(100) | Sim | Mensagem de erro ocorrida no processamento |

---

## Chave Primária

Não possui.

---

## Índices

### E000IEXIndice1

**Tipo:** Não unico

Campos:
- CodInt
- IdeInt
- CodEmp
- CodFil
- TipExp

### E000IEXIndice2

**Tipo:** Não unico

Campos:
- CodInt
- IdeInt
- CodEmp
- CodFil
- TipExp
- IndExp
- CodCli

### E000IEXIndice3

**Tipo:** Não unico

Campos:
- CodInt
- IdeInt
- CodEmp
- CodFil
- TipExp
- IndExp
- CodPro
- CodDer

---

## Relacionamentos

Nenhum relacionamento cadastrado.
