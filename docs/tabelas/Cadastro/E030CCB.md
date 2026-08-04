# E030CCB

## Descrição

Cadastros - Bancos - Configurações Correspondente Bancário

---

## Resumo

- Campos: 11
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodBan | String(003) | Não | Código do banco na Febraban |
| CodEmp | Number(004,0) | Não | Código da empresa |
| TptPgt | String(003) | Sim | Tipo de título padrão para efetuar pagamento de operações com corresp.bancário |
| TnsPgt | String(005) | Sim | Transação padrão para efetuar pagamento de operações com corresp.bancário |
| CbrCom | Number(001,0) | Não | Indica o tipo de cobrança padrão da comissão das operações com Corresp. Bancário |
| TptRec | String(003) | Sim | Tipo de título padrão para cobrança de operações com Corresp. Bancário |
| TnsRec | String(005) | Sim | Transação padrão para cobrança de operações com Corresp. Bancário |
| FilSnf | Number(005,0) | Sim | Código da filial para Série de Nota Fiscal |
| CodSnf | String(003) | Sim | Código da Série de Nota Fiscal a ser gerada para recebimento de comissão |
| CodSer | String(014) | Sim | Código de serviço do item de nota a ser gerada para recebimento de comissão |
| TnsSnf | String(005) | Sim | Transação padrão a ser gerada para recebimento de comissão via nota de serviço |

---

## Chave Primária

- CodBan
- CodEmp

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E030CCB_000

**Tabela:** E030BAN

| Origem | Destino |
|--------|---------|
| CodBan | CodBan |

