# E070FRE

## Descrição

Cadastros - Filiais - Parâmetros Gestão Contas a Receber

---

## Resumo

- Campos: 18
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| RecTre | String(005) | Sim | Transação padrão para baixa de títulos por entrada na renegociação de títulos |
| RecTcr | String(005) | Sim | Transação padrão para baixa de títulos por Crédito na renegociação de títulos |
| RecTtr | String(005) | Sim | Transação padrão para movimento de tesouraria na renegociação de títulos |
| CtaRci | String(014) | Sim | Número da conta interna para baixa de renegociação |
| PadTns | String(005) | Sim | Transação padrão para recebimento de ajuste em contrato derivativo |
| PadTpt | String(003) | Sim | Tipo de título padrão para recebimento de ajuste em contrato derivativo |
| StiReg | String(003) | Sim | Série padrão para renegociação |
| TptReg | String(003) | Sim | Tipo de título padrão para a renegociação |
| UsaPre | String(001) | Não | Usa prefixo para título na renegociação |
| PreReg | String(003) | Sim | Prefixo para geração de título na renegociação |
| MotObs | Number(006,0) | Sim | Código do motivo da observação da renegociação |
| MotCan | Number(006,0) | Sim | Código do motivo da observação do cancelamento da renegociação |
| TnsBrd | String(005) | Sim | Transação padrão para baixa do recebimento de ajuste em contrato derivativo |
| CcrTns | String(005) | Sim | Transação padrão entrada de títulos a receber em contratos de empréstimo |
| CcrTpt | String(003) | Sim | Tipo de título padrão entrada de títulos a receber em contratos de empréstimo |
| CteTns | String(005) | Sim | Transação para cancelamento de títulos a receber ao emitir CT-e de substituição |

---

## Chave Primária

- CodEmp
- CodFil

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
