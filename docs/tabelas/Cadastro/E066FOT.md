# E066FOT

## Descrição

Cadastros - Filiais de Operadoras de Telefonia

---

## Resumo

- Campos: 20
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodOte | Number(004,0) | Não | Código da operadora de telefonia |
| CodFot | Number(003,0) | Não | Sequencia da filial de operadora de telefonia |
| NomFot | String(100) | Sim | Nome da filial da operadora de telefonia |
| CodCli | Number(009,0) | Sim | Código do cliente relacionado ao cadastro da operadora |
| CodFor | Number(009,0) | Sim | Código do fornecedor relacionado ao cadastro da operadora |
| PerRep | Number(005,2) | Sim | Percentual de comissão a ser pago ao representante da venda. |
| PerCom | Number(005,2) | Sim | Percentual de comissão a ser paga a loja pela venda |
| OpeTef | String(030) | Sim | Operadora identificada pelo TEF |
| ObsOte | String(200) | Sim | Observação sobre a operada de telefonia |
| SitFot | String(001) | Não | Situação da filial de operadora de telefonia |
| TptPgt | String(003) | Sim | Tipo de título padrão para efetuar pagamento/repasse das recargas de celular |
| TnsPgt | String(005) | Sim | Transação padrão para efetuar pagamento das recargas de celular |
| CbrCom | Number(001,0) | Sim | Indica o tipo de cobrança padrão da comissão |
| TptRec | String(003) | Sim | Tipo de título padrão para cobrança de comissão |
| TnsRec | String(005) | Sim | Transação padrão para cobrança de comissão |
| FilSnf | Number(005,0) | Sim | Código da filial para Série de Nota Fiscal |
| CodSnf | String(003) | Sim | Código da Série de Nota Fiscal a ser gerada para recebimento de comissão |
| CodSer | String(014) | Sim | Código de serviço do item de nota a ser gerada para recebimento de comissão |
| TnsSnf | String(005) | Sim | Transação padrão a ser gerada para recebimento de comissão via nota de serviço |

---

## Chave Primária

- CodEmp
- CodOte
- CodFot

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
